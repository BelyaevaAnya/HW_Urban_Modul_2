numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = False

for index in range(len(numbers)):
    if numbers[index] == 1:
        continue
    # итерация от 2 до половины указанного числа numbers[index]
    for i in range(2, (numbers[index] // 2) + 1):
        # если numbers[index] делится на любое число между 2 и numbers[index] / 2, это не простое число
        if (numbers[index] % i) == 0:
            is_prime = False
            break
    else:
        is_prime = True
    # определение листа для записи
    if is_prime:
        primes.append(numbers[index])
    else:
        not_primes.append(numbers[index])

print(f'Простые числа: {primes}')
print(f'Не простые числа: {not_primes}')

# =>
# Простые числа: [2, 3, 5, 7, 11, 13]
# Не простые числа: [4, 6, 8, 9, 10, 12, 14, 15]
