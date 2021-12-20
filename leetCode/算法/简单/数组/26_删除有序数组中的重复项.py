'''
26. 删除有序数组中的重复项

思路：快慢指针都从下标1开始，[fast-1]、[fast]指针的值作为判定：
     值相等fast加1；
     值不想等slow内先加1并赋值，外再fast加1；

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        slow = fast = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1
        return slow
'''
class Solution:
    def removeDuplicates(nums):
        n = len(nums)

        fast = slow = 1
        while fast < n:
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1

        return slow, nums[0:slow]


    if __name__ == '__main__':
        nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
        print(removeDuplicates(nums))