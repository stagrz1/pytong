import random

alfabet_do_hasla= "abcdefghijklmnoprstuwzABCDEFGHIJKLMNOPRSTUWZ1234567890!@#$%^&*" 

dlugosc_hasla=int(input("jaka dlugosc mialoby miec twoje haslo?"))

haslo= ''.join(random.sample(alfabet_do_hasla,dlugosc_hasla))

print(haslo)