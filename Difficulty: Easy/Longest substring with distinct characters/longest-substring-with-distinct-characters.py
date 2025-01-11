#User function Template for python3

class Solution:
    def longestUniqueSubstr(self, arr):
        # code here
        i = 0
        j = 0
        mp = {}
        n = len(arr)
        answer = 0
        while j < n :
            mp[arr[j]] = mp.get(arr[j], 0) + 1
            if mp[arr[j]] == 1 :
                answer = max(answer, j-i+1)
            else :
                while(i < n and mp[arr[j]] > 1) :
                    mp[arr[i]] -= 1
                    if mp[arr[i]] == 0 :
                        del mp[arr[i]]
                    i += 1
                answer = max(answer, j-i+1)
            j += 1
        return answer

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        s = input()

        solObj = Solution()

        ans = solObj.longestUniqueSubstr(s)

        print(ans)

        print("~")
# } Driver Code Ends