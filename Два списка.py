from random import randrange
def my_func ():
    number_list1=[]
    print("Первый список: ")
    for i in range (0, 5):
        number_list1.append(randrange (0, 10))
        print(number_list1 [i])
    number_list2 = []
    print("Второй список: ")
    for i in range(0, 5):
        number_list2.append(randrange(0, 10))
        print(number_list2[i])
    number_list3 = list(set(number_list1).intersection(set(number_list2)))
    print("Результирующий список: ")
    res_len=len(number_list3)
    for i in range (0, res_len):
        print (number_list3 [i])
my_func()

