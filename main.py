import numpy as np
import random

rows = 10
cols = 10
random.seed(500)

paths = []
times = np.zeros((rows,cols))

for i in range(rows):
    for j in range(cols-i):
        num = random.randint(1,100)
        times[i][j+i] = num
        times[j+i][i] = num


def factorial(num):
    if num == 1:
        return 1
    return num * factorial(num-1)


def permute(index, array):
    if index == len(array)-1:
        paths.append(array.copy())
        return

    for i in range(len(array)-index):
        i += index

        temp = array[index]
        array[index] = array[i]
        array[i] = temp

        permute(index+1,array)

        temp = array[index]
        array[index] = array[i]
        array[i] = temp


def shortestPath(start, end, visit):
    output = np.zeros((factorial(len(visit))))
    permute(0, visit)

    # Find distances
    for i in range(len(paths)):
        output[i]+=times[start][paths[i][0]]
        output[i]+=times[paths[i][-1]][end]
        for j in range(len(visit)-1):
            output[i]+=times[paths[i][j]][paths[i][j+1]]

    print("\nThe paths are: ")
    print(paths)

    print("\nThe output times are:")
    print(output)

    print("\nThe shortest path is: ")
    print(paths[np.argmin(output)])


if __name__ == '__main__':
    print(times)
    locations = [2,6,3,8,9,1,4]
    shortestPath(0,0,locations)
