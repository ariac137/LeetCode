class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        SIZE = 9
        blocks = [[[] for _ in range(3)] for _ in range(3)]
        for i in range(SIZE):
            rows = []
            cols = []
            for j in range(SIZE):
                # check rows
                if board[i][j] != ".":
                    num1 = int(board[i][j])
                    if not (1 <= num1 <= 9):
                        return False
                    if num1 in rows:
                        return False
                    rows.append(num1)
                    
                    # check blocks
                    block_row = i // 3 - 1
                    block_col = j // 3 - 1
                    if num1 in blocks[block_row][block_col]:
                        return False
                    blocks[block_row][block_col].append(num1)
                    
                # check cols
                if board[j][i] != ".":
                    num2 = int(board[j][i])
                    if not (1 <= num2 <= 9):
                        return False
                    if num2 in cols:
                        return False
                    cols.append(num2)

        return True     
                
