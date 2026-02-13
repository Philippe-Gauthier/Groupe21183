"""
Auteur: James Bergeron
Date: 2026-02-03
Description: Script Python pour le projet de livre interactif.
"""
from socket import close


class Page:
    def __init__(self, numero, contenu_initial=None):
        self.numero = numero
        self.contenu = [contenu_initial] if contenu_initial else []

    def ajouter_texte(self, texte):
        if not isinstance(texte, str):
            raise TypeError("Le texte doit être une chaîne de caractères.")
        self.contenu.append(texte)

    def afficher(self):
        print(f"Page {self.numero}:")
        for ligne in self.contenu:
            print(ligne)

# Exemple d'utilisation
if __name__ == "__main__":
    try:
        # Création d'une page vide
        pagetitle = Page(1)

        # Ajout de texte
        pagetitle.ajouter_texte("Le chemin non prévu.")
        pagetitle.ajouter_texte("Par James Bergeron")
        pagetitle.ajouter_texte("2026-02-03")   
        

        # Affichage
        pagetitle.afficher()
        page_suivante = input("Appuyez sur Entrée pour continuer...")


        # Création d'une autre page avec contenu initial
        page2 = Page(2, "Situation initiale.")
        page2.ajouter_texte("Shade est un jeune cartographe talentueux voulant explorer des territoires inconnus pouvant avoir des dangers mortels.")
        page2.ajouter_texte("Celui-ci arrive sur une île mystérieuse et il commence son exploration.")
        page2.ajouter_texte("Après avoir marché pendant plusieurs heures, il arrive devant une intersection du sentier dont il suivait le tracé.")
        page2.ajouter_texte("Shade doit maintenant choisir un chemin.")
        page2.ajouter_texte("a- Prendre le chemin de gauche menant vers une forêt dense.")
        page2.ajouter_texte("b- Prendre le chemin de droite menant vers une grotte sinueuse dans la montagne menant à un village mystérieux.")
        page2.afficher()

        page2.ajouter_texte("Quel est votre choix?")
        choix = input("Entrez a ou b: ")
        if choix == "a":
            page2.ajouter_texte("Vous avez choisi le chemin de gauche vers la forêt dense.")
        elif choix == "b":
            page2.ajouter_texte("Vous avez choisi le chemin de droite vers la grotte sinueuse.")    
        elif choix == "0,3,4,5,6,7,8,9,q,w,e,r,t,y,u,i,o,p,s,d,f,g,h,j,k,l,z,x,c,v,b,n,m":
            page2.ajouter_texte("Erreur: Veuillez entrer un choix valide (a ou b).")
        page2.afficher()
        page_suivante = input("Appuyez sur Entrée pour continuer...")
        if choix == "a":
            while page_suivante == "a":
                open_page3 = "a"
    
                page3 = Page(3)
                page_suivante = page3.afficher()
                page_suivante = input("Appuyez sur Entrée pour continuer...")

        elif choix == "b":
            while page_suivante == "b":
                if page3 == "a":
                    not open_page4 == "b"
                open_page4 = "b"
                not open_page3 == "a"
                page4 = Page(4)
                page_suivante = page4.afficher()
                page_suivante = input("Appuyez sur Entrée pour continuer...")

        # Ajout d'une page avec du texte initial
        page3 = Page(3, "Shade décide de prendre le chemin de gauche vers la forêt dense.")
        page3.ajouter_texte("Il marche pendant plusieurs heures dans la forêt dense.")
        page3.ajouter_texte("Il tombe dans un piège et se blesse légèrement.")
        page3.afficher()

        # Ajout d'une page avec du texte initial
        page4 = Page(4, "Shade décide de prendre le chemin de droite vers la grotte sinueuse.")
        page4.ajouter_texte("Il marche pendant plusieurs heures dans la grotte sinueuse.")
        page4.ajouter_texte("Il arrive dans un village mystérieux où il rencontre des habitants étranges.")
        page4.afficher()



    except (ValueError, TypeError) as e:
        print(f"Erreur : {e}")