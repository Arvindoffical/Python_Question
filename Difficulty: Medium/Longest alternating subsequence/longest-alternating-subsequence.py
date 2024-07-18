#User function Template for python3
class Solution:
    # Function to find the maximum length of alternating subsequence
    # def alternatingMaxLength(self, arr):
       #code here
    def alternatingMaxLength(self, arr):        
        if len(arr) < 2: return 1        

        temp = arr[0]        
        ans = 0        
        findGreater = None
        
        for i in range(1, len(arr)):
            if temp == arr[i]:
                continue
            if findGreater == None:
                ans += 1
                findGreater = not (arr[i] > temp)
            if (findGreater and arr[i]>temp) or ((not findGreater) and (arr[i] < temp)):
                temp = arr[i]
                ans += 1
                findGreater = not findGreater
            else:
                if findGreater:
                    temp = min(temp, arr[i])
                else:
                    temp = max(temp, arr[i])                
        
        return ans + 1

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    tc = int(data[0])
    for i in range(1, tc + 1):
        s = data[i].strip().split()
        nums = list(map(int, s))
        obj = Solution()
        ans = obj.alternatingMaxLength(nums)
        print(ans)

# } Driver Code Ends