### Projet 1: Livre interractif (Par Anthony Ouellet)

import time

# Fonction de naration style RPG pour ralentir l'affichage du texte histoire
def nar(texte):
    for lettre in texte:
        print(lettre, end='', flush=True)
        time.sleep(0.05) # Vitesse d'affichage
    print()
    time.sleep(0.5) # Petite pause de réflexion après la phrase

# Situation initiale
def situation_initiale():
    nar("test")
    nar("test")
    nar("test")
    nar("test")
    nar("test")
    nar("test")
    nar("test")

    print("\n(1) Choix 1")
    print("(2) Choix 2")
    print("(3) Choix 3")
    choix = input("\nQuel est votre choix? (1, 2 ou 3) : ")

    if choix == "1":
        chemin_1()
    elif choix == "2":
        chemin_2()
    elif choix == "3":
        chemin_3()
    else: 
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        situation_initiale()
    

def chemin_1(): # Branche principale 1
    nar("\ntest")
    nar("test")
    nar("test")
    nar("test")

    print("\n(1) Choix 1")
    print("(2) Choix 2")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        chemin_1_1()
    elif choix == "2":
        chemin_1_2()
    else: 
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        chemin_1()

def chemin_1_1():
    nar("test")
    nar("test")

def chemin_1_2():
    nar("test")
    nar("test")

def chemin_2(): # Branche principale 2
    nar("\ntest")
    nar("test")
    nar("test")

def chemin_3(): # Branche principale 3
    nar("\nTest")
    nar("test")

# Lancement de l'hisoire
situation_initiale()