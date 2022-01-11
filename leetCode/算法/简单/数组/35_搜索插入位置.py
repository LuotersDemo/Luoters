'''
35. 搜索插入位置

思路：
    初始条件：left = 0, right = length-1
    终止：left <= right
    值相等：返回mid
    向左查找：
        是否同时满足nums[mid - 1] < target，满足返回mid;
        最左临界值判断;
        否则right = mid - 1
    向右查找：
        是否同时满足target < nums[mid + 1]，满足返回mid+1;
        最右临界值判断;
        否则left = mid + 1

给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

示例1：
输入: nums = [1,3,5,6], target = 5
输出: 2

示例2：
输入: nums = [1,3,5,6], target = 2
输出: 1

示例3：
输入: nums = [1,3,5,6], target = 7
输出: 4

示例4：
输入: nums = [1,3,5,6], target = 0
输出: 0

示例5：
输入: nums = [1], target = 0
输出: 0
'''

class Solution:
    def searchInsert(nums, target):
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
               return mid
            elif nums[mid] < target:
                if target < nums[mid + 1]:
                    return mid + 1
                elif nums[right] < target:
                    return right + 1
                else:
                    left = mid + 1
            elif nums[mid] > target:
                if nums[mid - 1] < target:
                    return mid
                elif target < nums[left]:
                    return left
                else:
                    right = mid - 1


    if __name__ == '__main__':
        nums = [1]
        target = 0

        print(searchInsert(nums, target))