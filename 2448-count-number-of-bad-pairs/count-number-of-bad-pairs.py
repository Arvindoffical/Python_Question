from collections import defaultdict

class Solution:
    def countBadPairs(self, nums: list[int]) -> int:
        mp = defaultdict(int)
        for i, num in enumerate(nums):
            mp[i - num] += 1
        
        ans = sum((count * (count - 1)) // 2 for count in mp.values())
        n = len(nums)
        tot = (n * (n - 1)) // 2
        return tot - ans