first = int(input('Введите 1 целое число: '))
second = int(input('Введите 2 целое число: '))
third = int(input('Введите 3 целое число: '))

if first == second == third:
    print(3)
elif second == third or first == third or first == second:
    print(2)
else:
    print(0)

# => Введите 1 целое число: 123
# => Введите 2 целое число: 456
# => Введите 3 целое число: 789
# => 0

# => Введите 1 целое число: 42
# => Введите 2 целое число: 69
# => Введите 3 целое число: 42
# => 2
