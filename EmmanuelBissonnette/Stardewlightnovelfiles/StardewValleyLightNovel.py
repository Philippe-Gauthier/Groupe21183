#libraries

#variables
current_page = () 
money = ()
melons = ()
hearts = ()
iridium = ()
carpe_mutante = ()
chosen_page = ()
display_page = ()
done = ()


# une fonction qui permet de sauvegarder
def save ():
    open('save.txt', 'w').close()
    file = open("save.txt","w")
    content = str(current_page) + str(money) + str(melons) + str(hearts) + str(iridium) + str(carpe_mutante)
    file.write(content)
    file.close()

#une fonction pour call une page dans une liste de fichier txt 
def page_calling (page_number):
    page_number = str(page_number)
    page_number =  page_number + ".txt"
    file = open(page_number,"r")
    char = file.readlines()[1]
    header =  char[0]
    if header == current_page:
        page = file.readlines()[2:]
        file.close()
        return (page)
    else:
        print("numero de page invalide")

# une fonction pour ajouter les items au joueur
def items_get ():
    item_page = str(current_page + ".txt")
    open(item_page, "r")
    char = file.readlines()[1]
    money = money + char[1]
    melons = melons + char[2]
    hearts = hearts + char[3]
    iridium = iridium + char[4]
    carpe_mutante = carpe_mutante + char[5]
    file.close()
    
# une fonction de win_condition elle na aucune entree elle verrifie seulement
# si le joueur a reussi a gagner le jeux en comparant les valeurs 
# de linventaire du joueur au valeur demandee pour ganger
def win_con ():
    if current_page == 10 and money == 100 and melons == 1 and hearts == 6 and iridium == 5 and carpe_mutante == 1:
        while reponse != 'X' or 'R':
            reponse = input("Bravo vous avez gagne le centre communautaire est restaure et tout les villageois sont heureux \n que voulez vous faire \n quitter appuyez sur X      recomencer appuyez sur R")
            if reponse == 'X':
                save()
                return(True)
            elif reponse == 'R': open('save.txt', 'w').close()  

            else: 
                print ("reponse invalide entrez une reponse valide")

            
    else : 
        pass 





#ouverture du ficher de sauvegarde 
with open("save.txt","r") as file:
    char = file.read()
    current_page = char[0]
    money = char[1]
    melons = char[2]
    hearts = char[3]
    iridium = char[4]
    carpe_mutante  = char[5]
    file.close() 

#main
#while done != True :
    display_page = page_calling(current_page)
    print (display_page)