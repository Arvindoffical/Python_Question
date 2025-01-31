
class Solution:
    def countDistinct(self, arr, k):
        start = 0
        end = 0
        n = len(arr)
        mp = {}
        res = []
        while end < n:
            mp[arr[end]] = mp.get(arr[end], 0) + 1
            if ((end - start) + 1) == k:
                res.append(len(mp.keys()))
                mp[arr[start]] -= 1
                if mp[arr[start]] <= 0:
                    del mp[arr[start]]
                start += 1
            end += 1
        return res
#{ 
 # Driver Code Starts
import sys
from collections import defaultdict
if __name__ == '__main__':
    input = sys.stdin.read
    data = input().splitlines()
    t = int(data[0])
    index = 1
    while t > 0:
        arr = list(map(int, data[index].strip().split()))
        index += 1
        k = int(data[index])
        index += 1

        ob = Solution()
        res = ob.countDistinct(arr, k)

        for element in res:
            print(element, end=" ")
        print()
        print("~")

        t -= 1

# } Driver Code Ends