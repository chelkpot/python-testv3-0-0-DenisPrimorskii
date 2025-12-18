# tasks/task1.py

def solve():
# Ниже пишите решение задачи
    n= int(input())
    num_last_digit= n%10
    num_second_digit= n//10%10
    num_first_digit= n//100%10
    num_sum= num_last_digit + num_second_digit + num_first_digit
    print(num_sum)


    
# Код ниже не трогать! он нужен для тестов
if __name__ == "__main__":
    solve()