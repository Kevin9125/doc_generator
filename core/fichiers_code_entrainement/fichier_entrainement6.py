
class Matrix:
    def __init__(self, rows, cols, data=None):
        self.rows = rows
        self.cols = cols
        self.data = data if data else [[0] * cols for _ in range(rows)]
    def multiply(self, other):
        if self.cols != other.rows:
            raise ValueError("Dimension mismatch")
        result = Matrix(self.rows, other.cols)
        for i in range(self.rows):
            for j in range(other.cols):
                sum = 0
                for k in range(self.cols):
                    sum += self.data[i][k] * other.data[k][j]
                result.data[i][j] = sum
        return result
    def transpose(self):
        result = Matrix(self.cols, self.rows)
        for i in range(self.rows):
            for j in range(self.cols):
                result.data[j][i] = self.data[i][j]
        return result