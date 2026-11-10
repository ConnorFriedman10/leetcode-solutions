class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return
        m, n = len(board), len(board[0])

        def mark_safe(r, c):
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if 0 <= x < m and 0 <= y < n and board[x][y] == 'O':
                    board[x][y] = 'S'
                    stack.extend([(x+1, y), (x-1, y), (x, y+1), (x, y-1)])

        for i in range(m):
            mark_safe(i, 0)
            mark_safe(i, n - 1)
        for j in range(n):
            mark_safe(0, j)
            mark_safe(m - 1, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 'S':
                    board[i][j] = 'O'