def detect_year (year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400!=0:
            print ("Невысокосный год ")
        else:
            print ("Высокосный год ")
    else:
        print ("Невысокосный год ")
year = int(input("Введите год: "))
detect_year (year)
