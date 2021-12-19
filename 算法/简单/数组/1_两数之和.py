'''
1. 两数之和

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] ==target:
                    return [i, j]
'''

class Solution:
    def twoSum(nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]



    if __name__ == '__main__':
        # nums = [2,7,11,15]
        nums = [3,2,4]

        target = 6

        print(twoSum(nums, target))