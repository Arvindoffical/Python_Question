class Solution:
    def firstCompleteIndex(self, a: List[int], g: List[List[int]]) -> int:
        d = {v:i for i,v in enumerate(a)}
        q = [[d[v] for v in r] for r in g]

        return min(map(max, q+[*zip(*q)]))