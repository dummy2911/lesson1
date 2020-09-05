#!/usr/local/bin/python3

def get_summ(one, two, delimiter='&'):
    return one.upper()+delimiter+two.upper()
    
word1 = input('Введите первое слово: ')
word2 = input('Введите второе слово: ')

print(get_summ(word1, word2))
