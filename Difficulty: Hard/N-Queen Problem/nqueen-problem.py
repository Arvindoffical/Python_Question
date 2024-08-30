#User function Template for python3

class Solution:
    def nQueen(self, n):
        # code here
        def backtrack(row):
            # If all n queens are placed, append the solution
            if row == n:
                results.append(cols[:])
                return
            
            for col in range(1, n + 1):
                if col in cols or (row - col) in diag1 or (row + col) in diag2:
                    continue
                
                # Place the queen
                cols.append(col)
                diag1.add(row - col)
                diag2.add(row + col)
                
                # Move to the next row
                backtrack(row + 1)
                
                # Backtrack: remove the queen
                cols.pop()
                diag1.remove(row - col)
                diag2.remove(row + col)
        
        results = []  # To store all valid configurations
        cols = []     # Column positions of queens for each row
        diag1 = set() # Main diagonal constraints
        diag2 = set() # Anti-diagonal constraints
        backtrack(0)  # Start backtracking from the first row
        return results

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        
        ob = Solution()
        ans = ob.nQueen(n)
        if(len(ans) == 0):
            print("-1")
        else:
            for i in range(len(ans)):
                print("[",end="")
                for j in range(len(ans[i])):
                    print(ans[i][j],end = " ")
                print("]",end = " ")
            print()
                
# } Driver Code Ends