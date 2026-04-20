class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = {i: set() for i in range(9)}
        columns = {i: set() for i in range(9)}
        squares = {i: set() for i in range(9)}

        for i in range(9):
            for j in range(9):
                value = board[i][j]
                if value == '.':
                    continue
                square_index = (i // 3) * 3 + (j // 3)
                if value in rows[i] or value in columns[j] or value in squares[square_index]:
                    return False
                rows[i].add(value)
                columns[j].add(value)
                squares[square_index].add(value)

        return True
        