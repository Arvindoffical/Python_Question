
class Solution:
    def subarrayXor(self, arr, k):
        count = 0
        xor = 0
        freq = {}
        
        for num in arr:
            xor ^= num
            
            # If the current XOR is equal to k, increment count
            if xor == k:
                count += 1
            
            # Calculate the value to check if a subarray with XOR k exists
            target = xor ^ k
            
            # If target is in the map, add its frequency to count
            if target in freq:
                count += freq[target]
            
            # Store the frequency of the current XOR
            if xor in freq:
                freq[xor] += 1
            else:
                freq[xor] = 1
        
        return count
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    tc = int(input())

    for _ in range(tc):
        arr = list(map(int, input().split()))
        k = int(input())

        obj = Solution()
        print(obj.subarrayXor(arr, k))
        print("~")

# } Driver Code Ends