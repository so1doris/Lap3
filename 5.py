# -*- coding: cp1251 -*-

def is_Prime():
  
    n = int(input())
    if(n == 1):
        return(print(f"Число {n} не простое"))
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return(print(f"Число {n} не простое"))
            else:
                return(print(f"Число {n} простое"))
is_Prime()