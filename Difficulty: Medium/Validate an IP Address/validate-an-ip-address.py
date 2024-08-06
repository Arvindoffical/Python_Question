#User function Template for python3
class Solution:
    def isValid(self, strr):
        #code here
        strr=strr.split('.')
        if '' in strr:
            strr=[x for x in strr if x !='']
        if len(strr)!=4:
            return False
        for i in strr:
            if int(i)<=255 and int(i)>=0 and len(i)==len(str(int(i))):
                continue
            else:
                return False
        return True        #code here



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == "__main__":
    t = int(input())
    for _ in range(0, t):
        s = input()
        ob = Solution()
        if (ob.isValid(s)):
            print("true")
        else:
            print("false")

# } Driver Code Ends