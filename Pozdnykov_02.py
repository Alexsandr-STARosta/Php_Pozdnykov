#Задание 2
text_arr=[]
text=str()

my_file = open("numbers.csv")
my_text = my_file.read()
my_file.close()

for number in range(0,len(my_text)):
    if my_text[number] == ",":
        text_arr.append(int(text))
        text=str()
    else:
        text=text+my_text[number]
text_arr.append(int(text))
out_arr=sorted(text_arr)
print(out_arr)


