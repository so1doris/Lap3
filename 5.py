# -*- coding: cp1251 -*-

def is_Prime():
  
    n = int(input())
    if(n == 1):
        return(print(f"����� {n} �� �������"))
    if n > 1:
        for i in range(2, int(n/2)+1):
            if (n % i) == 0:
                return(print(f"����� {n} �� �������"))
            else:
                return(print(f"����� {n} �������"))
is_Prime()