class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        perimeter = 0
        for i, row in enumerate(grid):
        	for j, tile in enumerate(row):
        		
        		n = 0		
        		if tile == 1:
	        		n = 4
	        		#check left
	        		if j-1 >= 0 and row[j-1] == 1:
	        			n-= 1
	        		
	        		#check right
	        		if j+1 < len(row) and row[j+1] == 1:
	        			n-= 1

	        		#check up
	        		if i-1 >= 0 and grid[i-1][j] == 1:
	        			n-= 1

	        		#check down
	        		if i+1 < len(grid) and grid[i+1][j] == 1:
	        			n-= 1

        		perimeter+=n  

        return perimeter		

if __name__ == "__main__":
	s = Solution()
	grid = [[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]]
	ans = s.islandPerimeter(grid)
	print(ans)