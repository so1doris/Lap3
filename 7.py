# -*- coding: cp1251 -*-

from turtle import pen


buff = 0
kO = 0
kCH = 0
kP = 0
unic = 0

for i in range(5):
    a = int(input())
    if (a != buff):
       if (a % 2 == 0):
           kCH += 1
       if (a < 0):
           kO += 1
       if (-256 <= a and a <= 1024):
           kP += 1
       if (a != buff):
           unic += 1
if (unic == 5):
    print(f"Все числа уникальные,  количество четных {kCH}, отрицательных {kO},лежащих в промежутке [-256 ; 1024] {kP}")
else:
    print (f"Все числа уникальные,  количество четных {kCH}, отрицательных {kO},лежащих в промежутке [-256 ; 1024] {kP}")

        
    
    