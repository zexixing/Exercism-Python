class Matrix(object):
    def __init__(self, matrix_string):
        self.matrix = []
        for i in matrix_string.split('\n'):
            rows = list(map(int, i.split()))
            self.matrix.append(rows)

    def row(self, index):
        return self.matrix[index-1][:]

    def column(self, index):
        return [i[index-1] for i in self.matrix]