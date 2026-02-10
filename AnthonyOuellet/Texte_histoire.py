### Projet 1: Livre interractif (Par Anthony Ouellet)

# Situation initiale
def situation_initiale():
    print("test")
    print("test")
    print("test")
    print("test")
    print("test")
    print("test")
    print("test")

    choix = input("\nQuel est votre choix? (1, 2 ou 3) : ")
    print("(1) Choix 1")
    print("(2) Choix 2")
    print("(3) Choix 3")

    if choix == "1":
        chemin_1()
    elif choix == "2":
        chemin_2()
    elif choix == "3":
        chemin_3()
    else: 
        print("Saisie invalide. Entrez un nombre de 1 à 3 correspondant à votre choix.")
        situation_initiale()
    

def chemin_1():
    print("\ntest")
    print("test")
    print("test")
    print("test")

def chemin_2():
    print("\ntest")
    print("test")
    print("test")

def chemin_3():
    print("\nTest")
    print("test")

# Lancement de l'hisoire
situation_initiale()