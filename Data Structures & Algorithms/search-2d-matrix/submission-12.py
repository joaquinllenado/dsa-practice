class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        top, bottom = 0, len(matrix) - 1

        while top <= bottom:
            mid = bottom + ((top - bottom) // 2)

            if matrix[mid][0] > target:
                bottom = mid - 1
            elif matrix[mid][-1] < target:
                top = mid + 1
            else:
                break
        
        target_row = bottom + ((top - bottom) // 2)

        left, right = 0, len(matrix[target_row]) - 1

        while left <= right:
            mid = left + ((right - left) // 2)

            if matrix[target_row][mid] == target:
                return True
            elif matrix[target_row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False