# -*- coding: cp1251 -*-

from ast import Return


def  is_year_leap():
    n = int(input())
    if(n % 4 == 0 and n%100 != 0 or n%400 == 0):
        return(print("Год високосный"))
    else:
        return(print("Год не високосный"))

is_year_leap()
    