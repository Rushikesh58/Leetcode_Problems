class Solution:
    def exist(self, board, word):
        ROWS , COLS = len(board) , len(board[0])
        path = set()

        def dfs(r,c,i):
            if i == len(word):
                return True
            if (r<0 or c<0 or r>= ROWS or c>=COLS or
                word[i]!= board[r][c] or 
                (r,c) in path):
                return False

            path.add((r,c))
            res = (dfs(r+1,c,i+1) or
                    dfs(r-1,c,i+1) or
                    dfs(r,c+1,i+1) or
                    dfs(r,c-1,i+1))
            
            path.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False

if __name__ == "__main__":
    sol = Solution()
    board = [
            ["A","B","C","D"],
            ["S","A","A","T"],
            ["A","C","A","E"]
            ]
    word = "CAT"
    print(sol.exist(board,word))