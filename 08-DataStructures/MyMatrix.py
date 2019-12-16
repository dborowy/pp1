class matrix():

    @staticmethod
    def create(w,h):
        matrix = [[0 for x in range(w)] for y in range(h)]
        return matrix
    @staticmethod
    def print(matrix):
        for row in matrix:
            print(row)
    @staticmethod
    def create_unix(x):
        m = matrix.create(x,x)
        for z in range(len(m)):
            m[z][z]=1
        return m

m = matrix.create_unix(3)
matrix.print(m)
