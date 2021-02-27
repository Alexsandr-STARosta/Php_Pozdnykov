#Задание 3
print("Введите число от 0 до 9:")
a=int(input())
if a>=0 and a<=9:
    print("Введите степень от 0 до 9:")
    b=int(input())
    if b>=0 and b<=9:
        c=a
        for number in range (b-1):
            c = c*a
        print("Ответ:",c)
    else:
        print("Ввели неправильную степень")
else:
    print("Ввели неправильное число")
