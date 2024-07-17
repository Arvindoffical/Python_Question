#User function Template for python3

class Solution:
    #Complete this function
    # Function for finding maximum AND value.
    def maxAND(self,arr, N):
    # Initialize result to 0
        result = 0
        for bit in range(31, -1, -1):
            temp_result = result | (1 << bit)
            count = 0
            for num in arr:
                if (num & temp_result) == temp_result:
                    count += 1
            if count >= 2:
                result = temp_result
        
        return result



#{ 
 # Driver Code Starts
#Initial Template for Python 3

import math


def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        arr=[int(x) for x in input().strip().split()]
        obj = Solution()
        print(obj.maxAND(arr,n))
        T-=1

if __name__=="__main__":
    main()
# } Driver Code Ends