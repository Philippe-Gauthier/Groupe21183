"""
Nom du fichier : Projet 1.py
Auteur : Marie-Hélène Mercier
"""

def ask_choice(min_value, max_value):
    """
    Cette fonction permet de forcer l'utilisateur à utiliser des nombres 
    de 1 à 4 ou  de 1 à 2 et ainsi éviter que le jeu plante. Elle reçoit 2 paramètres: 
    valeur minimal et valeur maximale. Elle répète la question tant qu'une valeur 
    valide n'est pas fournie et retourne un entier valide.

    Args:
        min_value (int): Valeur minimale acceptée.
        max_value (int): Valeur maximale acceptée.

    Returns:
        int: Le choix valide entré par l'utilisateur.

    """
    #Crée une boucle qui s'arrêtera quand l'on retourne un choix.
    while True:
        #Attend que l'on écrive quelque chose.
        choice = input("> ")
        #Vérifie si la variable choice est composé uniquement de chiffres.
        if choice.isdigit():
            #Transforme les numéros string en nombre, exemple: "1."
            choice = int(choice)
            #Vérifie si le nombre est accepté.
            if min_value <= choice <= max_value:
                #Quitte la fonction et envoie le nombre au programme principal.
                return choice
            else:
                #Le f permet d'insérer des variables dans le texte.
                print(f"Entrez un nombre entre {min_value} et {max_value}.")
        else:
            print("Entrez un nombre.")

def play_again():
    """
    Cette fonction permet à l'utilisateur de choisir s'il veut
    rejouer ou terminer la partie.

    Returns:
        bool: True si l'utilisateur veut rejouer, False sinon.

    """
    #Crée une boucle qui s'arrêtera quand on utilise return.
    while True:
        #Demande à l'utilisateur s'il veut rejouer.
        rejouer = input("Rejouer? (oui/non): ").lower()
        #Si oui, returne True et le jeu recommence.
        if rejouer == "oui":
            return True
        #Si non, retourne False et le jeux arrête.
        elif rejouer == "non":
            print("Merci d'avoir joué!")
            return False
        else:
            print("Entrez oui ou non.")




def start_game():
    """
    Démarre le jeu.

    Présente des choix et dirige l'utilisateur vers différentes branches selon
    les décisions du joueur.

    La fonction utilise la fonction ask_choice() pour valider les entrées
    et se termine lorsqu'une fin est atteinte.

    Return:
        None
    """
    print("--- Zdzisław Beksiński ---")
    print("Tu es sur une plaine de cendres. Un carnet vide repose dans ta main.")
    print("1. Avancer vers la cité")
    print("2. Examiner le carnet")
    print("3. Regarder le ciel.")
    print("4. T'asseoir dans la cendre")

    choice = ask_choice(1, 4)
    if choice == 1:
        print("--- Avancer vers la cité ---")
        print("Quatre formes émergent.")
        print("1. Os")
        print("2. Pierre")
        print("3. Métal")
        print("4. Oeil")

        choice = ask_choice(1, 2)
        if choice == 1:
            print("Os")
            print("1. Avancer")
            print("2. Toucher statue.")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Prison des os.")
            elif choice == 2:
                print("FIN : Statue vivante.")
        
        elif choice == 2:
            print("Pierre")
            print("1. Lire gravures.")
            print("2. Continuer")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Stase éternelle.")
            elif choice == 2:
                print("FIN : Couloir infini.")
        
        elif choice == 3:
            print("Métal")
            print("1. Explorer machines.")
            print("2. Monter passerelle")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Fusion mécanique.")
            elif choice == 2:
                print("FIN : Chute suspendue.")
    
        elif choice == 4:
            print("Oeil")
            print("1. Accepter vision.")
            print("2. Rejeter vision")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Vision infinie.")
            elif choice == 2:
                print("FIN : Oubli.")

    
    elif choice == 2:
        print("--- Examiner le carnet ---")
        print("Les pages frémissent.")
        print("1. Toucher le dessin")
        print("2. Refermer le carnet")
        print("3. Déchirer la page")
        print("4. Observer en silence")

        choice = ask_choice(1, 2)
        if choice == 1:
            print("Toucher dessin")
            print("1. Entrer dessin")
            print("2. Observer.")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Absorption.")
            elif choice == 2:
                print("FIN : Compagnon invisible.")
        
        elif choice == 2:
            print("Refermer carnet")
            print("1. Ouvrir à nouveau.")
            print("2. Partir")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Boucle temporelle.")
            elif choice == 2:
                print("FIN : Néant silencieux.")
        
        elif choice == 3:
            print("Déchirer page")
            print("1. Lire morceaux.")
            print("2. Écrire dessus")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Messages brisés.")
            elif choice == 2:
                print("FIN : Création fugace.")
    
        elif choice == 4:
            print("Observer en silence")
            print("1. Attendre.")
            print("2. Tourner page")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Temps suspendue.")
            elif choice == 2:
                print("FIN : Monde qui change.")


    elif choice == 3:
        print("--- Regarder le ciel ---")
        print("Quelque chose bouge.")
        print("1. Continuer de regarder")
        print("2. Fermer les yeux")
        print("3. Lever le carnet")
        print("4. Reculer")

        choice = ask_choice(1, 2)
        if choice == 1:
            print("Continuer")
            print("1. Observer frome")
            print("2. Approcher ombre.")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Ascension.")
            elif choice == 2:
                print("FIN : Ombre vivante.")
        
        elif choice == 2:
            print("Fermer yeux")
            print("1. Compter souffle.")
            print("2. Ouvrir yeux")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Oubli.")
            elif choice == 2:
                print("FIN : Vision éclatée.")
        
        elif choice == 3:
            print("Lever carnet")
            print("1. Toucher ciel.")
            print("2. Lire à voix haute")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Énergie du ciel.")
            elif choice == 2:
                print("FIN : Cri silencieux.")
    
        elif choice == 4:
            print("Reculer")
            print("1. Entrer cité.")
            print("2. Toucher sol")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Mirage.")
            elif choice == 2:
                print("FIN : Racines anciennes.")
    
    
    elif choice == 4 :
        print("--- T'asseoir dans la cendre ---")
        print("1. Te relever")
        print("2. T'allonger")
        print("3. Écrire ton nom")
        print("4. Laisser tomber le carnet")

        choice = ask_choice(1, 2)
        if choice == 1:
            print("Te relever")
            print("1. Avancer")
            print("2. Observer le ciel.")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Illusion.")
            elif choice == 2:
                print("FIN : Vent éveillé.")
        
        elif choice == 2:
            print("T'allonger")
            print("1. Rêver.")
            print("2. Fermer yeux")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Sommeil éternelli.")
            elif choice == 2:
                print("FIN : Absorption douce.")
        
        elif choice == 3:
            print("Écrire nom")
            print("1. Lire page.")
            print("2. Lever yeux")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Mot oublié.")
            elif choice == 2:
                print("FIN : Nom dans le vent.")
    
        elif choice == 4:
            print("Laisser tomber carnet")
            print("1. Ramasser.")
            print("2. Partir")

            choice = ask_choice(1, 2)
            if choice == 1:
                print("FIN : Livre vivant.")
            elif choice == 2:
                print("FIN : Néant mouvant.")

while True:
    #Démarre le jeux.
    start_game()
    #Si la fonction rejouer retoure True le jeux recommence.
    rejouer = play_again()
    #Si la fonction rejouer retourne False le jeux s'arrête.
    if rejouer == False:
        break