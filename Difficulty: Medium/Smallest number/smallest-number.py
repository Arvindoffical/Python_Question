#{ 
 # Driver Code Starts
#Initial Template for Python 3

# } Driver Code Ends
#User function Template for python3
class Solution:
    def smallestNumber(self, s, d):
        if (d*9) < s:
            return -1
        ans = ""
        for i in range(d-1,-1,-1):
            if s > 9:
                ans = '9' + ans
                s-=9
            else:
                if i==0:
                    ans = str(s) + ans
                else:
                    ans = str(s-1) + ans
                    i-=1
                    while i > 0:
                        ans ='0' + ans
                        i-=1
                    ans = '1' + ans
                    break
        return ans
        


#{ 
 # Driver Code Starts.
# Position this line where user code will be pasted.

import sys
import math
input = sys.stdin.read
data = input().split()

t = int(data[0])
index = 1

for _ in range(t):
    s = int(data[index])
    d = int(data[index + 1])
    index += 2
    ob = Solution()
    print(ob.smallestNumber(s, d))

# } Driver Code Ends