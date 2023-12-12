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

print("Objetosc jakiej bryły chcesz dziś obliczyc?")
print("1. Sześcian")
print("2. Kula")
print("3. prostopadłoscian")  
print("4. Walec")    


wybor_uzytkownika=int(input("wybierz numer od 1-4"))    

if wybor_uzytkownika == '1':
            promien = float(input("Podaj długość boku szescianu: "))
            objetosc  = objetosc_szescianu

elif wybor_uzytkownika == '2':
            promien = float(input("Podaj promień kuli: "))
            objetosc = objetosc_kuli
elif wybpr_uzyw