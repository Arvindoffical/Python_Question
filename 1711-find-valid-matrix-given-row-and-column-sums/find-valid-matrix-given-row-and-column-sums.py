class Solution:
    def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        n, m = len(rowSum), len(colSum)
        res = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n):
            for j in range(m):
                nm = min(rowSum[i], colSum[j])
                res[i][j] = nm
                rowSum[i] -= nm
                colSum[j] -= nm
        return res
    # def restoreMatrix(self, rowSum: List[int], colSum: List[int]) -> List[List[int]]:
        