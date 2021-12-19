'''
27. 移除元素

思路：与26. 删除有序数组中的重复项类似，快慢双指针

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        n = len(nums)
        fast = slow = 0
        while fast < n:
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow
'''

class Solution:
    def removeElement(num1, val):
        n = len(num1)
        slow = fast = 0
        while fast < n:
            if num1[fast] != val:
                num1[slow] = num1[fast]
                slow += 1
            fast += 1

        return slow, num1[0:slow]

    if __name__ == '__main__':
        num1 = [0,1,2,2,3,0,4,2]
        val = 2

        print(removeElement(num1, val))