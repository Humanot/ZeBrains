#1
# Написать функцию, которая по переданной строке (например: "Тест"), возвращает словарь ({1: Т, 2: е, 3: c, 4: т}),
# ключами которого будут порядковый номер буквы в строке, а значением буква из строки
def testing(test):
    result = []
    for i in enumerate(test, start=1):
        result.append(i)

    return result

#OUTPUT
print(dict(testing('STRING taken in')))

#2.
# Написать функцию выводящую ряд чисел Фибоначчи до n-го числа (n - входной параметр функции)

#LOOP - Со списком с интервью:
def fib_loop(n):
    first = second = 1

    seq = [first, second]
    for i in range(n - 2):
        #fib1, fib2 = fib2, fib1 + fib2
        fib_seq = first + second
        first = second
        second = fib_seq
        seq.append(fib_seq)

    return seq

def print_fib(n):
    for i in range(n + 1):
        res = fib_loop(i)
        if i == n:
            print(res)

#OUTPUT
print_fib(8) #8 FIB sequence

#Без списка:
def fib_loop(n):
    first = second = 1
    for i in range(n - 2):
        first, second = second, first + second

    return first

def print_fib_2(n):
    for i in range(2, n + 2):
        punc = ', '
        if i == n + 1:
            punc = '.'

        print(fib_loop(i), end=punc)

#OUTPUT
print_fib_2(8) #8 FIB sequence