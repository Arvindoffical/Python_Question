#User function Template for python3

class Solution:
    def sum_of_middle_elements(self, arr1, arr2):
        n = len(arr1)
        
        if n == 1:
            return arr1[0] + arr2[0]
        
        low, high = 0, n
        
        while low <= high:
            i = (low + high) // 2
            j = n - i
            
            left1 = arr1[i-1] if i > 0 else float('-inf')
            left2 = arr2[j-1] if j > 0 else float('-inf')
            right1 = arr1[i] if i < n else float('inf')
            right2 = arr2[j] if j < n else float('inf')
            
            if left1 <= right2 and left2 <= right1:
                return max(left1, left2) + min(right1, right2)
            elif left1 > right2:
                high = i - 1
            else:
                low = i + 1

#{ 
 # Driver Code Starts
#Initial Template for Python 3

import sys

input = sys.stdin.read


def main():
    input_lines = input().strip().split("\n")
    t = int(input_lines[0])

    index = 1
    results = []
    while t > 0:
        arr = list(map(int, input_lines[index].strip().split()))
        brr = list(map(int, input_lines[index + 1].strip().split()))
        index += 2

        solution = Solution()
        res = solution.sum_of_middle_elements(arr, brr)
        results.append(res)

        t -= 1

    for result in results:
        print(result)


if __name__ == "__main__":
    main()

# } Driver Code Ends