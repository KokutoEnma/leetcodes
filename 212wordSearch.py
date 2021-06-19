import copy


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        self.board = board

        return [word for word in words if self.findWord(word)]

    def findWord(self, word):

        temp_board = copy.deepcopy(self.board)

        def dfs(word_ind, x, y):
            if word_ind >= len(word):
                return True

            if 0 <= x < len(temp_board) and 0 <= y < len(temp_board[0]) and temp_board[x][y] == word[word_ind]:
                temp, temp_board[x][y] = temp_board[x][y], ""
                for dx, dy in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    if dfs(word_ind+1, x+dx, y+dy):
                        return True

                temp_board[x][y] = temp

        counter = Counter(word)
        store = {c: counter[c] for c in counter}

        starts = []
        for i in range(len(temp_board)):
            for j in range(len(temp_board[i])):
                if temp_board[i][j] in counter:
                    store[temp_board[i][j]] -= 1
                if temp_board[i][j] == word[0]:
                    starts.append((i, j))

        if max(store.values()) > 0:
            return False

        for i, j in starts:
            if dfs(0, i, j):
                return True

        return False
