import cx_Oracle
import pandas as pd
import numpy as np
from sqlalchemy.dialects.oracle import \
    BFILE, BLOB, CHAR, CLOB, DATE, \
    DOUBLE_PRECISION, FLOAT, INTERVAL, LONG, NCLOB, \
    NUMBER, NVARCHAR, NVARCHAR2, RAW, TIMESTAMP, VARCHAR, \
    VARCHAR2
import os

os.environ['NLS_LANG']='SIMPLIFIED CHINESE_CHINA.UTF8'


db=cx_Oracle.connect('用户名/密码@服务器IP地址:端口号/实例名')    #建立连接db
print("数据库版本："+db.version)
cr=db.cursor()      #创建游标cr
sql="delete from 表名 where VALUE_DATA=0"
# sql1="select MONITOR_ID,COLLECT_DATE,COLLECT_TIME,VALUE_DATA,UPLOAD,LESSEE_ID,rk " \
#         "from (" \
#             "select a.*,row_number() over(partition by MONITOR_ID order by COLLECT_TIME) rk " \
#         "from 表名  a " \
#     ")" \
#     "where rk>=1"

sql1="select * from (" \
    "select MONITOR_ID," \
        "to_date(substr(to_char(COLLECT_DATE,'yyyy-mm-dd hh:mi:ss'),0,10),'yyyy-mm-dd') COLLECT_DATE," \
        "COLLECT_DATE COLLECT_TIME," \
        "VALUE_DATA," \
        "UPLOAD," \
        "LESSEE_ID," \
        "row_number() over(partition by MONITOR_ID order by COLLECT_TIME) rk" \
    "from 表名" \
    "where MONITOR_ID in(" \
    "select MONITOR_ID from (" \
        "select b.MONITOR_ID MONITOR_ID" \
        "from (" \
            "select distinct MONITOR_ID" \
            "from monitor_data_relation t1 join monitor_item t2 " \
            "on t1.item_id=t2.item_id" \
            "where item_name like '%累计流量%' and item_name!='负累计流量' and item_name!='反向累计流量'" \
        ") a " \
        "left join" \
            "(SELECT distinct MONITOR_ID FROM 表名) b" \
        "on a.MONITOR_ID=b.MONITOR_ID" \
    ")where MONITOR_ID is not null" \
    ")" \
") where rk>=1"


cr.execute(sql)
cr.execute(sql1)     #通过游标执行sql
cf=cr.fetchall()        #通过游标获取记录，返回的是二维的元组列表
db.close()  # 关闭连接


def MDH_Data_Cleansing(db,cf):
    #将二维元组列表转为二维数组array
    demo=pd.array(cf)
    print(1)
    data_values=[i0[3] for i0 in demo]   #取出二维数组array中的data_values列数据,生成新数组data_values
    rk=[i1[6] for i1 in demo]   #取出二维array中的rk列数据,生成新数组rk
    print("data_values:",data_values,'\n')
    print("rk:",rk,'\n')

    # 对data数组中不符合单调递增趋势的异常数据进行替换
    m = len(rk)
    n = len(data_values)
    id_num = 1
    print(m, n)
    for i in range(1, m):
        for j in range(1, n):
            if (rk[i + 3] == 1):
                i += 4
                j += 4
                id_num += 1     #对递增趋势id进行计数
            else:
                if (data_values[i] > data_values[i - 1] and data_values[i] > data_values[i + 1] and data_values[i] >
                        data_values[i + 2]):
                    data_values[i] = data_values[i - 1]
                if (data_values[i] < data_values[i - 1]):
                    data_values[i] = data_values[i - 1]
                i += 1
                j += 1
            if (j == n - 3 * id_num):  # 下标j,控制跳出循环
                break
        if (i == m - 3):
            break

    ma_data=np.column_stack((demo,data_values))   #把一维数组data_values作为二维数组demo新的一列进行合并，合并后转为二维矩阵ma_data
    data=pd.DataFrame(ma_data,columns=['MONITOR_ID','COLLECT_DATE','COLLECT_TIME','VALUE_DATA_DEMO','UPLOAD','LESSEE_ID','RK','VALUE_DATA'])       #List转为表数据结构dataframe,并设置字段
    print(data.isnull())
    data.info()     #查看数据基本信息

    data.drop('VALUE_DATA_DEMO',axis=1,inplace=True)     #删除列VALUE_DATA_DEMO
    data.drop('RK', axis=1, inplace=True)  # 删除列RK
    data.dropna(subset=['VALUE_DATA'],axis=0,inplace=True)     #删除列VALUE_DATA存在缺失值的所在行
    data.drop_duplicates(subset=['MONITOR_ID','COLLECT_DATE','VALUE_DATA'],keep='first',inplace=True)      #根据两个列去进行去重

    '''
    去重的另一种脱裤子放屁的写法如下:
    data['new_column']=data['COLLECT_DATE'].map(str)+data['VALUE_DATA'].map(str)        #合并两列生成新的一列
    data.drop_duplicates(subset=['new_column'],keep='first',inplace=True)       #根据新列去进行去重
    data.drop('new_column',axis=1,inplace=True)     #删除列new_column
    '''

    pd.set_option('display.max_columns',None)      #控制台完整显示列
    pd.set_option('display.max_rows',2000)         #控制台显示2000行
    pd.set_option('max_colwidth',100)              #控制台显示values为100,默认长度是50
    print(data)

    MDH_Dataframe_toOracle(data)


def mapping_data_types(data):       #实现Dataframe字段的类型转换(必转，否则就是给自己挖坑，不要问我是怎么知道的)
    dtypedict = {}
    for i, j in zip(data.columns, data.dtypes):
        if "object" in str(j):
            dtypedict.update({i: VARCHAR(256)})
        if "int" in str(j):
            dtypedict.update({i: NUMBER(10, 2)})
        if "date" in str(j):
            dtypedict.update({i: DATE(19)})
    return dtypedict


def MDH_Dataframe_toOracle(data):       #将Dataframe数据写入ORACLE数据库
    from sqlalchemy import types, create_engine
    conn='oracle+cx_oracle://用户名/密码@服务器IP地址:端口号/实例名'        #连接字符串
    engine=create_engine(conn,encoding='utf-8',echo=True)
    from sqlalchemy.dialects.oracle import \
        BFILE, BLOB, CHAR, CLOB, DATE, \
        DOUBLE_PRECISION, FLOAT, INTERVAL, LONG, NCLOB, \
        NUMBER, NVARCHAR, NVARCHAR2, RAW, TIMESTAMP, VARCHAR, \
        VARCHAR2
    #print(engine)
    dtypedict = mapping_data_types(data)

    tableName='monitor_data_his_cleanaftertb'
    data.to_sql(tableName,con=engine,if_exists='append',dtype=dtypedict,chunksize=None,index=False)


if __name__ == '__main__':
    MDH_Data_Cleansing(db, cf)