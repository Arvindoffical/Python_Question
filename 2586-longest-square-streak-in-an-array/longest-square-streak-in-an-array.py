class Solution:
    def longestSquareStreak(self, a: List[int]) -> int:
        return (-1,r:=max(map(f:=lambda v:1+(v*v in a and f(v*v)),a:={*a})))[r>1]