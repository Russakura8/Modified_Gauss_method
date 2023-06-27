N = int(input())
matrix = []
f = []
x = []
for i in range(N):
    a = [float(item) for item in input().split(' ')]
    if len(a) != N + 1:
        raise Exception("error")
    matrix.append(a[:N])
    f.append(a[N])
    x.append('x' + str(i+1))

def print_matrix(matrix):
    length = len(matrix)
    for i in range(length):
        print(' '.join(map(str, matrix[i])))

    print('\n')

def find_max(matrix, step):
    maximum = (matrix[step][step], step, step)
    length = len(matrix)

    for i in range(step, length):
        for j in range(step, length):
            if matrix[i][j] > maximum[0]:
                maximum = (matrix[i][j], i, j)

    return maximum


def change(matrix, x, f):
    length = len(matrix)
    for i in range(length - 1):
        clue = find_max(matrix, i)
        tmp = f[clue[1]]
        f[clue[1]] = f[i]
        f[i] = tmp
        tmp = x[clue[2]]
        x[clue[2]] = x[i]
        x[i] = tmp
        tmp = matrix[clue[1]].copy()
        matrix[clue[1]] = matrix[i].copy()
        matrix[i] = tmp[:]

        for j in range(length):
            tmp = matrix[j][clue[2]]
            matrix[j][clue[2]] = matrix[j][i]
            matrix[j][i] = tmp


        for k in range(i+1, length):
            koef = (matrix[k][i] / clue[0])
            f[k] -= koef * f[i]
            for l in range(length):
                if l == i:
                    matrix[k][l] = 0
                else:
                    matrix[k][l] -= matrix[i][l] * koef



def solve(matrix, x, f):
    change(matrix,x, f)
    length = len(x)
    solution = [0] * length
    for i in range(length):
        main_element = matrix[i][i]
        f[i] /= main_element
        for j in range(length):
            matrix[i][j] /= main_element

    for i in range(length - 1, -1, -1):
        solution[i] = f[i]
        for j in range(length):
            if i != j:
                solution[i] -= solution[j] * matrix[i][j]

    for i in range(length):
        print(x[i] + ' = ' + str(solution[i]))






print_matrix(matrix)
solve(matrix,x,f)

"""3
2 3 4 4
2 324 2 1
23 -1 28 2"""

"""5
27 72 72 19 91 01
37 84 84 29 91 49
37 46 36 72 82 92
128 17 62 -1 -743 0
27 4 5 6 81 1"""

"""2
1 -1 0
2 2 4"""