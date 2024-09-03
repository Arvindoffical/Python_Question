#User function Template for python3
#User function Template for python3
from functools import lru_cache
class Solution:
    def minOperations(self, s1, s2):
        m=len(s1)
        n=len(s2)
        @lru_cache(None)
        def dp(a=m-1,b=n-1):
            nonlocal s1,s2
            if a<0 or b<0:
                return b+1 if a<0 else a+1
            mn=min(dp(a-1,b),dp(a,b-1))+1
            if s1[a]==s2[b]:
                mn=min(mn,dp(a-1,b-1))
            return mn
        return dp()

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    T = int(input())
    for i in range(T):
        s1, s2 = input().split()
        ob = Solution()
        ans = ob.minOperations(s1, s2)
        print(ans)

# } Driver Code Ends