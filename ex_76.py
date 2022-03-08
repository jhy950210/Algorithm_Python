import numpy as np

square = 5
can_find_range = 3

mines = [[1, 0, 0, 1, 0],
          [0, 1, 0, 0, 1],
          [0, 0, 0, 1, 0],
          [0, 0, 0, 0, 0],
          [0, 0, 1, 0, 0]]
s = 0

for i in range(square - can_find_range + 1):
    for j in range(can_find_range):
        if np.sum(mines[i:can_find_range+i, j:can_find_range+j]) > s:
            s = np.sum(mines[i:can_find_range+i, j:can_find_range+j])

print(s)