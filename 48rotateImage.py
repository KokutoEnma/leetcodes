class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        1. transpose
        2. reflect
        """

#         self.transpose(matrix)
#         self.reflect(matrix)

#     def transpose(self, matrix):
#         for i in range(len(matrix)):
#             for j in range(i, len(matrix)):
#                 matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

#     def reflect(self, matrix):
#         for i in range(len(matrix)):
#             for j in range(len(matrix)//2):
#                 matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

        """
        rotate and reduce size
        """
        n = 0

        while n <= len(matrix)//2:
            for i in range(n, len(matrix)-n-1):
                matrix[n][i], matrix[i][len(matrix)-n-1], matrix[len(matrix)-n-1][len(matrix)-i-1], matrix[len(matrix)-i-1][n] = matrix[len(
                    matrix)-i-1][n], matrix[n][i], matrix[i][len(matrix)-n-1], matrix[len(matrix)-n-1][len(matrix)-i-1]

            n += 1
