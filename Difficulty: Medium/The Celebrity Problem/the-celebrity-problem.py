
class Solution:
    def celebrity(self, mat):
        m=len(mat)
        sta=0
        sto=m-1
        while sta<sto:
            if mat[sta][sto]==1:
                sta+=1
            else:
                sto-=1
        for ix in range(m):
            if ix==sto:
                continue
            if mat[ix][sto]!=1 or mat[sto][ix]!=0:
                return -1
        return sto

#{ 
 # Driver Code Starts
# Main function to handle input and output
if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        M = []
        for _ in range(n):
            M.append(list(map(int, input().split())))

        ob = Solution()
        print(ob.celebrity(M))

# } Driver Code Ends