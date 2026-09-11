class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        #go through the grid, find all of the rotten bananas
        directions = ((1, 0), (0, 1), (-1, 0), (0, -1))
        rottenset = deque([])
        cleanset = set()
        time = -1

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    rottenset.append((row, col))
                if grid[row][col] == 1:
                    cleanset.add((row, col))
        
        if not cleanset and not rottenset:
            return 0
        
        while rottenset:
            time += 1
            for i in range(len(rottenset)):
                crow, ccol = rottenset.popleft()
                for di in directions:
                    nrow = crow + di[0]
                    ncol = ccol + di[1]
                    if nrow >= 0 and nrow < len(grid) and ncol >= 0 and ncol < len(grid[0]):
                        if grid[nrow][ncol] == 1:
                            grid[nrow][ncol] = 2
                            cleanset.remove((nrow, ncol))
                            rottenset.append((nrow, ncol))
        
        if cleanset:
            return -1
        return time

        #then using bfs, cover each banana going rotten one by one

        #then if there's still an unrotten banana at the end of this 
        #process return -1, else return the # of minutes