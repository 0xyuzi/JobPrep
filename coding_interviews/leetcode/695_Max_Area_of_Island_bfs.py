from collections import deque 

ISLAND = 1
DIRECTIONS = [(-1,0), (0,1), (1,0), (0,-1)]

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    # bfs method not dfs
        if not grid or len(grid[0]) == 0:
            return 0
        
        row_num, col_num = len(grid), len(grid[0])
        visited = set()
        
        max_area = 0
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == ISLAND and grid[i][j] not in visited:
                    visited.add((i,j))
                    island_area = self.bfs(i,j, grid, visited)
                    
                    if max_area < island_area:
                        max_area = island_area
        return max_area
    
    def bfs(self, row, col, grid, visited):
        island_area = 1
        queue = deque([])
        queue.append((row,col))
        
        while queue:
            x, y = queue.popleft()
            
            for dx, dy in DIRECTIONS:
                next_x = x + dx
                next_y = y + dy
                
                if self.is_island(next_x, next_y, grid, visited):
                    queue.append((next_x, next_y))
                    visited.add((next_x, next_y))
                    island_area += 1
        
        return island_area
    
    def is_island(self,x,y,grid,visited):
        row_num, col_num = len(grid), len(grid[0])
        
        if x < 0 or x>= row_num or y< 0 or y>= col_num:
            return False 
        
        if grid[x][y] != ISLAND or (x,y) in visited:
            return False
        
        return True