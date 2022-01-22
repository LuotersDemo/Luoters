package firstSample;

/**
 * @author Luoters
 * @since 2022-01-22
 */
public class HelloWorld {

    public void isHelloWorld(){
        System.out.println("--------");
        String helloW = "hello world!";
        System.out.println(helloW);

        String helloW1 = helloW.substring(0, 7);
        System.out.println(helloW1);

        String helloW2 = helloW + helloW1;
        if (helloW != null && helloW.length() != 0 || helloW1 != null && helloW1.length() != 0) {
            System.out.println(helloW2);
        }

        System.out.println("--------");
        char helloW1At = helloW2.charAt(6);     //返回给定位置的代码单元
        System.out.println(helloW1At);

        int helloW2At = helloW1.codePointAt(6);
        System.out.println(helloW2At);          //返回给定位置开始的码点

        int helloW2_At = helloW2.offsetByCodePoints(6, 2);      //返回从startIndex码点开始，cpCount个码点之后的码点索引
        System.out.println(helloW2_At);

        int helloWAt = helloW.compareTo(helloW1);
        System.out.println(helloWAt);

        int[] helloWList = helloW.codePoints().toArray();
        System.out.println(helloWList);

        int helloWCount = helloW.codePointCount(3, 6);
        System.out.println(helloWCount);

        String helloWList1 = new String(helloWList, 2, 4);
        System.out.println(helloWList1);

        System.out.println("--------");
        if (helloW.isEmpty() == false) {
            System.out.println("hello is not empty!");
        }
        if (helloW.equals(helloW1) == false) {
            System.out.println("hello is not null!");
        }

        if (helloW.startsWith(helloW1) == true) {
            System.out.println("helloW is start with helloW1!");
        }

        int ll0Index =helloW.indexOf("llo", 1);
        System.out.println(ll0Index+"\n--------");

        System.out.println(helloW.length());

        String hello = helloW.replace(" world!", "");
        System.out.println(hello);

        System.out.println(helloW.substring(6));
        System.out.println(helloW.toUpperCase());
        System.out.println(" hello ".trim());


        System.out.println("".join(",", hello, "!"));



    }

}
