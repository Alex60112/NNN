import figuryplaskie
import bryly

def main():
    print("Kalkulator Geometryczny")
    print("Dostępne opcje:")
    print("1 - Figury płaskie")
    print("2 - Bryły")
    print("3 - Zakończ program")

    while True:
        choice = input("\nWybierz kategorię: ")

        if choice == "1":
            figury_plaskie_menu()
        elif choice == "2":
            bryly_menu()
        elif choice == "3":
            print("Dziękujemy za skorzystanie z kalkulatora!")
            break
        else:
            print("Nie ma takiej opcji. Spróbuj ponownie.")

def figury_plaskie_menu():
    print("\nFigury płaskie:")
    print("1 - Pole i obwód kwadratu")
    print("2 - Pole i obwód prostokąta")
    print("3 - Pole i obwód równoległoboku")
    print("4 - Pole i obwód trapezu")
    print("5 - Pole i obwód koła")
    print("6 - Pole i obwód trójkąta")
    print("7 - Pole i obwód trójkąta równobocznego")
    print("8 - Pole i obwód rombu")
    print("9 - Powrót do głównego menu")

    while True:
        choice = input("\nWybierz figurę: ")

        if choice == "1":
            a = float(input("Podaj bok kwadratu (a): "))
            print(f"Pole: {figuryplaskie.pole_kwadratu(a)}, Obwód: {figuryplaskie.obwod_kwadratu(a)}")
        elif choice == "2":
            a = float(input("Podaj długość prostokąta (a): "))
            b = float(input("Podaj szerokość prostokąta (b): "))
            print(f"Pole: {figuryplaskie.pole_prostokata(a, b)}, Obwód: {figuryplaskie.obwod_prostokata(a, b)}")
        elif choice == "3":
            a = float(input("Podaj długość podstawy równoległoboku (a): "))
            h = float(input("Podaj wysokość równoległoboku (h): "))
            b = float(input("Podaj długość drugiego boku (b): "))
            print(f"Pole: {figuryplaskie.pole_rownolegloboku(a, h)}, Obwód: {figuryplaskie.obwod_rownolegloboku(a, b)}")
        elif choice == "4":
            a = float(input("Podaj długość pierwszej podstawy trapezu (a): "))
            b = float(input("Podaj długość drugiej podstawy trapezu (b): "))
            h = float(input("Podaj wysokość trapezu (h): "))
            c = float(input("Podaj długość boku trapezu (c): "))
            d = float(input("Podaj długość drugiego boku trapezu (d): "))
            print(f"Pole: {figuryplaskie.pole_trapezu(a, b, h)}, Obwód: {figuryplaskie.obwod_trapezu(a, b, c, d)}")
        elif choice == "5":
            r = float(input("Podaj promień koła (r): "))
            print(f"Pole: {figuryplaskie.pole_kola(r)}, Obwód: {figuryplaskie.obwod_kola(r)}")
        elif choice == "9":
            break
        else:
            print("Nie ma takiej opcji.")

def bryly_menu():
    print("\nBryły:")
    print("1 - Objętość i pole powierzchni sześcianu")
    print("2 - Objętość i pole powierzchni prostopadłościanu")
    print("3 - Objętość i pole powierzchni walca")
    print("4 - Objętość i pole powierzchni stożka")
    print("5 - Objętość i pole powierzchni kuli")
    print("6 - Objętość i pole powierzchni ostrosłupa")
    print("7 - Powrót do głównego menu")

    while True:
        choice = input("\nWybierz bryłę: ")

        if choice == "1":
            a = float(input("Podaj krawędź sześcianu (a): "))
            print(f"Objętość: {bryly.objetosc_szescianu(a)}, Pole: {bryly.pole_szescianu(a)}")
        elif choice == "7":
            break
        else:
            print("Nie ma takiej opcji.")

if __name__ == "__main__":
    main()
