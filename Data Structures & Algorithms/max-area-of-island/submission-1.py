class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        visited = set()
        maxarea = 0
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]

        def bfs(row,col): #idx is the idx of the current 1
            currarea = 0    
            queue = deque([(row, col)])
            while queue:
                currcom = queue.popleft()
                ro, co = currcom[0], currcom[1]
                if grid[ro][co] == 1:
                    grid[ro][co] = 0
                    currarea += 1
                    for direct in directions:
                        nrow = ro + direct[0]
                        ncol = co + direct[1]
                        if nrow < len(grid) and nrow >= 0 and ncol < len(grid[0]) and ncol >= 0:
                            if grid[nrow][ncol] == 1:
                                queue.append((nrow, ncol))
            return currarea

        for ridx, row in enumerate(grid):
            for cidx, col in enumerate(row):
                if col == 1:
                    narea = bfs(ridx, cidx)
                    if narea > maxarea:
                        maxarea = narea

        return maxarea
