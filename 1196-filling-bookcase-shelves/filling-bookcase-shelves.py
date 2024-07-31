class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        n = len(books)
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(n):
            w, h = 0, 0
            # every i represents the most minimized height configuration in books[:i]
            # from this configuration, we want to see how we can fit books in the next row down
            for j in range(i, n): # iterate through i -> n
                w += books[j][0]
                h = max(h, books[j][1])
                # dp[j+1] represents adding the jth book to the next row if it fits

                if w > shelfWidth: 
                    break
                # minimum of configurtaion precomputed and adding it to the next row
                dp[j+1] = min(dp[j+1], dp[i] + h)
        return dp[n]
                    