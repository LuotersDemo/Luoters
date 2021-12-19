'''
88. 合并两个有序数组

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:] = nums2
        nums1.sort()
'''

class Solution:
    def merge(m, num1, num2):
        # num1[m:] = num2
        num1 = num1[0:m] + num2
        num1.sort()

        return num1

    if __name__ == '__main__':
        num1 = [1,2,3,0,0,0]
        num2 = [2,5,6]
        m = 3

        print(merge(m, num1, num2))