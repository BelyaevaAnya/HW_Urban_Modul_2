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
result4 = get_matrix(0, 0, 0)
result5 = get_matrix(5, 0, 0)
result6 = get_matrix(0, 5, 0)
print(result1)  # => [[10, 10], [10, 10]]
print(result2)  # => [[42, 42, 42, 42, 42], [42, 42, 42, 42, 42], [42, 42, 42, 42, 42]]
print(result3)  # => [[13, 13], [13, 13], [13, 13], [13, 13]]
print(result4)  # => []
print(result5)  # => [[], [], [], [], []]
print(result6)  # => []

