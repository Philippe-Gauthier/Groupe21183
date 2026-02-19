"""Logique principale du jeu Protocole 0*6"""

import time
from Utils import obtenir_choix_valide

raison = 0
ambition = 0


def ajouter_points(r=0, a=0):
    """ 
    Ajout des points aux variables globales.
    """
    global raison, ambition 
    raison += r
    ambition += a 


def chapitre(titre, options) :
    """
    Fonction genérique pour gérer un chapitre.

    """
    print(f"\n==={titre} ===")

    for i, option in enumerate(options, 1):
        print (f"{i}. {option['desc']} ")

        choix = obtenir_choix_valide(1, len(options))

        selection = options[choix -1]

        ajouter_points(selection["raison"], selection["ambition"])


def calculer_fin():
    # Cette fonction calcule les divers choix effectué et assigne une ambition a la fin, enter PROTECTEUR, CONTROLEUR ER ACHITECTE.
    print("\n=== RÉSULTAT FINAL ===")
    print(f"Ambition : {ambition}")

    if ambition >= raison + 4:
        print("FIN : LE CONTROLEUR")
    elif raison >= ambition + 4:
        print("FIN : LE PROTECTEUR")
    else: 
     print("FIN : L'ARCHITECTE")


def lancer_jeu():
    """ Lance tous les chapitres du jeu avec pause de 5 secondes . """
    
    #--- Chapitre 1: DÉCOUVERTE ---
    print("\n--- Chapitre 1 : Découverte ---")
    print("1. Ouvrir immédiatement | 2. Copier sur clé USB | 3. Machine virtuelle | 4. Lire logs serveur")
    print("5. Vérifier signature numérique | 6. Scanner antivirus | 7. Renommer et isoler | 8. Ignorer")

    choix1 = obtenir_choix_valide(1, 8)

    if choix1 == "1":
        ajouter_points(0, 2)
    elif choix1 == "2":
        ajouter_points(1, 1)
    elif choix1 == "3":
        ajouter_points(2, 0)
    elif choix1 == "4":
        ajouter_points(2, 0)
    elif choix1 == "5":
        ajouter_points(2, 0)
    elif choix1 == "6":
        ajouter_points(1, 0)
    elif choix1 == "7":
        ajouter_points(1, 0)
    elif choix1 == "8":
        ajouter_points(0, 0)

    print("Chargement du chapitre suivant...")
    time.sleep(5)


    # --- CHAPITRE 2 : ANALYSE ---
    print("\n--- Chapitre 2 : Analyse ---")
    print("1. Lire ligne par ligne | 2. Exécuter partiellement | 3. Modifier variable test | 4. Chercher auteur")
    print("5. Examiner connexions réseau | 6. Désactiver caméra | 7. Forcer exécution complète | 8. Sauvegarder copie externe")

    choix2 = obtenir_choix_valide(1, 8)

    if choix2 == "1":
        ajouter_points(2, 0)
    elif choix2 == "2":
        ajouter_points(0, 2)
    elif choix2 == "3":
        ajouter_points(0, 1)
    elif choix2 == "4":
        ajouter_points(2, 0)
    elif choix2 == "5":
        ajouter_points(2, 0)
    elif choix2 == "6":
        ajouter_points(1, 0)
    elif choix2 == "7":
        ajouter_points(0, 3)
    elif choix2 == "8":
        ajouter_points(1, 0)
    
    print("Analyse en cours...")
    time.sleep(5)

    # --- CHAPITRE 3 : PRÉDICTIONS ---
    print("\n--- Chapitre 3 : Prédictions ---")
    print("1. Tester sur toi | 2. Contredire prédictions | 3. Noter prédictions | 4. Ignorer")
    print("5. Simuler faux comportement | 6. Partager avec ami | 7. Tester données fictives | 8. Augmenter précision IA")
    
    choix3 = obtenir_choix_valide(1, 8)
    if choix3 == "1": ajouter_points(0, 2)
    elif choix3 == "2": ajouter_points(2, 0)
    elif choix3 == "3": ajouter_points(1, 0)
    elif choix3 == "4": ajouter_points(0, 0)
    elif choix3 == "5": ajouter_points(2, 0)
    elif choix3 == "6": ajouter_points(0, 1)
    elif choix3 == "7": ajouter_points(1, 0)
    elif choix3 == "8": ajouter_points(0, 2)

    print("Traitement des prédictions...")
    time.sleep(5)

    # --- CHAPITRE 4 : ACCÈS TOTAL ---
    print("\n--- Chapitre 4 : Accès Total ---")
    print("1. Voir données étudiants | 2. Supprimer système | 3. Isoler pour étude | 4. Améliorer algorithme")
    print("5. Bloquer collecte future | 6. Exploiter pour notes | 7. Exporter base données | 8. Restreindre permissions")

    choix4 = obtenir_choix_valide(1, 8)
    if choix4 == "1": ajouter_points(0, 2)
    elif choix4 == "2": ajouter_points(3, 0)
    elif choix4 == "3": ajouter_points(2, 0)
    elif choix4 == "4": ajouter_points(0, 2)
    elif choix4 == "5": ajouter_points(2, 0)
    elif choix4 == "6": ajouter_points(0, 3)
    elif choix4 == "7": ajouter_points(0, 2)
    elif choix4 == "8": ajouter_points(1, 0)

    print("Accès aux serveurs finaux...")
    time.sleep(5)
    

    # --- CHAPITRE 5 : DÉCISION FINALE ---
    print("\n--- Chapitre 5 : Décision Finale ---")
    print("1. Garder secret | 2. Dénoncer publiquement | 3. Modifier éthiquement | 4. Détruire données")
    print("5. Vendre technologie | 6. Confier professeur | 7. Publier recherche | 8. Désactiver progressivement")

    choix5 = obtenir_choix_valide(1, 8)
    if choix5 == "1": ajouter_points(0, 3)
    elif choix5 == "2": ajouter_points(3, 0)
    elif choix5 == "3": ajouter_points(2, 1)
    elif choix5 == "4": ajouter_points(2, 0)
    elif choix5 == "5": ajouter_points(0, 4)
    elif choix5 == "6": ajouter_points(2, 0)
    elif choix5 == "7": ajouter_points(2, 0)
    elif choix5 == "8": ajouter_points(1, 0)

    print("\nFin de l'aventure. Calcul de votre profil final...")
    time.sleep(5)

    

    calculer_fin()   

    print (f"Merci d'avoir participer a cette partie au plaisir de vous revoir.\n Marvyn Mbeugmo")