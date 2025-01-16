class Solution:
    def xorAllNums(self, a: List[int], b: List[int]) -> int:
        return len(a)%2*reduce(xor,b)^len(b)%2*reduce(xor,a)