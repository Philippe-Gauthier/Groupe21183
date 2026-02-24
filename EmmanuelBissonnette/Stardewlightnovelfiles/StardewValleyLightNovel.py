
done = ()



# une fonction qui permet de sauvegarder
def save ():
    open('save.txt', 'w').close()
    global current_page
    current_page = int(current_page)
    if current_page < 10:
        current_page = "0" + str(current_page) 
        file = open("save.txt","w")
        content = str(current_page) + str(money) + str(melons) + str(hearts) + str(iridium) + str(carpe_mutante)
        file.write(content)
        file.close()
    else : 
        file = open("save.txt","w")
        content = str(current_page) + str(money) + str(melons) + str(hearts) + str(iridium) + str(carpe_mutante)
        file.write(content)
        file.close()

#une fonction pour call une page dans une liste de fichier txt 
def page_calling (page_number):
        page_number =  str(page_number)
        if page_number.isdigit() == True:
            page_number = int(page_number)
            if 0 < page_number <= 30 : 
                page_number = str(page_number)
                page_number =  page_number + ".txt"
                file = open(page_number,"r")
                page = file.readlines()[2:]
                for x in page:
                    x = x.strip("[")
                    x = x.strip("]")
                    x = x.strip(",")
                file.close()
                return  page , True
            else:
                
                return ( "",False)
                
        else :
            return ("",False)
    
# une fonction pour ajouter les items au joueur
def items_get (current_page):
    global money 
    global melons
    global hearts
    global iridium
    global carpe_mutante
    money = int(money)
    hearts = int(hearts)
    melons = int(melons)
    iridium = int(iridium)
    carpe_mutante = int(carpe_mutante) 

    current_page = str(current_page) 
    page = current_page + ".txt"
    file = open(page, "r")
    char = file.readlines()[0]
    money = money + char[0]
    melons = melons + char[1]
    hearts = hearts + char[2]
    iridium = iridium + char[3]
    carpe_mutante = carpe_mutante + char[4]
    file.close()
    
# une fonction de win_condition elle na aucune entree elle verrifie seulement
# si le joueur a reussi a gagner le jeux en comparant les valeurs 
# de linventaire du joueur au valeur demandee pour ganger
def win_con ():
    global current_page
    current_page = int(current_page)
    if current_page == 25:
        if money > 9 and melons > 1 and hearts > 6 and iridium > 5 and carpe_mutante > 1:
            while reponse != 'X' or 'R':
                reponse = input("Bravo vous avez gagne le centre communautaire est restaure et tout les villageois sont heureux \n que voulez vous faire \n quitter appuyez sur X      recomencer appuyez sur R")
                if reponse == 'X':
                    save()
                    return(True)
                elif reponse == 'R': open('save.txt', 'w').close()  

                else: 
                    print ("reponse invalide entrez une reponse valide")
                
            
        else :
            print (f"vous navez pas reussi a reunir les ressource \n \n vous avez {money} Or sur 9, {melons}melons sur 1, {hearts} sur 6, {iridium}sur 5 et {carpe_mutante} sur 1 \n \n revenez lorsque vous aurez toute les resources")
            input("\n appuyez sur entrer pour continuer")
            current_page = "03"
            return(False)
    else :
        return (False)

#ouverture du ficher de sauvegarde 
file =  open("save.txt","r") 
char = file.read()
current_page = char[0:2]
money = char[2]
melons = char[3]
hearts = char[4]
iridium = char[5]
carpe_mutante  = char[6]
file.close() 
#main
display_page , failsafe = page_calling(current_page)
for x in display_page:
    print(x)
current_page = input("inscrire le numero de la page a laquelle vous voulez aller ")
while not done  :
    display_page , failsafe = page_calling(current_page)
    for x in display_page:
        print(x)
    current_page = input("inscrire le numero de page a laquelle vous voulez aller")
    while failsafe == False :
            current_page = input("inscrire une page valide")
            display_page , failsafe = page_calling(current_page)
        
    done = win_con()
    save()