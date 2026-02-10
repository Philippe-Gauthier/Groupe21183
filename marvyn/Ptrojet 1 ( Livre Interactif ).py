
"""
Titre: PROTOCOLE 0*6
#Référence au code 6 = "Oui"
Concept
#Un étudiant en technologie découvre un prograamme caché dans les serveurs du cégep:un système expérimental capable de prédire les décisions 
#humaines.
#Mais le programme commence a prédire ses propres choix.

STRUCTURE GÉNÉRALE 
SYSTÈME INTÉRACTIF

#Le lecteur accumule 2 types de points:
#Raison (Logique)
#Ambition (Risque)
#Les choix modifient ces scores.
A la fin le score dominant détermine la fin.

STRUCTURE DES CHAPITRES
CHAPITRE 1- lE Fichier Caché 
Le laboratoire est presque vide.
Un fichier apparaît : prediction_engine.ps1
Date : 03:12 AM.

Message automatique :

“Sujet détecté.”

Choix :

1-Ouvrir immédiatement (+2 ambition)
2-Copier et analyser en sécurité (+2 raison)
3- Prévenir l'administration (+1 raison)

CHAPITRE 2- La Exécution Directe 
Le programme s'exécute.

“Sujet actuel : VOUS.”
“Probabilité d'activation : 87%.”

Une ligne clignote :
Lancer simulation comportementale ?

Choix :

1- Oui (+2 ambition)
2- Non, Analyser le code(+2 raison)

CHAPITRE 2B — Analyse sécurisée (si choix 2)

Tu ouvres le fichier dans un environnement isolé.

Le code contient :

Analyse des habitudes

Accès aux caméras

Données académiques

Le programme semble prédire des décisions humaines.

Choix :

1-Tester les prédictions sur toi (+1 ambition)
2-Chercher l'origine du programme (+2 raison)

CHAPITRE 2C — Signalement (si choix 3)

Tu informes le département.

Réponse étrange :

“Merci. Nous sommes déjà au courant.”

Ton badge d'accès cesse de fonctionner.

Quelqu'un t'observe.

(+1 raison automatique)

→ Aller au Chapitre 3

CHAPITRE 3 — L'Anomalie

Le programme commence à prédire tes actions :

“Dans 5 secondes, vous allez regarder votre téléphone.”

Et tu le fais.

Tu sens que quelque chose t'influence.

Choix :

1- Essayer de contredire les prédictions (+2 raison)
2- Les utiliser à ton avantage (+2 ambition)
3- Supprimer toutes les traces du programme (+1 raison)

CHAPITRE 4 — L'Accès Total

Tu découvres que le système est relié à :

Données sociales

Résultats scolaires

Réseaux internes

Tu peux maintenant :

1- Exploiter les données pour réussir (+3 ambition)
2-Contacter un journaliste (+2 raison)
3- Modifier le programme pour le comprendre (+1 raison, +1 ambition)

LES FINS

À la fin, compare les scores.

FIN 1 — LE CONTRÔLEUR (ambition > raison)

Tu utilises le système pour manipuler les décisions.

Tu réussis.
Tu anticipes tout.

Mais un jour le programme affiche :

“Probabilité de perte de contrôle : 100%.”

FIN 2 — LE LANCEUR D'ALERTE (raison > ambition)

Tu exposes le projet.

Scandale.

Le système est démantelé.

Tu perds certaines opportunités…
Mais tu gardes ton intégrité.

FIN 3 — L'ÉQUILIBRE (égalité)

Tu modifies le programme.

Il ne prédit plus l'avenir.

Il t'aide à mieux comprendre tes propres décisions.

Tu ne contrôles pas le futur.
Tu apprends à le construire.
"""
"""
PROJET : PROTOCOLE 0x6
Type : Livre interactif (version courte)
Auteur : Marvyn Mbeugmo

Description :
    Ce programme propose un chapitre interactif.
    Le joueur fait un choix qui influence la fin.
"""

# Variables de score
raison = 0
ambition = 0


def chapitre1():
    """
    Chapitre unique de l'histoire.
    Permet au joueur de choisir une action.
    """
    global raison, ambition
    """
    Cette variable n'est pas locale a la fonction. 
    En gros, je dis a python de ne pas inventer une variable ici
"""
    print("=== CHAPITRE 1 : Le fichier mystérieux ===")
    print("Un fichier nommé 'prediction_engine.ps1' apparaît sur le serveur.")
    print("\nQue fais-tu ?")
    print("1 - Ouvrir immédiatement le fichier (+2 Ambition)")
    print("2 - L'analyser prudemment (+2 Raison)")
    print("3 - Ignorer le fichier (aucun point)")

    choix = input("Ton choix (1/2/3) : ")

    if choix == "1":
        ambition += 2
    elif choix == "2":
        raison += 2
    elif choix == "3":
        print("Tu décides de ne pas intervenir.")
    else:
        print("Choix invalide.")
        return chapitre1()
    """
    Retour au chapitre 1 
    """
    

    fin()


def fin():
    """
    Affiche la fin selon les scores.
    """
    print("\n=== FIN ===")
    print(f"Score Raison : {raison}")
    print(f"Score Ambition : {ambition}")

    if ambition > raison:
        print("Tu choisis le risque et le pouvoir.")
    elif raison > ambition:
        print("Tu privilégies la prudence et la logique.")
    else:
        print("Tu restes neutre face à l'inconnu.")


if __name__ == "__main__":
    chapitre1()
