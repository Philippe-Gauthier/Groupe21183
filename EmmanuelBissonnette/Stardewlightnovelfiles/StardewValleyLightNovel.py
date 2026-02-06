#libraries
import time 

#variables
current_page = () 
money = ()
melons = ()
hearts = ()
iridium = ()
carpe_mutante = ()
chosen_page = (str())


# une fonction qui permet de sauvegarder
def sauvegarde (input):
    open('save.txt', 'w').close()
    global current_page
    global money 
    global melons 
    global hearts 
    global carpe_mutante
    file = open("save.txt","w")


# une fonction pour formater la page

#une fonction pour call une page dans une liste de fichier txt 
def page_calling (page_number):
    page_number =  page_number + ".txt"
    file = open(page_number,"r")
    page = file.read()
    file.close()
    return (page)
# une fonction pour afficher une page

# une fonction pour choisier une page 

# une fonction pour quitter le jeux

# une fonction de win_condition


#main


#ouverture du ficher de sauvegarde 
with open("save.txt","r") as file:
    lines = file.readlines()
    current_page = lines[0]
    money = lines[1]
    melons = lines[2]
    hearts = lines[3]
    iridium = lines[4]
    carpe_mutante  = lines[5]
    file.close() 


chosen_page = (str(input("inscrire le numero de page")))
current_page = page_calling (chosen_page)
print(current_page)
input("appuyez sur entrer pour contiuner")

