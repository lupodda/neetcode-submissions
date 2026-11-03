class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        n = len(matrix)
        m = len(matrix[0])
        self.matrix = matrix
        self.matrix_sum = [[0]*(m+1) for _ in range(n+1)]

        for r in range(1,n+1):
            for c in range(1,m+1):
                self.matrix_sum[r][c] = matrix[r-1][c-1] + self.matrix_sum[r-1][c] + self.matrix_sum[r][c-1] - self.matrix_sum[r-1][c-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.matrix_sum[row2+1][col2+1] - self.matrix_sum[row1][col2+1] - self.matrix_sum[row2+1][col1] + self.matrix_sum[row1][col1]

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

# MAIN TAKEAWAYS
# Visualize the matrix: Drawing the 2D matrix helps understand indexing and avoid off-by-one errors.
# Use an auxiliary matrix with an extra row and column (n+1 × m+1): This simplifies prefix-sum calculations and boundary handling.
# Use 2D prefix sums: Precompute cumulative sums to answer any rectangular region sum query in O(1) using inclusion-exclusion.


# Time and Space complexity init:
# time O(n*m)
# space O(n+1*m+1)

# Time and Space complexity sumRegion:
# time O(1)
# space O(1)