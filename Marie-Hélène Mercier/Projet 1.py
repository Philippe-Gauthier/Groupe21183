def start_game():
    print("--- Zdzisław Beksiński ---")
    print("Tu es sur une plaine de cendres. Un carnet vide repose dans ta main.")
    print("1. Avancer vers la cité")
    print("2. Examiner le carnet")
    print("3. Regarder le ciel.")
    print("4. T'asseoir dans la cendre")

    choice = int(input("> "))
    if choice == 1:
        print("--- Avancer ver la cité ---")
        print("Quatre formes émergent.")
        print("1. Os")
        print("2. Pierre")
        print("3. Métal")
        print("4. Oeil")

        choice = int(input("> "))
        if choice == 1:
            print("Os")
            print("1. Avancer")
            print("2. Toucher statue.")

            choice = int(input("> "))
            if choice == 1:
                print("FIN : Prison des os.")
            elif choice == 2:
                print("FIN : Statue vivante.")
        
        elif choice == 2:
            print("Pierre")
            print("1. Lire gravures.")
            print("2. Continuer")

            choice = int(input("> "))
            if choice == 1:
                print("FIN : Stase éternelle.")
            elif choice == 2:
                print("FIN : Couloir infini.")
        
        elif choice == 3:
            print("Métal")
            print("1. Explorer machines.")
            print("2. Monter passerelle")

            choice = int(input("> "))
            if choice == 1:
                print("FIN : Fusion mécanique.")
            elif choice == 2:
                print("FIN : Chute suspendue.")
    
        elif choice == 4:
            print("Oeil")
            print("1. Accepter vision.")
            print("2. Rejeter vision")

            choice = int(input("> "))
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

        choice = int(input("> "))
        if choice == 1:
            print("Toucher dessin")
            print("1. Entrer dessin")
            print("2. Observer.")

            choice = int(input("> "))
            if choice == 1:
                print("FIN : Absorption.")
            elif choice == 2:
                print("FIN : Compagnon invisible.")
        
        elif choice == 2:
            print("Refermer carnet")
            print("1. Ouvrir à nouveau.")
            print("2. Partir")

            choice = int(input("> "))
            if choice == 1:
                print("FIN : Boucle temporelle.")
            elif choice == 2:
                print("FIN : Néant silencieux.")
        
        elif choice == 3:
            print("Déchirer page")
            print("1. Lire morceaux.")
            print("2. Écrire dessus")

            choice = int(input("> "))
            if choice == 1:
                print("FIN : Messages brisés.")
            elif choice == 2:
                print("FIN : Création fugace.")
    
        elif choice == 4:
            print("Observer en silence")
            print("1. Attendre.")
            print("2. Tourner page")

            choice = int(input("> "))
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

        choice = int(input("> "))
        if choice == 1:
            print("Continuer")
            print("1. Observer frome")
            print("2. Approcher ombre.")

            choice = int(input("> "))
            if choice == 1:
                print("FIN : Ascension.")
            elif choice == 2:
                print("FIN : Ombre vivante.")
        
        elif choice == 2:
            print("Fermer yeux")
            print("1. Compter souffle.")
            print("2. Ouvrir yeux")

            choice = int(input("> "))
            if choice == 1:
                print("FIN : Oubli.")
            elif choice == 2:
                print("FIN : Vision éclatée.")
        
        elif choice == 3:
            print("Lever carnet")
            print("1. Toucher ciel.")
            print("2. Lire à voix haute")

            choice = int(input("> "))
            if choice == 1:
                print("FIN : Énergie du ciel.")
            elif choice == 2:
                print("FIN : Cri silencieux.")
    
        elif choice == 4:
            print("Reculer")
            print("1. Entrer cité.")
            print("2. Toucher sol")

            choice = int(input("> "))
            if choice == 1:
                print("FIN : Mirage.")
            elif choice == 2:
                print("FIN : Racines anciennes.")
    
    

start_game()