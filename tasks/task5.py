# tasks/task5.py

def solve():
# Ниже пишите решение задачи
    n = int(input())
    h = n // 3600
    m = (n % 3600) // 60
    s = n % 60
    min_tens = m // 10
    min_ones = m % 10
    sec_tens = s // 10
    sec_ones = s % 10
    time= ((str(h) + ":") + (str(min_tens)) + (str(min_ones) + ":") + (str(sec_tens)) + (str(sec_ones)))
    print(time)


   
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()