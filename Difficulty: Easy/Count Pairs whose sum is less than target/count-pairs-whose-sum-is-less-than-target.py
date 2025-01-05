#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


# } Driver Code Ends
#User function Template for python3
class Solution:
    #Complete the below function
    def countPairs(self, arr, target):
        #Your code here
        arr.sort()
        cnt = 0
        l,r = 0,len(arr)-1
        while l<r:
            summ = arr[l]+arr[r]
            if summ >=target:
                r-=1
            else:
                cnt+= (r-l)
                l+=1
        return cnt

#{ 
 # Driver Code Starts.

def main():
    T = int(input())
    while (T > 0):

        A = [int(x) for x in input().strip().split()]

        k = int(input())
        ob = Solution()
        print(ob.countPairs(A, k))
        print('~')
        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends