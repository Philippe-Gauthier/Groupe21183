#libraries
import time 

#variables
current_page = () 
money = ()
melons = ()
hearts = ()
iridium = ()
carpe_mutante = ()
short_de_lewis = ()
current_page = ()

#fonctions 

#une fonction qui permet d'initialiser un fichier de sauvegarde 
def get_save_files(): 
    global current_page 
    global money 
    global melons 
    global hearts 
    global iridium 
    global carpe_mutante 
    global short_de_lewis 

    filepath = "save.txt" 
    with open(filepath, "r") as file:
        lines = file.readlines()
        current_page = lines[0]
        money = lines[1]
        melons = lines[2]
        hearts = lines[3]
        iridium = lines[4]
        carpe_mutante  = lines[5]
        short_de_lewis = lines[6]
        file.close()

    


# une fonction qui permet de sauvegarder


# une fonction pour formater la page

#une fonction pour call une page dans une liste de fichier txt 

# une fonction pour afficher une page

# une fonction pour choisier une page 

# une fonction pour quitter le jeux

# une fonction de win_condition


#main
get_save_files()
print(current_page)
