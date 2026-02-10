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
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        situation_initiale()
    

def chemin_1(): # Branche principale 1
    print("\ntest")
    print("test")
    print("test")
    print("test")

    choix = input("\nQuel est votre choix? (1 ou 2) : ")
    print("(1) Choix 1")
    print("(2) Choix 2")

    if choix == "1":
        chemin_1_1()
    elif choix == "2":
        chemin_1_2()
    else: 
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        chemin_1()

def chemin_1_1():
    print("test")
    print("test")

def chemin_1_2():
    print("test")
    print("test")

def chemin_2(): # Branche principale 2
    print("\ntest")
    print("test")
    print("test")

def chemin_3(): # Branche principale 3
    print("\nTest")
    print("test")

# Lancement de l'hisoire
situation_initiale()