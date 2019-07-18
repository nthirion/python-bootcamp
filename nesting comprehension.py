M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

col2 = [row[1] for row in M]

print(col2)

even_col1 = [row[0] for row in M if row[0] % 2 == 0]

print(even_col1)
