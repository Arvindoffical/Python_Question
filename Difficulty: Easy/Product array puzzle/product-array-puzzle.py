#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        p=1
        zero=0
        
        for i in nums:
            if i==0:
                zero+=1
                continue
            p*=i
        
        for i in range(0,len(nums)):
            
            if zero==0:
                
                nums[i]= (p//nums[i])
                
            elif zero==1:
                
                if nums[i]==0:
                    nums[i]=p
                else:
                    nums[i]=0
            else:
                
                nums[i]=0
                
        return nums

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())
        arr = [int(x) for x in input().split()]

        ans = Solution().productExceptSelf(arr)
        print(*ans)

# } Driver Code Ends