# tasks/task3.py

def solve():
# Ниже пишите решение задачи
    n=int(input())
    sotni = n // 100
    ostatok = n % 100
    dvadcat = ostatok // 20
    ostatok %= 20
    desyatki = ostatok // 10
    ostatok %= 10
    pyat = ostatok // 5
    ostatok %= 5
    edinici = ostatok
    kupuri = sotni + dvadcat + desyatki + pyat + edinici
    print(kupuri)
   


# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()