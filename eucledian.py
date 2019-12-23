import matplotlib.pyplot as plt
import math
import numpy as np

def eucledian(arr):
    p = len(arr)
    hasil = np.zeros((p,p))
    non_zero_i = []
    non_zero_j = []
    for i in range(p):
        for j in range(p):
            if (arr[i][j] == 1):
                non_zero_i.append(i)
                non_zero_j.append(j)
    for i in range(p):
        for j in range(p):
            if (arr[i][j] != 1):
                temp = []
                for x in range(len(non_zero_i)):
                    non_zero_x = non_zero_i[x]
                    non_zero_y = non_zero_j[x]
                    rumus = ((i-non_zero_x)**2) + ((j-non_zero_y)**2)
                    akar = math.sqrt(rumus)
                    temp.append(akar)
                minim = min(temp)
                hasil[i][j] = minim
            else:
                hasil[i][j] = 0

    return hasil

arr2 = np.array([[0,0,0,0,0], ##example of biner image
        [0,1,0,0,0],
        [0,0,0,0,0],
        [0,0,0,1,0],
        [0,0,0,0,0]])

hasil = eucledian(arr2)
print(hasil)

f, (x1,x2) = plt.subplots(1,2)
x1.imshow(arr2, 'gray')
x2.imshow(hasil, 'gray')
plt.show()

