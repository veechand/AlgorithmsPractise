class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        current_cell = [0,0]
        answers = []
        current_path = [0,0]
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        self.get_paths(current_cell, answers, current_path, m, n, obstacleGrid)
        return len(answers)
    """
    current_cell = [m',n'] - Where m' and n' shows the row and column number
    answers = [current_paths] - [[current_path[],[current_cell]][[],[]]]
    current_path = [current_cell] - List of cells
    """
    def get_paths(self, current_cell, answers, current_path, m, n, obstacles):
        if self.is_solution(current_cell, m, n):
            answers.append(current_path)
        else:
            all_possible_paths = self.get_all_possible_paths(current_cell, m, n, obstacles) #[[cells]]
            for path in all_possible_paths:
                current_path.append(path)
                self.get_paths(path, answers, current_path, m, n,obstacles)
                current_path.pop(-1)
    
    def get_all_possible_paths(self,current_cell, m, n, obstacles):
        result = []
        proposed_cells = [
            [current_cell[0] + 1, current_cell[1]], 
            [current_cell[0], current_cell[1] + 1]
        ]
        for proposed_cell in proposed_cells:
            if self.is_with_in_grid(proposed_cell, m, n) and self.is_not_obstacle(proposed_cell, obstacles):
                result.append(proposed_cell)
        return result
    
    def is_with_in_grid(self, cell, m, n):
        return (cell[0] < m and cell[1] < n)
    
    def is_not_obstacle(self, cell, obstacles):
        return obstacles[cell[0]][cell[1]] == 0
    
    def is_solution(self, cell, m, n):
        return cell[0] == m - 1 and cell[1] == n - 1