class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bot = 0, len(matrix) - 1

        while top <= bot:
            mid = top + ((bot - top) // 2)
            if matrix[mid][0] > target:
                bot = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        
        targetRow = top + ((bot - top) // 2)
        l, r = 0, len(matrix[targetRow]) - 1

        while l <= r:
            m = l + ((r - l) // 2)
            if matrix[targetRow][m] == target:
                return True
            elif matrix[targetRow][m] < target:
                l = m + 1
            else:
                r = m - 1
        return False