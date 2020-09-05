#!/usr/local/bin/python3

a = 2
b = 0.5
print (a+b)

name = 'Alexey'
#New type => Python3.6
print(f'Привет, {name}!')
#Old type < Python3.6
print('Привет, ' + '{}'.format(name) + '!')

v = input('Введите число от 1 до 10: ')
print(f'Ваше число плюс 10 равно {int(v) + 10}')

print(float('1'))
#print(int('2.5'))
print(bool(1))
print(bool(''))
print(bool(0))
print(bool(-3))
