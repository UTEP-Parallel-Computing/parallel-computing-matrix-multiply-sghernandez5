#author:Sofia Hernandez

import time
import pymp
import numpy as np
def genMatrix(size = 1024, value = 1):
    matrix = [[value for col in range(0,size)] for row in range(0,size)]
    return matrix

def printSubarray( matrix, size = 10):
    for row in range (1, size):
              for col in range (1,size):
                        print(f'{matrix[row][col]} ', end=' ')
              print(' ')

def matrix_multi(a,b):
    result = []
   # sharedMatrix = pymp.shared.list()
    arr = [[0 for col in range(0,len(b[0]))] for row in range(0, len(a))]
    sharedMatrix = pymp.shared.list()
    with pymp.Parallel(8) as p:
        print(f'Hello from thread {p.thread_num} of {p.num_threads}')
        for i in p.range(len(a)):
                       for j in range(len(b[0])):
                           for k in range(len(b)):
                              arr[i][j] += a[i][k] * b[k][j]
                           sharedMatrix.append(arr)
    return sharedMatrix


def main():
    a = genMatrix(80,2)
    b = genMatrix(80,4)

    #calculate time
    startTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    arr =  matrix_multi(a,b)
    endTime = time.clock_gettime(time.CLOCK_THREAD_CPUTIME_ID)
    print(f'Elapse time { endTime-startTime:.2f} seconds')
    print('Matrix Result')
    printSubarray(arr,10)

if __name__ == '__main__':
    main(); 
