import random
import time

def gra_papier_kamien_nozyce():
    print("Witaj w grze Papier, Kamien, Nozyce, wyvierz jedną z opcji")
    print(" 1. Papier")
    print(" 2. Kamień")
    print(" 3. Nozyce")

gra_papier_kamien_nozyce()

wybor_gracza = input("Twoj wybor, (wpisz numer)")



if wybor_gracza not in ["1", "2", "3"]:
    print("postaraj sie wybrac opcje pod numerem 1, 2 lub 3")
  

wybor_gracza = int(wybor_gracza)

mapa_wyborow = {1: "Papier", 2: "Kamien", 3: "Nozyce" }


print("twoj wybor" + mapa_wyborow[wybor_gracza])



wybor_komputera = random.randint(1,3)
print("wybor komputera" + mapa_wyborow[wybor_komputera])

if wybor_gracza == wybor_komputera:
    print("Mamy remis!!")

elif(wybor_gracza == 3 and wybor_komputera == 1) or \
    (wybor_gracza == 1 and wybor_komputera == 2) or \
    (wybor_gracza == 2 and wybor_komputera == 3):
    print("Wygrałeś!!")
else:
    print("Przegrałeś! , spróbuj ponownie")