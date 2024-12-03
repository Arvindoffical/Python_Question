class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = -10000
        cur_sum = 0

        for i in nums:
            cur_sum += i
            cur_sum = max(cur_sum, i)
            max_sum = max(cur_sum, max_sum)
        
        return max_sum
                
