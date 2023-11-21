import random
import time

def gra_papier_kamien_nozyce():
    print("Witaj w grze Papier, Kamien, Nozyce, wyvierz jedną z opcji")
    print(" 1. Papier")
    print(" 2. Kamień")
    print(" 3. Nozyce")

wybor_gracza = input("Twoj wybor, (wpisz numer)")



if wybor_gracza not in ["1", "2", "3"]:
    print("postaraj sie wybrac opcje pod numerem 1, 2 lub 3")
   

wybor_gracza = int(wybor_gracza)

mapa_wyborow = {1: "Papier", 2: "Kamien", 3: "Nozyce" }


print("twoj wybor")