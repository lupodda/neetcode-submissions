class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n =len(matrix)
        m=len(matrix[0])
        left=0
        right=n*m-1
        while left<=right:
            mid=left+(right-left)//2
            row, col= mid//m, mid%m
            if target>matrix[row][col]:
                left=mid+1
            elif target<matrix[row][col]:
                right=mid-1
            else:
                return True

        return False