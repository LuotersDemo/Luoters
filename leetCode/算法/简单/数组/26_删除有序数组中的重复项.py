'''
26. 删除有序数组中的重复项

思路：快慢指针都从下标1开始，[fast-1]、[fast]指针的值作为判定：
     值相等fast加1；
     值不想等slow内先加1并赋值，外再fast加1；

给你一个有序数组 nums ，请你 原地 删除重复出现的元素，使每个元素 只出现一次 ，返回删除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

示例1：
输入：nums = [1,1,2]
输出：2, nums = [1,2]
解释：函数应该返回新的长度 2 ，并且原数组 nums 的前两个元素被修改为 1, 2 。不需要考虑数组中超出新长度后面的元素。

示例2：
输入：nums = [0,0,1,1,1,2,2,3,3,4]
输出：5, nums = [0,1,2,3,4]
解释：函数应该返回新的长度 5 ， 并且原数组 nums 的前五个元素被修改为 0, 1, 2, 3, 4 。不需要考虑数组中超出新长度后面的元素。
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