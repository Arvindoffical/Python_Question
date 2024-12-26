class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        totalsum = sum(nums)
        offset = totalsum
        dp = [[-1 for _ in range(2*totalsum+1)] for _ in range(len(nums))]
        
        def rec(i,cs):
            if i == len(nums):
                if cs == target:
                    return 1
                else:
                    return 0
            if dp[i][cs+offset]!=-1:
                return dp[i][cs+offset]
            add = rec(i+1,cs+nums[i])
            sub = rec(i+1,cs-nums[i])
            dp[i][cs+offset] = add+sub
            return dp[i][cs+offset]
        return rec(0,0)
