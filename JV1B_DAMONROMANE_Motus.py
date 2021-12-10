import random
from types import ModuleType 
from colorama import init, Fore, Back, Style

listemots= ["banane", "agneau", "raidir", "poulpe", "palmes", "souris", "canard", "girafe", "maison" ,"meduse"]
tentatives= 8   
victoire= False
Défaite= True 
motvide='_ _ _ _ _ _ '

print(Back.WHITE, Fore.BLACK + motvide)



def choixmot(listemots):    
    return random.choice(listemots)

def indicelettre(lettre,mot): 
    for i in range(0,len(mot)):
        if mot[i]== lettre:
            return i

def lettremot(lettre,mot):
    trouver = False
    for i in range(0,len(listemots)):
        if mot[i] == lettre:
            trouver = True
    return trouver

def listelettres(mot):
    liste = len(listemots) * [""]
    compteur = 0
    for i in range(0,len(mot)):
        if not(lettremot(mot[i],liste)):
            liste[compteur] = mot[i]
            compteur += 1