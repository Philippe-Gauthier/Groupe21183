"""Module utilitaire du Projet Protocole 0*6"""
 
def obtenir_choix_valide(min_val, max_val):
    """Demande un choix valide à l'utilisateur."""
    while True:
        try:
            choix = int(input("Votre choix : "))
            if min_val <= choix <= max_val:
                return choix
            else:
                print("Choix hors limite.")
        except ValueError:
            print("Veuillez entrer un nombre valide.")

# Exemple d'utilisation
choix = obtenir_choix_valide(1, 5)
print(f"Vous avez choisi : {choix}")


# def obtenir_choix_valide(min_val, max_val): On crée une fonction qui:
# Prend une valeur minimale 
# Prend une valeur maximale 
# if min_val <= choix <= max_val :
# return choix= Est-ce que le choix est dans la bonne page. Si oui on retourne la valeur 
# except ValueError:Intercepter les erreur.