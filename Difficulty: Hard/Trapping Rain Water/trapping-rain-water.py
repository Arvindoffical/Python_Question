

class Solution:
    def maxWater(self, arr):
        c=1
        r=len(arr)-2
        k=arr[c-1]
        j=arr[r+1]
        ans=0
        while c<=r:
            if j<=k:
                ans+=max(0,j-arr[r])
                j=max(j,arr[r])
                r-=1
            else:
                ans+=max(0,k-arr[c])
                k=max(k,arr[c])
                c+=1
        return ans
        # code here

#{ 
 # Driver Code Starts
#Initial template for Python 3

import math


def main():
    t = int(input())
    while (t > 0):

        arr = [int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxWater(arr))

        t -= 1
        print("~")


if __name__ == "__main__":
    main()

# } Driver Code Ends