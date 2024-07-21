name = input('Введите имя: ')
if name == 'Urban':
    print('Здравствуйте, администратор!')
if name == 'Денис':
    print('Здравствуйте, преподаватель!')
else:
    print('Привет! ',name)

number = int(input('Введите число: '))
if number % 3 == 0 and number % 5 == 0:
    print('FizzBuzz')
elif number % 5 == 0:
    print('Buzz')
elif number % 3 == 0:
    print('Fizz')
else:
    print('Число не подходит')
#or и andd