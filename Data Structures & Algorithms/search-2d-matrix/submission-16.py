class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1

        while top <= bot:
            mid = top + (bot - top) // 2

            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break

        target_row = top + (bot - top) // 2
        l, r = 0, COLS - 1

        while l <= r:
            mid = l + (r - l) // 2

            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        return False