import math

#objetosc bryl
def objetosc_szescianu(a):
    return a**3


def objetosc_kuli(r):
    return (4/3) * math.pi * r**3


def objetosc_walca(r,h ):
    return math.pi * r**2 * h


def objetosc_prostopadloscianu(a,b,c):
    return a * b * c

while True:
    print("Objetosc jakiej bryły chcesz dziś obliczyc?")
    print("1. Sześcian")
    print("2. Kula")
    print("3. prostopadłoscian")  
    print("4. Walec")    
    

    wybor_uzytkownika=input("wybierz numer od 1-4")

    if wybor_uzytkownika == '1':
            a = float(input("Podaj długość boku szescianu: "))
            objetosc  = objetosc_szescianu(a)

    elif wybor_uzytkownika == '2':
            promien = float(input("Podaj promień kuli: "))
            objetosc = objetosc_kuli(promien)

    elif wybor_uzytkownika == '3':
       a = float(input("Podaj długość boku podstawy: "))
       b = float(input("Podaj długość 2 boku podstawy: "))
       c = float(input("Podaj wysokość prostopadloscianu : "))
       objetosc = objetosc_prostopadloscianu(a,b,c)

    elif wybor_uzytkownika == '4':
       r = float(input("podaj dlugosc promienia podstawy: "))
       h = float(input("Podaj wysokosc walca: "))
       objetosc = objetosc_walca(r,h)
    
    
    else:   
            print("Nieprawidłowy wybór. Spróbuj ponownie.")
            continue

    print(f"Objętość bryły: {objetosc:.2f}")

