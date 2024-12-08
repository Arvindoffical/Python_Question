class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Step 1: Sort events by their end times
        events.sort(key=lambda x: x[1])

        # Step 2: Create a running max array
        n = len(events)
        maxValues = [0] * n
        maxValues[0] = events[0][2]

        for i in range(1, n):
            maxValues[i] = max(maxValues[i - 1], events[i][2])

        maxSum = 0

        # Step 3: Iterate through the events and use binary search
        for i in range(n):
            start, value = events[i][0], events[i][2]
            idx = self.binarySearch(events, start - 1)

            currentSum = value
            if idx != -1:
                currentSum += maxValues[idx]

            maxSum = max(maxSum, currentSum)

        return maxSum

    def binarySearch(self, events, targetEnd):
        start, end = 0, len(events) - 1
        res = -1

        while start <= end:
            mid = start + (end - start) // 2
            if events[mid][1] <= targetEnd:
                res = mid
                start = mid + 1
            else:
                end = mid - 1

        return res