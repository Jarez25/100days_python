array1 = [12, 5, 8, 3, 15]
array2 = [7, 1, 14, 9, 4]


array_full = dict(zip(array1, array2))


print(array_full)

for i, j in array_full.items():
    print(i, j)
