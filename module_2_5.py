def get_matrix(n=3, m=3, value=1):
    list_matrix = []
    list_coloumns = []
    for raws in range(n):
        list_coloumns = []
        for coloumns in range(m):
            list_coloumns.append(value)
        list_matrix.append(list_coloumns)
    return list_matrix


result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)
print(result1)
print(result2)
print(result3)
