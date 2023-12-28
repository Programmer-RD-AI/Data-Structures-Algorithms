class Solution:
    def twoSum(self, nums, target: int) -> int:
        for num in range(len(nums)):
            print(nums)
            nums_copy = nums.copy()
            del nums_copy[num]
            for n in range(len(nums_copy)):
                if (nums_copy[num] + nums[n]) == target:
                    return [num, n]
        return [None, None]


print(Solution().twoSum([3, 3], 6))
