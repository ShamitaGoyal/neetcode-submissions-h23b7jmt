class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        row = [ set() for _ in range(9)]
        col = [set() for _ in range(9)]
        boxes = {}

        for i in range(9):
            for j in range(9):

                val = board[i][j]

                #1) check for empty vals 
                if val == ".":
                    continue 
                
                #2) check for row
                if val in row[i]:
                    return False
                row[i].add(val)

                #3) check in col
                if val in col[j]:
                    return False
                col[j].add(val)

                #4) check in boxes

                box = (i // 3, j // 3)
                if box not in boxes:
                    boxes[box] = set()
                if val in boxes[box]:
                    return False
                boxes[box].add(val)
        return True

        