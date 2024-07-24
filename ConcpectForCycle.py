# Бесконечный цикл while
# while 1 > 0:
#     print('Hello World!')
# print('Goodbye!')
for i in 1, 2, 3, 4:
    print('ok')

for i in 1, 2, 3, 4:
    print(i)

# i - сохраняет значения последовательности

for i in 'hello':
    print(i)

list_ = ['one', 'two', 'three']
for i in list_:
    print(i)

#
# for i in list_:
#     if i == 'three':
#         list_.remove(i)
# print(list_)

for i in range(5):
    print(i)
# =>
# 0
# 1
# 2
# 3
# 4
#
# for i in range(len(list_)):
#     print(list_[i])
# =>
# one
# two
# three
# for i in range(len(list_)):
#     list_[i] = ':('
#
# print(list_)
# => [':(', ':(', ':(']

list_2 = [2, 3, 4, 5, 1]
sum_ = 0
for i in range(len(list_2)):
    sum_ += list_2[i]

print(sum_)     # => 15

for i in range(1, 11, 2):  # range(start, stop, step)
    print(i)

# Вложенный цикл
for i in range(1, 11):
    print("............")
    for j in range(1, 11):
        print(f'{i} x {j} = {i*j}')
# 1x1
# 1x2
# 1x3
# ...
# 10x10=100

# цикл for может перебирать словари
dict_ = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
for i in dict_:
    print(i,dict_[i])
# a 1
# b 2
# c 3
# d 4

for i, k in dict_.items():
    print(f'{i}, {k}')

# a, 1
# b, 2
# c, 3
# d, 4

