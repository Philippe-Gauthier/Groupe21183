"""Logique principale du jeu Protocole 0*6"""

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
    """ Lance tous les chapitres du jeu. """
    # Des dictionnaires, ne peuvent pas être modifié, reste inchangeable.
    chapitre("chapitre 1- Découverte", [
        {"desc": "Ouvrir immédiatement ", "raison": 0, "ambition": 2},
        {"desc": "Copier sur clé USB", "raison": 1, "ambition": 1},
            {"desc": "Machine virtuelle", "raison": 2, "ambition": 0},
            {"desc": "Lire logs serveur", "raison": 2, "ambition": 0},
            {"desc": "Vérifier signature numérique", "raison": 2, "ambition": 0},
            {"desc": "Scanner antivirus", "raison": 1, "ambition": 0},
            {"desc": "Renommer et isoler", "raison": 1, "ambition": 0},
            {"desc": "Ignorer", "raison": 0, "ambition": 0},

    ])

    chapitre("chapitre 2 - Analyse", [
        {"desc": "Lire ligne par ligne", "raison": 2, "ambition": 0},
            {"desc": "Exécuter partiellement", "raison": 0, "ambition": 2},
            {"desc": "Modifier variable test", "raison": 0, "ambition": 1},
            {"desc": "Chercher auteur", "raison": 2, "ambition": 0},
            {"desc": "Examiner connexions réseau", "raison": 2, "ambition": 0},
            {"desc": "Désactiver caméra", "raison": 1, "ambition": 0},
            {"desc": "Forcer exécution complète", "raison": 0, "ambition": 3},
            {"desc": "Sauvegarder copie externe", "raison": 1, "ambition": 0},
        ])


    chapitre("Chapitre 3 - Prédictions", [
            {"desc": "Tester sur toi", "raison": 0, "ambition": 2},
            {"desc": "Contredire prédictions", "raison": 2, "ambition": 0},
            {"desc": "Noter prédictions", "raison": 1, "ambition": 0},
            {"desc": "Ignorer", "raison": 0, "ambition": 0},
            {"desc": "Simuler faux comportement", "raison": 2, "ambition": 0},
            {"desc": "Partager avec ami", "raison": 0, "ambition": 1},
            {"desc": "Tester données fictives", "raison": 1, "ambition": 0},
            {"desc": "Augmenter précision IA", "raison": 0, "ambition": 2},
    ])


    chapitre("Chapitre 4 - Accès Total", [
            {"desc": "Voir données étudiants", "raison": 0, "ambition": 2},
            {"desc": "Supprimer système", "raison": 3, "ambition": 0},
            {"desc": "Isoler pour étude", "raison": 2, "ambition": 0},
            {"desc": "Améliorer algorithme", "raison": 0, "ambition": 2},
            {"desc": "Bloquer collecte future", "raison": 2, "ambition": 0},
            {"desc": "Exploiter pour notes", "raison": 0, "ambition": 3},
            {"desc": "Exporter base données", "raison": 0, "ambition": 2},
            {"desc": "Restreindre permissions", "raison": 1, "ambition": 0},
        ])


    chapitre("Chapitre 5 - Décision Finale", [
            {"desc": "Garder secret", "raison": 0, "ambition": 3},
            {"desc": "Dénoncer publiquement", "raison": 3, "ambition": 0},
            {"desc": "Modifier éthiquement", "raison": 2, "ambition": 1},
            {"desc": "Détruire données", "raison": 2, "ambition": 0},
            {"desc": "Vendre technologie", "raison": 0, "ambition": 4},
            {"desc": "Confier professeur", "raison": 2, "ambition": 0},
            {"desc": "Publier recherche", "raison": 2, "ambition": 0},
            {"desc": "Désactiver progressivement", "raison": 1, "ambition": 0},
        ])

    calculer_fin()   