class Solution(object):
    def countUnguarded(self, m, n, guards, walls):
  
        # Initialize the grid
        grid = [['' for _ in range(n)] for _ in range(m)]

        # Mark guards on the grid
        for x, y in guards:
            grid[x][y] = 'G'

        # Mark walls on the grid
        for x, y in walls:
            grid[x][y] = 'W'

        # Mark cells guarded by each guard
        for x, y in guards:
            # Right direction
            for j in range(y + 1, n):
                if grid[x][j] in ('W', 'G'):
                    break
                grid[x][j] = 'C'

            # Left direction
            for j in range(y - 1, -1, -1):
                if grid[x][j] in ('W', 'G'):
                    break
                grid[x][j] = 'C'

            # Down direction
            for i in range(x + 1, m):
                if grid[i][y] in ('W', 'G'):
                    break
                grid[i][y] = 'C'

            # Up direction
            for i in range(x - 1, -1, -1):
                if grid[i][y] in ('W', 'G'):
                    break
                grid[i][y] = 'C'

        # Count unguarded cells
        unguarded = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '':  # Unoccupied and unguarded
                    unguarded += 1

        return unguarded

        