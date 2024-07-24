import random
# Функция с параметром


def say_hello():
    print('Hello')


say_hello()
say_hello()
say_hello()


# Виды функций
# Принимающие, возвращающие, анонимные, обычные

# Принимающие
def say_hello_name(name):
    print('Hello, ' + name + '!')


say_hello_name('Denis')
say_hello_name('Max')
say_hello_name('Anton')


# Возвращающая
def lottery():
    tickets = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    win_tick = random.choice(tickets)
    return win_tick


win = lottery()
print(win)


# Одновременно принимающие и возвращающие

def lottery_2(mon, thue):
    tickets = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(mon, thue)
    return win1, win2


winner1, winner2 = lottery_2('mon', 'thue')
print(winner1, winner2)


def lottery_3(*args, **kwargs):
    tickets = [1, 2, 3, 5, 6, 7, 8, 9, 10]
    win1 = random.choice(tickets)
    tickets.remove(win1)
    win2 = random.choice(tickets)
    print(*args)
    return win1, win2


winner1, winner2 = lottery_3('mon', '1', 'thue')
print(winner1, winner2)


def test(a=2, b=True):
    print(a, b)


test()
# => 2 True
test(False, 'Ok')
# => False Ok
test([1, 2])
# => [1, 2] True
# Распаковка параметров
test(*[1, 2])
# => 1 2
# для распоковки словаря **
dect_ = {'a': 12, 'b': 13}
print(type(dect_))
test(**dect_)
# => 12 13