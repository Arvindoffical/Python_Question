#User function Template for python3

class Solution:
    def countSubarrays(self, arr, k):
        # code here
 # Dictionary to store prefix sums frequencies
        prefixSums = {}
        res = 0
        currSum = 0
    
        for val in arr:
            # Add current element to sum so far
            currSum += val
    
            # If currSum is equal to desired sum, then a new subarray is found
            if currSum == k:
                res += 1
    
            # Check if the difference exists in the prefixSums dictionary
            if currSum - k in prefixSums:
                res += prefixSums[currSum - k]
    
            # Add currSum to the dictionary of prefix sums
            prefixSums[currSum] = prefixSums.get(currSum, 0) + 1
    
        return res


#{ 
 # Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
from collections import deque

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER


@atexit.register
def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())


if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        k = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        res = ob.countSubarrays(arr, k)
        print(res)
        print("~")

# } Driver Code Ends