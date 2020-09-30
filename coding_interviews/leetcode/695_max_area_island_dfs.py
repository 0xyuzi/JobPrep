ISLAND = 1
DIRECTIONS = [(-1,0), (0,1), (1,0), (0,-1)]
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # dfs method 
        if not grid or len(grid[0])==0:
            return 0
        
        row_num, col_num = len(grid), len(grid[0])
        
        visited = set()
        
        max_area = 0
        
        for i in range(row_num):
            for j in range(col_num):
                if grid[i][j] == ISLAND and (i,j) not in visited:
                    print(f"go to {i,j}")
                    
                    island_area = self.dfs(i,j,grid,visited)
                    print(island_area)
                    if  max_area < island_area:
                        max_area = island_area
        
        return max_area
    
    
    def dfs(self, x,y, grid, visited):
        
        if x<0 or x>= len(grid) or y<0 or y >=len(grid[0]):
            return 0
        
        if (x,y) in visited or grid[x][y] != ISLAND:
            return 0
        
        visited.add((x,y))
       
        
        num_island_subbranch = 1
        for dx, dy in DIRECTIONS:
            num_island_subbranch += self.dfs(x + dx, y+dy, grid, visited)
            # print(self.dfs(x + dx, y+dy, grid, visited))
           # 1 print(num_island_subbranch)
            
        return num_island_subbranch
       