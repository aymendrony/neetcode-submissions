class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        dictLigne = defaultdict(list)
        dictCol = defaultdict(list)
        dictCarre = defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != ".":
                    if board[i][j] not in dictLigne[i]:
                        dictLigne[i].append(board[i][j])
                    else:
                        return False
                    if board[i][j] not in dictCol[j]:
                        dictCol[j].append(board[i][j])
                    else:
                        return False 
                    if board[i][j] not in dictCarre[(i//3, j//3)]:
                        dictCarre[(i//3, j//3)].append(board[i][j])
                    else:
                        return False

        return True