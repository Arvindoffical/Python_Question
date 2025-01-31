#User function Template for python3
class Solution:
    def is_safe(self, mat, row, col, num):
        for x in range(9):
            if mat[row][x] == num or mat[x][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if mat[start_row + i][start_col + j] == num:
                    return False
        return True
    def find_empty_location(self, mat):
        for i in range(9):
            for j in range(9):
                if mat[i][j] == 0:
                    return i, j  
        return None  
    def solve_sudoku(self, mat):
        empty = self.find_empty_location(mat)
        if not empty:
            return True  
        row, col = empty
        for num in range(1, 10):  
            if self.is_safe(mat, row, col, num):
                mat[row][col] = num
                if self.solve_sudoku(mat):  
                    return True  
                mat[row][col] = 0  
        return False  
    def solveSudoku(self, mat):
        self.solve_sudoku(mat)
    def print_sudoku(self, mat):
        for row in mat:
            print(" ".join(map(str, row)))
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    import sys
    input = sys.stdin.read
    data = input().split()

    t = int(data[0])
    index = 1

    for _ in range(t):
        matrix = []
        n = 9
        for i in range(n):
            row = list(map(int, data[index:index + n]))
            matrix.append(row)
            index += n
        obj = Solution()
        obj.solveSudoku(matrix)
        for i in range(n):
            for j in range(n):
                print(matrix[i][j], end=" ")
            print()
        print("~")

# } Driver Code Ends