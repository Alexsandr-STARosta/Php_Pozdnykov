#Задание 1
import random
n=100
my_file = open("numbers.csv","w+")
for number in range(0,n):
    my_file.write(str(random.randint(1,100)))
    if(number!=n-1):
        my_file.write(",")   
my_file.close()
