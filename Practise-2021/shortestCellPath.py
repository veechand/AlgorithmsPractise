import sys

def shortestCellPath(grid, sr, sc, tr, tc):
	"""
	@param grid: int[][]
	@param sr: int
	@param sc: int
	@param tr: int
	@param tc: int
	@return: int
	"""
	value = 0
	result_grid = [[sys.maxint for i in range(len(grid[0]))] for j in range(len(grid))]
	findShortestCellPath(value,result_grid,sr,sc,tr,tc,grid,[])
	return result_grid[tr][tc] if result_grid[tr][tc] != sys.maxint else -1 

def findShortestCellPath(value,result_grid,sr,sc,tr,tc,grid,path):
	if sr < 0 or sc < 0 or tr < 0 or tc < 0 or sr >= len(grid) or sc >= len(grid[0]) or tr >= len(grid) or tc >= len(grid[0]):
		return
	if ((sr, sc) in path) or grid[sr][sc] == 0:
		return
	# print(sr,sc)
	"""
	This is one mistake forgotten to add the path
	"""
	path.append((sr,sc)) 

	if value < result_grid[sr][sc]:
		result_grid[sr][sc] = value
		if (sr, sc) != (tr, tc):
			findShortestCellPath(value+1,result_grid,sr+1,sc,tr,tc,grid,path)
			findShortestCellPath(value+1,result_grid,sr-1,sc,tr,tc,grid,path)
			findShortestCellPath(value+1,result_grid,sr,sc+1,tr,tc,grid,path)
			findShortestCellPath(value+1,result_grid,sr,sc-1,tr,tc,grid,path)

grid = [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]
sr = 0
sc = 2
tr = 2
tc = 2
print(shortestCellPath(grid, sr, sc, tr, tc))
