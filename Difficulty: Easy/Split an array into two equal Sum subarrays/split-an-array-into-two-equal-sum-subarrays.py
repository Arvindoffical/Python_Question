class Solution:
    def canSplit(self, arr):
        #code here
        sum1=0
        sum2=sum(arr)
        for i in arr:
            sum1+=i
            sum2-=i
            if sum1==sum2:
                return True
        return False
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().splitlines()

    t = int(data[0])
    index = 1
    for _ in range(t):
        arr = list(map(int, data[index].split()))
        index += 1

        obj = Solution()
        res = obj.canSplit(arr)
        if (res):
            print("true")
        else:
            print("false")

# } Driver Code Ends