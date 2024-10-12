class Solution:
    def minGroups(self, inter):
        inter.sort()

        pq = []

        for l, r in inter:
            if not pq:
                heapq.heappush(pq, r)
            else:
                if pq[0] >= l:
                    heapq.heappush(pq, r)
                else:
                    heapq.heappop(pq)
                    heapq.heappush(pq, r)

        return len(pq)