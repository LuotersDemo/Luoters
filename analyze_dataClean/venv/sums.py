class Solution:
    def twoSum(nums, target):
        n = len(nums)
        for i in range(n):
            j = i+1
            for j in range(n):
                if nums[i] + nums[j] == target:
                    return [i, j]



    if __name__ == '__main__':
        nums = [2,7,11,15]
        target = 9

        print(twoSum(nums, target))
