
class Solution:
    def countTriplets(self, arr, target):
        # code here
        n = len(arr)
        cnt = 0
        
        for i in range(n):
            l, r = i+1, n-1
            
            while l < r:
                s = arr[i] + arr[l] + arr[r]
                
                if s > target:
                    r -= 1
                
                elif s < target:
                    l += 1
                    
                else:
                    left = arr[l]
                    right = arr[r]
                    cl = cr = 0
                    
                    while l<=r and arr[l]==left:
                        l += 1
                        cl += 1
                        
                    while l<=r and arr[r]==right:
                        r -= 1
                        cr += 1
                        
                    if left == right:
                        cnt += (cl * (cl-1)) //2
                    else:
                        cnt += cl*cr
        
        return cnt

#{ 
 # Driver Code Starts
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        arr = list(map(int, input().split()))
        target = int(input())
        ob = Solution()
        ans = ob.countTriplets(arr, target)
        print(ans)
        print("~")
# } Driver Code Ends