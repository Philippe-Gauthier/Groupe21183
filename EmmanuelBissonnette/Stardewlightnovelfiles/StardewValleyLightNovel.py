# sa bugait sinon jai pas u le chois de le hard initialise
done = ()



# une fonction qui permet de sauvegarder
#elle prend aucune entree 
# elle ne retourne rien
# elle ouvre le ficher de sauvgarde elle sassure dajouter 0 au numero de page se qui est nessesaire pour garder une place au numer au dessus de 9
# si le ficher est sous 10 elle ajoute 0 sinon elle fait seulement assembler les valeurs de lincentaire ainsi que des pages  pour ensuite lecrire
def save ():
    open('save.txt', 'w').close()
    global current_page
    current_page = int(current_page)
    #if verifie si la page est sous 10 si oui elle rajoute un 0 avant pour preserver la place au chiffre a deux digit
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
#elle prend le nombre de la page verife quil est un digit sinon retourne false se qui trigger une loop dans le main
#ensuite elle verifie que cette page existe entre 0 et 25 si non elle trigger la loop
#ensuite elle ovre le fichier a partir de la ligne 3 [2;] 
#elle formate le fiicher en retirant les truc indesirable de liste ex [] et les virgules
#elle retourne la page ou false dependament de si la protection dentree detecte un page invalide
#comme cette fonction se situe avant les fonctions sensible au input elle empeche que cest input invalide aie faire bugger les autre fonctions
def page_calling (page_number):
        page_number =  str(page_number)
        #verifie que cest pas juste du texte genre banane et bien des
        if page_number.isdigit() == True:
            page_number = int(page_number)
            #verifie que la page est entre 0 et 25
            if 0 < page_number <= 25 : 
                page_number = str(page_number)
                #ajoute .txt au numero de page pour acceder aux fichier texte
                page_number =  page_number + ".txt"
                file = open(page_number,"r")
                page = file.readlines()[2:]
                #retire les characteres de liste
                for x in page:
                    x = x.strip("[")
                    x = x.strip("]")
                    x = x.strip(",")
                file.close()
                return  page , True
            else:
                #trigger de la boucle de protection
                return ( "",False)
                
        else :
            #trigger la boucle de protection
            return ("",False)
    
# une fonction pour ajouter les items au joueur
#elle prend une entree qui est certainment un chiffre a cause de la verification effectue avant dans le code a laide de la fonction page calling
#elle transtype tout dans le bon type 
#verifie que les items ne depasse pas 9 car sinon sa brise le fichier sauvegarde
# elle ajoute les items cite dans le header des pages au valeurs de linventaire
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
        #ceci a lair inutile mais sa sert a enlever le zero dans le cas ou quelquun ecrit par exemple 04
        current_page = str(current_page) 
        current_page = int(current_page)
        current_page = str(current_page)
        page = current_page + ".txt"
        file = open(page, "r")
        char = file.readlines()[0]
        # les if font en sorte deviter que le nombre ditem aie au dessu de 9 se qui casserait le fichier de sauvegarde
        if money + int(char[0]) > 9:
             pass
        else:
             money = money + int(char[0])
        if melons + int(char[1]) > 9 :
             pass
        else:
            melons = melons + int(char[1])
        if hearts + int(char[2]) > 9 :
             pass
        else: 
            hearts = hearts + int(char[2])
        if iridium + int(char[3]) > 9 :
             pass
        else :
            iridium = iridium + int(char[3])
        if carpe_mutante + int(char[4]) > 9:
             pass
        else:
            carpe_mutante = carpe_mutante + int(char[4])
        file.close()
    
# une fonction de win_condition elle na aucune entree elle verrifie seulement
# si le joueur a reussi a gagner le jeux en comparant les valeurs de linventaire du joueur au valeur demandee pour ganger
#ele verifie si cest la bonne page 
# si ce nest pas la bonne page la fonction ne fait rien si oui et que les comparaison echoue elle print le nombre ditem restant a optenir
#elle permet de choisir si on veux quiter ou reset le jeux
def win_con ():
    #met toute les valeurs en global et les transtype en int pour les comparaison 
    global money 
    global melons
    global hearts
    global iridium
    global carpe_mutante
    global current_page
    current_page = int(current_page)
    money = int(money)
    melons = int(melons)
    hearts = int(hearts)
    iridium = int(iridium)
    carpe_mutante = int(carpe_mutante)
    # le code enbtier de la fonction est skipe si la page nest pas la page du centre communautaire
    if current_page == 25:
        if money > 8 and melons > 0 and hearts > 5 and iridium > 4 and carpe_mutante > 0:
            reponse = ""
            #la boucle si dessus seffectue tant que une des deux option ne son pas selectione
            while reponse != 'x' or 'r':
                reponse = input("Bravo vous avez gagne le centre communautaire est restaure et tout les villageois sont heureux \n que voulez vous faire \n quitter appuyez sur x     recomencer appuyez sur r")
                #le if ici sert a choisir se qui arrive en fonction de lopion choisir
                # soit on continue la boucle soit on reset le fichier et casse la boucle
                #ou on quite le jeux en cassant la boucle main
                if reponse == 'x':
                    #quite le jeux si le joeur apuie sur x en retournant true se qui termine le while ou toutle code est store
                    save()
                    return(True)
                elif reponse == 'r':
                    #remet le ficher a neuf pour recomancer le jeux je sais que la variable sert a rien mais jai plus beaucoup de temps
                    original = ("0100000")
                    file = open('save.txt','w')
                    file.write(original)
                    file.close()
                    print(" \n iscrire page 1 pour recommancer")
                    break
                    
                    
                else: 
                    print ("\n \n reponse invalide entrez une reponse valide")
                
           # si la page est bonne mais que le joueur na pas les items requis le jeux lui dit quel item il lui manque 
        else :
            print (f"vous navez pas reussi a reunir les ressource \n \n vous avez {money} Or sur 9, {melons}melons sur 1, {hearts} sur 6, {iridium}sur 5 et {carpe_mutante} sur 1 \n \n revenez lorsque vous aurez toute les resources")
            input("\n appuyez sur entrer pour continuer")
            current_page = "03"
            return(False)
    else :
        return (False)

#ouverture du ficher de sauvegarde 
# le fichier est ouvert et le code recupere les data dans la premire ligne
# celle si sont mise dans les variables respectives
#le fichier est ensuite ferme 
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
#premierement la page initiale est affiche et formate une fois avec une boucle for
display_page , failsafe = page_calling(current_page)
for x in display_page:
    print(x)
#ensuite le code rentre dans le while pour le reste de la session de jeux
while not done  :
    #input pour choisir la page
    current_page = input("inscrire le numero de la page a laquelle vous voulez aller ")
    #la fonction page calling met soit true sois false dans failsafe en utilisant current page
    # et elle met dans display page la page a laquelle on a retire les truc de liste exemple []n \ ,
    display_page , failsafe = page_calling(current_page)
    #la variable display page est formate et imprime sur le termnale
    for x in display_page:
        print(x)
    #failsafe is faux donc un numero de page invalide entre dans la boucle de protextion qui redemande toujours un nouveau 
    #numero de page jusqua avoir un numer de page valide se qui cause a failsaife de devenir true se qui casse la boucle
    while failsafe == False :
            current_page = input("inscrire une page valide")
            display_page , failsafe = page_calling(current_page)
    # ensuite la fonction current page est calle pour ajouter les items du header a linventaire 
    items_get(current_page)
    # la fonction save sauvegarde dans un fichier texte save.txt les items de linventaire ainsi que la page sur lauqlle vous etes
    #seci permet de quiter le jeux et de revenir plus tard pour finir la partie
    save()
    #finalemetnt wincon retourne sois true ou false dans done se qui determine si le jeux se termine ou continue 
    #en fonction de la page ou on est des items que lon a et de loption que lon choisi a la fin
    done = win_con()