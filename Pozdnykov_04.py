#Задание 3
def polinom (a):
    number_a=len(a)-1
    number_b=0
    while number_a >= 0:
        if a[number_a]==a[number_b]:
            number_a=number_a-1
            number_b=number_b+1
        else:
            return("Фраза не являеться палиндромом")
        
    return("Фраза  являеться палиндромом")   


print("Введите фразу:")
a=str(input())
number_a=len(a)-1
number_b=0
print(polinom(a)) 


