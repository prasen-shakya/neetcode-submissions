class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])

        # Find the right row 

        t, b = 0, ROWS - 1

        while t <= b:
            mid = (t + b) // 2

            if matrix[mid][-1] < target:
                t = mid + 1
            elif matrix[mid][0] > target:
                b = mid - 1
            else:
                break
        
        row = (t + b) // 2

        l, r = 0, COLS - 1

        while l <= r:
            mid = (l + r) // 2

            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True
        
        return False
