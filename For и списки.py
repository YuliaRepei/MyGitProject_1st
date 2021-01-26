from random import randrange
number_list = []
for i in range (0, 15):
    number_list.append(randrange(0, 10))
    print(number_list[i])
number = int(input("Пожалуйста, введите число: "))
for i in range (0, 15):
    if number_list[i] == number:
        print("Найденное число: " + str(number)+ ". Порядок числа " + str(i+1))
        break