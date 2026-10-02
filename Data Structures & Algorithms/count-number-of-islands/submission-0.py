class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        res = 0

        def dfs(row, col):
            # Bounds check
            if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]):
                return
            
            if grid[row][col] == '0':
                return

            grid[row][col] = '0'

            # Traverse 
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)


        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '0':
                    continue
                
                dfs(row, col)
                res += 1
        
        return res