class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # def twoSum(nums, target):
        numToIndex = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in numToIndex:
                return [numToIndex[complement], i]
            numToIndex[num] = i
        return []  # No solution found!
        