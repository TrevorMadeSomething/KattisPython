# gameplan ->
# .x.       ..xx..        .x.       .x.
# x.x  ->   xx..xx        x.x  ->   .x.
# .x.       ..xx..        .x.       x.x
#                                   x.x
#                                   .x.
#                                   .x.
import sys
import numpy as np


def main():
    inputData = input()
    inputData = inputData.replace(' ', '')
    R = int(inputData[0])
    C = int(inputData[1])
    Zr = int(inputData[2])
    Zc = int(inputData[3])
    matrix = []

    for i in range(R):
        temp = []
        for j in range(C):
            temp1 = sys.stdin.read(1)
            if temp1 != '\n':
                temp.append(temp1)
            else:
                temp.append(sys.stdin.read(1))
        matrix.append(temp)

    matrix = np.repeat(matrix, repeats=Zr, axis=0)
    matrix = np.repeat(matrix, repeats=Zc, axis=1)

    for a in range(R * Zr):
        if a != 0:
            print()
        for b in range(C * Zc):
            print(matrix[a][b], end='')


main()
