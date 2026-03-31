class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = top + ((bottom - top) // 2)

            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bottom = mid - 1
            else:
                break
        
        if not top <= bottom:
            return False
        row = top + ((bottom - top) // 2)
        l, r = 0, len(matrix[row]) - 1

        while l <= r:
            m = l + ((r - l) // 2)

            if matrix[row][m] == target:
                return True
            elif matrix[row][m] < target:
                l = m + 1
            else:
                r = m - 1
        
        return False