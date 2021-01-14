def print_q (a, b):
    while d < b:
        c = 1
        d = a + c
        print("значение", a, ' - пока еще нет')
        if a >= b:
            print("Ура! Дождались!")
            print_q(10, 15)
