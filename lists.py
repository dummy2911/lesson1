#!/usr/local/bin/python3

numbers = [3,5,7,9,10.5]
print(f'Our list includes these elements: {numbers}')
print(f'Count of elements in the list is {len(numbers)}\n')
numbers.append("Python")
print('We added Python in list\n')
print(f'Now our list includes these elements: {numbers}')
print(f'And count of elements in the list is {len(numbers)}')
print(f'\nThe first element of the list is {numbers[0]}')
print(f'\nThe last element of the list is {numbers[-1]}')
print(f'\nFrom the 2th to the 4th elements of the list are {numbers[1:4]}')
print(f'\nNow deleting "Python" from the list:')
numbers.remove("Python")
print(f'\nAnd returning new list {numbers}')
