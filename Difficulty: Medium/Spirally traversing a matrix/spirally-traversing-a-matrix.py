class Solution:
    def spirallyTraverse(self, matrix):
        row = len(matrix)
        column = len(matrix[0])
        len_a = row*column
        ans = []
        if row/2>row//2:
            temp = row//2+1
        else:
            temp = row//2
        for p in range(temp):
            start= p
            for i in range(4):
                if i==0:
                    for j in range(start,column-start):
                        if len(ans) == len_a:
                            break
                        ans.append(matrix[start][j]) 
                if i==1 :
                    for j in range(start+1,row-start):
                        if len(ans) == len_a:
                            break
                        ans.append(matrix[j][column-1-start])
                if i==2 :
                    for j in range(start+1,column-start):
                        if len(ans) == len_a:
                            break
                        ans.append(matrix[row-1-start][column-1-j])
                if i==3:
                    for j in range(start+1,row-1-start):
                        if len(ans) == len_a:
                            break
                        ans.append(matrix[row-1-j][start])
        return ans
        
#{ 
 # Driver Code Starts
if __name__ == "__main__":
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1
    for _ in range(t):
        r = int(data[index])
        c = int(data[index + 1])
        index += 2
        matrix = []
        for i in range(r):
            row = list(map(int, data[index:index + c]))
            matrix.append(row)
            index += c

        solution = Solution()
        result = solution.spirallyTraverse(matrix)
        print(" ".join(map(str, result)))

# } Driver Code Ends