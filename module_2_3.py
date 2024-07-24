my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
index = 0
print('Числа > 0 в листе:')
while index < len(my_list):
    if my_list[index] == 0:
        index += 1
        continue
    elif my_list[index] > 0:
        print(my_list[index])
    else:
        print(f'Встретилось отрицательное число: {my_list[index]}')
        break
    index += 1