'''
66. 加一

给定一个由 整数 组成的 非空 数组所表示的非负整数，在该数的基础上加一。

最高位数字存放在数组的首位， 数组中每个元素只存储单个数字。

你可以假设除了整数 0 之外，这个整数不会以零开头。

示例1：
输入：digits = [1,2,3]
输出：[1,2,4]
解释：输入数组表示数字 123

示例2：
输入：digits = [4,3,2,1]
输出：[4,3,2,2]
解释：输入数组表示数字 4321

示例3：
输入：digits = [0]
输出：[1]
'''

class Solution:
    def plusOne(digits):
        n = len(digits)
        for i in range(n-1, -1, -1):
            if digits[i] != 9:
                digits[i] += 1
                for j in range(i+1, n):
                    digits[j] = 0

                return digits

        return [1] + [0]*n

    if __name__ == '__main__':
        # digits = [4, 3, 2, 1]
        digits = [1, 3, 5, 7, 9, 9]
        # digits = [9, 9, 9]

        print(plusOne(digits))


