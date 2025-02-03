class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        increase_count = decrease_count = max_length = 1
        
        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:  # Increasing sequence
                increase_count += 1
                decrease_count = 1
            elif nums[i] > nums[i + 1]:  # Decreasing sequence
                decrease_count += 1
                increase_count = 1
            else:  # Equal elements → reset both counts
                increase_count = decrease_count = 1
            
            max_length = max(
                max_length, increase_count, decrease_count
            )
        
        return max_length