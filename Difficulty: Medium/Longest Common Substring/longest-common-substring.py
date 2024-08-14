#User function Template for python3

class Solution:
    def longestCommonSubstr(self, S1, S2):
        # code her
        n=len(S1)
        
        m=len(S2)
        
        dp=[[0]*(m+1)for i in range(n+1)]
        
        maxa=0
        
        for i in range(1,n+1):
            
            for j in range(1,m+1):
                
                if S1[i-1]==S2[j-1]:
                    
                    dp[i][j]=dp[i-1][j-1]+1
                    
                    maxa=max(maxa,dp[i][j])
                    
                else:
                    
                    dp[i][j]=0
                    
        return maxa

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        S1 = input().strip()
        S2 = input().strip()
        ob = Solution()
        print(ob.longestCommonSubstr(S1, S2))

# } Driver Code Ends