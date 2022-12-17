# !/usr/bin/env python3
# -*- coding: utf-8 -*-

# Дано предложение. Вывести «столбиком» все его буквы и, стоящие на четных местах.

if __name__ == '__main__':
    s = input("Введите строку: ")
    for index, value in enumerate(s):
        if (index + 1) % 2 == 0 and value == 'и':
            print(value, sep="\n")
