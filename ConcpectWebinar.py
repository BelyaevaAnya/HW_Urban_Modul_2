# Условия (ветвления)
# num = int(input('Введите число: '))
# if num % 2 == 0:
#     print('Четное')
# # if num % 2 != 0:
# #     print('Нечетное')
# else:
#     print('Нечетное')

# month = 3
# if month == 1:
#     print('Январь')
# if month == 2:
#     print('Февраль')
# if month == 3:
#     print('Март')
# elif month == 2:
#     print('Февраль')
# elif month == 3:
#     print('Март')

# match month:
#     case 1:
#         print('Январь')
#     case 2:
#         print('Февраль')
#     case 3:
#         print('Март')

# month = 3
# print(f'Номер месяца: {month}!')
# list_ = [1, 2, 3, 4, 5, 6, 7]
# if len(list_)>4:
#     print('В списке много элементов')

# l = [2, 3, 'Hi', 10, 11]
# i = 0
# while i < len(l):
#     if l[i] == 3:
#         i += 1
#         continue
#     if l[i] == 10:
#         break
#     print(l[i])
#     # i = i + 1
#     i += 1

# l = [2, 3, 'Hi', 10, 11]
# for i in 'HELLO':
#     print(i)
# for i in l:
#     if l[i] == 10:
#         break
#     print(i)

# for i in range(5, 10, 2):
#     print(i)

# numbers = list(range(1, 16))
# print(numbers)
# primes = []
# not_primes = []
#
# for i in numbers:
#     if i == 1:
#         continue
#     is_prime = True
#     for j in range(2, i):
#         if i % j == 0:
#             is_prime = False
#             break
#     if is_prime:
#         primes.append(i)
#     else:
#         not_primes.append(i)
#
# print(primes)
# print(not_primes)

def hello_func(name, age):
    # print(f'Привет, {name}!')
    # print(f'Тебе {age} :)')
    return (f'Привет, {name}!\n'
            f'Тебе {age} :)')


res1 = hello_func('Святослав', 25)
res2 = hello_func('Владимир', 26)

print(res1)
print(res2)
