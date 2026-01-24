class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix) // 2):
            for j in range(len(matrix) // 2 + len(matrix) % 2):
                prev = matrix[i][j]
                new_i = j
                new_j = len(matrix) - i - 1
                # self.print_matrix(matrix)
                while new_i != i or new_j != j:
                    temp = matrix[new_i][new_j]
                    matrix[new_i][new_j] = prev
                    prev = temp
                    
                    temp_i = new_i
                    new_i = new_j
                    new_j = len(matrix) - temp_i - 1
                
                matrix[i][j] = prev
                # self.print_matrix(matrix)


    def print_matrix(self, matrix):
        for i in matrix:
            print(i)
        print()