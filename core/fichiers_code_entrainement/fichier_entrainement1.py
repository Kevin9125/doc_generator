class Matrix:
    def __init__(self, rows):
        self.rows = rows
        self.m = len(rows)
        self.n = len(rows[0]) if rows else 0

    def multiply(self, other):
        result = [[0 for _ in range(other.n)] for _ in range(self.m)]
        for i in range(self.m):
            for j in range(other.n):
                s = 0
                for k in range(self.n):
                    s += self.rows[i][k] * other.rows[k][j]
                result[i][j] = s
        return Matrix(result)

    def transpose(self):
        result = [[self.rows[j][i] for j in range(self.m)] for i in range(self.n)]
        return Matrix(result)
