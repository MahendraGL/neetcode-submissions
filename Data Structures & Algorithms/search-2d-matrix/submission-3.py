class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        l = 0
        r = (row * col)-1

        while l<=r:
            m = (l+r) // 2

            i = m // col
            j = m % col

            mid = matrix[i][j]

            if target == mid:
                return True
            elif target < mid:
                r = m - 1
            else:
                l = m + 1
        return False


        