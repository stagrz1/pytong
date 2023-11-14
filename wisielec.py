import random

print("Hej, zagrajmy w wisielca!")
lista=("szkola", "krzeslo", "Szczebrzeszyna", "Pomorze", "Kamienie")

wyraz=str(lista[random.randint(0, len(list) - 1)])
tablica= list(wyraz)

for i in range(len(wyraz)):
    tablica[i]= "_"

zycia=7
while zycia>0:
    print("pozostalo Ci ", zycia, "zyc")
    print("--------------")
    print("--------------")
    print(" ",(tablica))
    print("--------------")
    print("--------------")


    print("podaj litere")
    litera=input()