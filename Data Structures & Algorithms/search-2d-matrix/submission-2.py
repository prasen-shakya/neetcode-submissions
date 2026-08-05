class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix) - 1

        for i in range(len(matrix) - 1, -1, -1):
            if matrix[i][0] <= target:
                row = i
                break
        
        l = 0
        r = len(matrix[row]) - 1

        print(l, r)


        while l <= r:
            mid = (l  + r) // 2
            if matrix[row][mid] < target:
                l = mid + 1
            elif matrix[row][mid] > target:
                r = mid - 1
            else:
                return True


        return False 