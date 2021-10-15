    class Solution(object):
        possible_paths = [
            (-1, 0),
            (1, 0),
            (0, -1),
            (0, 1)
        ]
        def numIslands(self, grid):
            """
            :type grid: List[List[str]]
            :rtype: int
            """
            rows = len(grid)
            cols = len(grid[0])
            visited_grid = [[False for i in range(cols)] for j in range(rows)]
            start_pos = self.get_non_visited_land(visited_grid, grid, (0,0))
            total_islands = 0
            while( start_pos != None):
                # print("Starting pos", start_pos)
                self.mark_all_reachable_lands(visited_grid, grid, start_pos)
                # print("Starting pos", start_pos)
                total_islands += 1
                start_pos = self.get_non_visited_land(visited_grid, grid, start_pos)
            return total_islands
        
        def mark_all_reachable_lands(self, visited_grid, grid, start_pos):
            if start_pos[0] < 0 or start_pos[0] >= len(grid) or start_pos[1] < 0 or start_pos[1] >= len(grid[0]) or visited_grid[start_pos[0]][start_pos[1]] :
                return
            if(grid[start_pos[0]][start_pos[1]] == "1"):
                visited_grid[start_pos[0]][start_pos[1]] = True   
                for next_pos in self.possible_paths:
                    next_loc = (start_pos[0] + next_pos[0], start_pos[1] + next_pos[1])
                    self.mark_all_reachable_lands(visited_grid, grid, next_loc)

        def get_non_visited_land(self, visited_grid, grid, start_pos):
            # print("Starting pos in non_visisted", start_pos)
            for i in range(len(grid)):
                for j in range(len(grid[0])): # +1 has to be added
                    # print (i,j)
                    # print(grid[i][j])
                    # print(visited_grid[i][j])
                    if grid[i][j] == "1" and not visited_grid[i][j]:
                        # print("Returning ",i,j)
                        return (i,j)
            return None

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
grid3 = [
    ["0","1","0"],
    ["1","0","1"],
    ["0","1","0"]
]
solution = Solution()
print(solution.numIslands(grid1) == 1)
print(solution.numIslands(grid2) == 3)
print(solution.numIslands(grid3) == 4)