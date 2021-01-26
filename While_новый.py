def sun (a, b):
    while a < b:
        print(a, " все еще  меньше ", b)
        a += 1
        if a >= b:
            print("Ура! Дождались!", a)
sun (10,16)

