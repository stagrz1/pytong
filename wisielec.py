import random

print("Hej, zagrajmy w wisielca!")
lista=("szkola", "krzeslo", "Szczebrzeszyna", "Pomorze", "Kamienie")
wyraz= random.choice(lista)
tablica= list("_"* len (wyraz))

zycia=7

while zycia>0:
    print("pozostalo Ci ", zycia, "zyc")
    print("--------------")
    print("--------------")
    print(" ".join(tablica))
    print("--------------")
    print("--------------") 

    litera=input("podaj litere")

if litera in wyraz:
     for i in range(len(wyraz)):
         if wyraz[i] == litera:
             tablica[i] = litera

if "".join(tablica) == wyraz:
    print("pozostalo Ci ", zycia, "zyc")
    print("")
    print(" ".join(tablica))
    print("")
    print("wygrales!!")    
    


else: zycia -=(-1)
