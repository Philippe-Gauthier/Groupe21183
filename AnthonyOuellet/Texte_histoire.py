### Projet 1: Livre interractif (Par Anthony Ouellet)

# Bibliothèque
import time

# Fonction de naration style RPG pour ralentir l'affichage du texte histoire
def nar(texte):
    for lettre in texte: # Pour chaque caractère contenu dans la phrase (un par un)
        print(lettre, end='', flush=True) # Affiche la lettre sans passer à la ligne et force l'affichage immédiat
        time.sleep(0.03) # Vitesse d'affichage
    print()
    time.sleep(0.5) # Petite pause de réflexion après la phrase

# Situation initiale
def situation_initiale():
    nar("La cloche funèbre résonne dans les ruines.")
    nar("Le ciel est noir, figé dans une nuit éternelle.")
    nar("Vous vous réveillez sur un pavé de pierre froide.")
    nar("Votre mémoire est brisée, votre corps marqué de cicatrices anciennes.")
    nar("Vous sentez que quelque chose vous a ramené à la vie, mais à quel prix ?")
    nar("Trois chemins s'offrent à vous, chacun émanant le malheur.")

    print("\n(1) Explorer la cathédrale en ruines")
    print("(2) Descendre dans les catacombes sombres")
    print("(3) Sortir de la cathédrale et prendre la route noyée dans le brouillard")
    choix = input("\nQuel est votre choix? (1, 2 ou 3) : ")

    if choix == "1":
        cathedrale()
    elif choix == "2":
        catacombe()
    elif choix == "3":
        brouillard()
    else: 
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        situation_initiale()
    

def cathedrale(): # Branche principale 1
    nar("\nLa cathédrale est éventrée, ses vitraux pleurent le sang.")
    nar("Des statues déformées vous observent, leurs visages figés dans l'agonie.")
    nar("Au centre de la cathédrale, un chevalier en armure noire garde quelque chose.")
    nar("À votre gauche, un escalier monte vers le clocher.")

    print("\n(1) Affronter le chevalier noir")
    print("(2) Contourner discrètement vers l'autel")
    print("(3) Monter l'escalier vers le clocher")
    choix = input("\nQuel est votre choix? (1, 2 ou 3) : ")

    if choix == "1":
        chevalier_noir()
    elif choix == "2":
        contourne_vers_autel()
    elif choix == "3":
        escalier_clocher()
    else: 
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        cathedrale()

def chevalier_noir(): # Branche 1.1
    nar("\nVous avancez vers le chevalier. Il lève lentement son épée déchiquetée.")
    nar("Ses mouvements sont mécaniques, comme s'il était un pantin de la mort.")
    nar("Le combat est innévitable.")

    print("\n(1) Attaquer frontalement avec rage")
    print("(2) Esquiver et chercher une ouverture")
    print("(3) Tenter de dialoguer avec lui")
    choix = input("\nQuel est votre choix? (1, 2 ou 3) : ")

    if choix == "1":
        attaque_frontal()
    elif choix == "2":
        esquive_ouverture()
    elif choix == "3":
        dialoguer_chevalier()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        chevalier_noir()

def attaque_frontal(): # Branche 1.1.1
    nar("\nVous chargez avec toute votre fureur.")
    nar("L'épée du chevalier vous transperce avant même que vous ne le touchiez.")
    nar("Votre vision s'obscurcit. La mort vous réclame une fois de plus.")
    nar("\n=== FIN: La furie du désespoir ===")
    rejouer()

def esquive_ouverture(): # Branche 1.1.2
    nar("\nVous roulez sous son attaque et frappez ses jambes.")
    nar("Le chevalier s'effondre dans un fracas métallique.")
    nar("Dans sa main, vous trouvez une clé rouillée gravée de symboles anciens.")

    print("\n(1) Prendre la clé et explorer l'autel")
    print("(2) Prendre la clé et monter vers le clocher")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        clé_autel()
    elif choix == "2":
        clé_clocher()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        esquive_ouverture()

def clé_autel(): # Branche 1.1.2.1
    nar("\nLa clé ouvre un coffre derrière l'autel.")
    nar("À l'intérieur, un anneau d'argent noirci pulse d'une énergie malsaine.")

    print("\n(1) Mettre l'anneau")
    print("(2) Le laisser et partir")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        nar("\nL'anneau se resserre autour de votre doigt comme une mâchoire.")
        nar("Des visions de carnage inondent votre esprit.")
        nar("Vous êtes maintenant consumé par sa malédiction.")
        nar("\n=== FIN : L'anneau du chaos ===")

def clé_clocher(): # Branche 1.1.2.2
    nar("\nAu sommet du clocher, la clé ouvre une trappe.")
    nar("Vous découvrez une cage contenant un corbeau parlant.")

    print("\n(1) Libérer le corbeau")
    print("(2) L'interroger d'abord")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 1.1.2.2.1
        nar("\nLe corbeau s'envole, laissant derrière lui une traînée de plumes noires.")
        nar("Il vous guide vers une sortie secrète de la cathédrale.")
        nar("Vous échappez à la malédiction, mais votre destin reste incertain.")
        nar("\n=== FIN : Le messager libéré ===")
        rejouer()
    elif choix == "2":
        interrogation_corbeau()

def interrogation_corbeau(): # Branche 1.1.2.2.2       
    nar("\n « Je connais la sortie de ce cauchemar », croasse-t-il.")
    nar("« Mais le prix est ton humanité. Accepte-tu? »")

    print("\n(1) Accepter le pacte du corbeau")
    print("(2) Refuser et le laisser")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 1.1.2.2.2.1
        nar("\nLe corbeau vous guide vers un portail scintillant.")
        nar("Vous le franchissez et perdez toute conscience de qui vous étiez.")
        nar("\n=== FIN : Le pacte du corbeau ===")
        rejouer()
    elif choix == "2": # Branche 1.1.2.2.2.2
        nar("\nLe corbeau vous regarde avec une tristesse infinie.")
        nar("\nVous redescendez du clocher, plus sage mais toujours prisonnier.")
        nar("\n=== FIN : L'errance éternelle ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        interrogation_corbeau()

def dialoguer_chevalier(): # Branche 1.1.3
    nar("\n« Qui es-tu? » demandez-vous.")
    nar("Le chevalier s'immobilise.")
    nar("« Je...je garde...j'ai oublié quoi...je suis... »")
    nar("Sa voix est un écho lointain imprégné de souffrance.")

    print("\n(1) Lui offrir la paix en le détruisant")
    print("(2) Chercher à le libérer de sa malédiction")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        nar("\nVous le terrassez avec pitié.")
        nar("Il murmure un dernier souffle de gratitude avant de se dissoudre en poussière noire.")
        nar("Son armure reste vide sur le sol, comme un souvenir de l'oubli.")
        nar("\n=== FIN : La miséricorde noire ===")
        rejouer()
    elif choix == "2":
        liberer_chevalier()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        dialoguer_chevalier()

def liberer_chevalier():
    nar("\nVous touchez son casque.")
    nar("Des souvenirs douloureux affluent.")
    nar("Il était autrefois gardien de ce lieu sacré.")

    print("\n(1) Tenter un rituel de purification")
    print("(2) Prendre son rôle de gardien")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        nar("\nLe rituel consume votre énergie vitale mais le libère.")
        nar("Vous vous effondrez, satsisfait d'avoir sauvé une âme.")
        nar("\n === FIN : Le sacrifice du libérateur ===")
        rejouer()
    elif choix == "2":
        nar("\nVous endossez son rôle.")
        nar("Votre corps se rigidifie.")
        nar("Vous êtes maintenant le nouveau gardien éternel.")
        nar("\n=== FIN : Le nouveau gardien ===")

def contourne_vers_autel(): # Branche 1.2
    nar("test")
    nar("test")

def escalier_clocher(): # Branche 1.3
    nar("test")
    nar("test")

def catacombe(): # Branche principale 2
    nar("\ntest")
    nar("test")
    nar("test")

def brouillard(): # Branche principale 3
    nar("\nTest")
    nar("test")

def rejouer():
    choix = input("\nVoulez-vous rejouer? (oui/non) : ")
    if choix == "oui":
        situation_initiale()
    elif choix == "non":
        nar("Merci d'avoir joué.")
    else:
        print("Saisie invalide. Entrez 'oui' ou 'non'.")
        rejouer()


# Lancement de l'hisoire
situation_initiale()