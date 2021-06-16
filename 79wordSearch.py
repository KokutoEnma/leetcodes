class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        dfs, fast, need understand
        """
        def dfs(x, y, depth):
            if depth == len(word):
                return True

            if 0 <= x < len(board) and 0 <= y < len(board[0]) and board[x][y] == word[depth]:
                board[x][y], tmp = "", board[x][y]
                for dx, dy in ((-1, 0), (1, 0), (0, -1), (0, 1)):

                    if dfs(x+dx, y+dy, depth+1):
                        return True

                board[x][y] = tmp

        counter = Counter(word)
        starts = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                counter[board[i][j]] -= 1
                if board[i][j] == word[0]:
                    starts.append((i, j))

        if max(counter.values()) > 0:
            return False

        for i, j in starts:
            if dfs(i, j, 0):
                return True

        return False

        """
        backtracking, slow, need optimize
        """
#         currs =set()
#         for i in range(len(board)):
#             for j in range(len(board[i])):
#                 if board[i][j]==word[0]:
#                     currs.add((i,j))

#         if len(currs)<1: return False

#         for curr in currs:
#             if self.bk(board, word[1:], [curr], curr):
#                 return True


#         return False

    def bk(self, board, word, visited, curr):

        if len(word) < 1:
            return True

        i, j = curr
        neighbors = [(i, j) for i, j in [(i, j+1), (i, j-1), (i-1, j), (i+1, j)] if i >=
                     0 and j >= 0 and i < len(board) and j < len(board[0]) and (i, j) not in set(visited)]

        # print(curr, neighbors, word[0], visited)

        for n_i, n_j in neighbors:
            if board[n_i][n_j] == word[0]:

                if self.bk(board, word[1:], visited+[(n_i, n_j)], (n_i, n_j)):
                    return True

        return False
