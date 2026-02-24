
def demander_choix():
    choix = input("Choix (1 ou 2) : ")
    while choix != "1" and choix != "2":
        print("Choix invalide, tape 1 ou 2 s'il te plaît.")
        choix = input("Choix (1 ou 2) : ")
    return choix

#  Début du jeu 
def debut():
    print("\nTu es devant une vieille maison.")
    print("Il fait jour et le soleil passe à travers les branches des arbres.")
    print("La maison semble un peu étrange, mais pas dangereuse.")
    print("1. Entrer dans la maison")
    print("2. Faire le tour de la maison")
    choix = demander_choix()

    if choix == "1":
        entrer()
    elif choix == "2":
        contourner()

def entrer():
    print("\nTu ouvres la porte et tu entres.")
    print("La maison sent le vieux bois et les biscuits oubliés.")
    print("1. Monter à l’étage")
    print("2. Aller dans le salon")
    choix = demander_choix()

    if choix == "1":
        etage()
    elif choix == "2":
        salon()

def etage():
    print("\nTu montes les escaliers doucement.")
    print("Tu vois des portraits et des jouets anciens sur le sol.")
    print("1. Entrer dans une chambre")
    print("2. Avancer dans le couloir")
    choix = demander_choix()

    if choix == "1":
        chambre_etage()
    elif choix == "2":
        couloir()

def chambre_etage():
    print("\nLa chambre est colorée avec de vieux jouets partout.")
    print("1. Regarder sous le lit")
    print("2. Ouvrir l’armoire")
    choix = demander_choix()

    if choix == "1":
        fin("Tu trouves un chat qui dort tranquillement sous le lit. Il te regarde et s'étire avant de se rendormir.")
    elif choix == "2":
        fin("L’armoire est remplie de vieux vêtements et d’un chapeau rigolo que tu essaies juste pour rire.")

def couloir():
    print("\nLe couloir est long mais pas effrayant.")
    print("Tu entends un petit bruit comme un jouet qui tombe.")
    print("1. Continuer doucement")
    print("2. Courir vite")
    choix = demander_choix()

    if choix == "1":
        fin("Tu trouves un coffre avec des bonbons à l’intérieur. Tu prends un petit goûter et continues l’aventure.")
    elif choix == "2":
        fin("Tu trébuches sur un tapis et tombes dans un tas de coussins. Ça te fait rigoler.")

def salon():
    print("\nLe salon est lumineux et plein de meubles anciens.")
    print("1. Regarder les tableaux")
    print("2. S’asseoir sur le canapé")
    choix = demander_choix()

    if choix == "1":
        fin("Les tableaux montrent des paysages rigolos. Tu trouves ça amusant et tu continues ton exploration.")
    elif choix == "2":
        fin("Le canapé est moelleux et tu t’assois pour te reposer. Tu trouves un vieux livre de coloriage et tu passes un moment tranquille.")


def contourner():
    print("\nTu fais le tour de la maison.")
    print("Le jardin est rempli de fleurs et de buissons.")
    print("1. Aller vers la cuisine")
    print("2. Regarder par la fenêtre")
    choix = demander_choix()

    if choix == "1":
        cuisine()
    elif choix == "2":
        fenetre()

def cuisine():
    print("\nLa cuisine sent les biscuits et le chocolat.")
    print("1. Ouvrir le frigo")
    print("2. Regarder le sol")
    choix = demander_choix()

    if choix == "1":
        fin("Le frigo est rempli de friandises. Tu prends un chocolat et tu es content.")
    elif choix == "2":
        fin("Tu trouves un petit jouet caché sur le sol et tu rigoles.")

def fenetre():
    print("\nTu regardes par la fenêtre.")
    print("Tu vois un petit jardin avec des oiseaux qui chantent.")
    print("1. Frapper à la vitre")
    print("2. Partir tranquillement")
    choix = demander_choix()

    if choix == "1":
        fin("Un oiseau vient se poser sur le rebord de la fenêtre et te regarde curieusement.")
    elif choix == "2":
        fin("Tu t’éloignes de la maison, content de ton exploration.")

#  Fin de l’histoire 
def fin(texte):
    print("\n" + texte + " Fin de l’histoire.")

#  Lancer le jeu 
debut()
