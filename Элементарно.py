def my_func(number):
    string = str(number)
    result = 0
    for i in range (0, len (string)):
        result = result + int(string[i])
    print(result)
number=int(input ("Введите число: "))
my_func(number)

