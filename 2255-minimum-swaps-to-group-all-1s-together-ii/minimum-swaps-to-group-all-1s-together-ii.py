class Solution:
    def minSwaps(self, nums: List[int]) -> int:
        cnt = sum(nums)
        nums += nums # To eliminate the circular property of the array, we can append the original array to itself. Then, we checcnt each subarray of length total.
        ans = zeroes = nums[:cnt].count(0)
        for i in range(cnt, len(nums)):
            if nums[i] == 0:
                zeroes += 1
            if nums[i-cnt] == 0:
                zeroes -= 1
            ans = min(ans, zeroes) # The number of swaps required is the number of 0’s in the subarray of length cnt
        return ans

    # or

    def minSwaps(self, nums: List[int]) -> int:
        cnt = sum(nums)
        if cnt == 0 or cnt == len(nums):
            return 0

        nums += nums
        curOnes = sum(nums[:cnt])
        ones = curOnes
        for i in range(len(nums)//2):
            curOnes = curOnes - nums[i] + nums[i + cnt]
            ones = max(curOnes, ones)
        
        return cnt - ones 