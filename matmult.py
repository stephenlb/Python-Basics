
import torch
a = [          
    [1,2], # [1,2]
    [3,4], # [3,4]
]             
t = torch.tensor(a)

#print(t)

#rint(a)
def matmult(a, b):
    newMatrix = []
    x = len(a)
    y = len(a[0])
    z = len(b[0])
    newMatrix = [[0 for _ in range(y)] for _ in range(x)]
    for i in range(x):
        for j in range(y):
            for k in range(z):
                newMatrix[i][j] +=a[i][k] * b[k][j]
    return newMatrix

print(matmult(a,a))
print(t @ t)
