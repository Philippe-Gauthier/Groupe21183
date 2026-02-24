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
    nar("=== NOUVELLE PARTIE ===")
    nar("\nLa cloche funèbre résonne dans les ruines.")
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
        catacombes()
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

    if choix == "1": # Branche 1.1.2.1.1
        nar("\nL'anneau se resserre autour de votre doigt comme une mâchoire.")
        nar("Des visions de carnage inondent votre esprit.")
        nar("Vous êtes maintenant consumé par sa malédiction.")
        nar("\n=== FIN : L'anneau du chaos ===")
        rejouer()
    elif choix == "2": # Branche 1.1.2.1.2
        nar("\nVous laissez l'anneau et quittez la cathédrale.")
        nar("Vous avez échappé à une malédiction, mais votre destin reste incertain.")
        nar("\n=== FIN : La prudence récompensée ===")
        rejouer()
    else: 
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        clé_autel()

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

    if choix == "1": # Branche 1.1.3.1
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

def liberer_chevalier(): # Branche 1.1.3.2
    nar("\nVous touchez son casque.")
    nar("Des souvenirs douloureux affluent.")
    nar("Il était autrefois gardien de ce lieu sacré.")

    print("\n(1) Tenter un rituel de purification")
    print("(2) Prendre son rôle de gardien")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 1.1.3.2.1
        nar("\nLe rituel consume votre énergie vitale mais le libère.")
        nar("Vous vous effondrez, satisfait d'avoir sauvé une âme.")
        nar("\n=== FIN : Le sacrifice du libérateur ===")
        rejouer()
    elif choix == "2": # Branche 1.1.3.2.2
        nar("\nVous endossez son rôle.")
        nar("Votre corps se rigidifie.")
        nar("Vous êtes maintenant le nouveau gardien éternel.")
        nar("\n=== FIN : Le nouveau gardien ===")
        rejouer()

def contourne_vers_autel(): # Branche 1.2
    nar("\nVous vous faufilez dans l'ombre entre les colonnes brisées.")
    nar("L'autel dégage une lueur malsaine.")
    nar("Un calice rempli d'un liquide noir y repose.")

    print("\n(1) Boire le liquide")
    print("(2) Examiner l'autel de plus près")
    print("(3) Renverser le calice")
    choix = input("\nQuel est votre choix? (1, 2 ou 3) : ")

    if choix == "1":
        boire_liquide()
    elif choix == "2":
        examiner_autel()
    elif choix == "3":
        renverser_calice()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        contourne_vers_autel()

def boire_liquide(): # Branche 1.2.1
    nar("\nLe liquide brûle votre gorge comme de l'acide.")
    nar("Votre corps se transforme. La corruption vous consume.")
    nar("\n=== FIN : La corruption du calice ===")
    rejouer()

def examiner_autel(): # Branche 1.2.2
    nar("\nSous l'autel, vous découvrez des inscriptions anciennes.")
    nar("Elles parlent d'un rituel pour briser le cycle de résurrection.")

    print("\n(1) Tenter le rituel")
    print("(2) Ignorer et partir")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 1.2.2.1
        nar("\nLe rituel demande un sacrifice de sang. Le vôtre.")
        nar("Vous accomplissez le rituel. Le cycle est brisé.")
        nar("\n=== FIN: La Liberté Finale ===")
        rejouer()
    elif choix == "2": # Branche 1.2.2.2
        nar("\nVous partez, condamné à errer pour l'éternité.")
        nar("\n=== FIN: Le Refus du Destin ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        examiner_autel()

def renverser_calice(): # Branche 1.2.3
    nar("\nLe liquide se répand et ronge la pierre.")
    nar("Le chevalier noir rugit et charge vers vous!")

    print("\n(1) Fuir vers les catacombes")
    print("(2) Se battre avec ce que vous avez")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        fuite_catacombes()
    elif choix == "2": # Branche 1.2.3.2
        nar("\nVous vous défendez du mieux que vous pouvez, mais le chevalier est implacable.")
        nar("Il vous terrasse rapidement.")
        nar("\n=== FIN : La fureur du chevalier ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        renverser_calice()

def fuite_catacombes(): # Branche 1.2.3.1
    nar("\nVous vous précipitez vers l'entrée, le chevalier à vos trousses.")
    nar("Vous plongez dans les catacombes sombres, espérant semer votre poursuivant.")
    nar("Les couloirs sont un labyrinthe de mort et de désespoir.")

    print("\n(1) Continuer à fuir dans les catacombes")
    print("(2) Trouver un endroit pour se cacher")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 1.2.3.1.1
        nar("\nVous continuez à courir, mais le chevalier est implacable.")
        nar("Finalement, il vous rattrape et vous terrasse.")
        nar("\n=== FIN : La traque sans fin ===")
        rejouer()
    elif choix == "2": # Branche 1.2.3.1.2
        nar("\nVous trouvez une alcôve secrète et vous y cachez.")
        nar("Le chevalier passe à côté sans vous voir.")
        nar("Vous avez survécu, mais à quel prix ?")
        nar("\n=== FIN : La survie dans l'ombre ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        fuite_catacombes()

def escalier_clocher(): # Branche 1.3
    nar("\nL'escalier en spirale craque sous vos pas.")
    nar("Des murmures emplissent l'air vicié du clocher.")
    nar("Au sommet, une silhouette encapuchonnée vous attend.")

    print("\n(1) Approcher la silhouette")
    print("(2) Observer depuis l'entrée")
    choix = input("\nQuel est votre choix? (1 ou 2): ")

    if choix == "1":
        approcher_silhouette()
    elif choix == "2":
        observer_silhouette()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        escalier_clocher()

def approcher_silhouette(): # Branche 1.3.1
    nar("\nLa silhouette se retourne.")
    nar("C'est un miroir de vous-même.")
    nar("« Je suis ce que tu aurais pu être », dit-il d'une voix glaciale.")

    print("\n(1) Attaquer votre reflet")
    print("(2) Lui parler")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 1.3.1.1
        nar("\nEn le frappant, vous vous frappez vous-même.")
        nar("Vous tombez ensemble dans le vide du clocher.")
        nar("\n=== FIN: Le Suicide Métaphysique ===")
        rejouer()
    elif choix == "2": # Branche 1.3.1.2
        nar("\n« Accepte ton passé », dit le reflet avant de disparaître")
        nar("Vous trouvez la paix intérieure malgré l'horreur environnante.")
        nar("\n=== FIN : L'acceptation ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        approcher_silhouette()

def observer_silhouette(): # Branche 1.3.2
    nar("\nVous observez la silhouette manipuler quelque chose.")
    nar("C'est une cloche. Si elle sonne, quelque chose de terrible arrivera.")
    
    print("\n(1) L'empêcher de sonner")
    print("(2) Laisser faire")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 1.3.2.1
        nar("\nVous vous précipitez et détruisez la cloche.")
        nar("Le monde entier tremble. Vous avez empêché l'apocalypse.")
        nar("\n=== FIN: Le Sauveur Silencieux ===")
        rejouer()
    elif choix == "2": # Branche 1.3.2.2
        nar("\nLa cloche sonne. Le monde s'effondre dans les ténèbres.")
        nar("\n=== FIN : La fin de toute chose ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        observer_silhouette()

def catacombes(): # Branche principale 2
    nar("\nLes marches descendent dans l'obscurité totale.")
    nar("L'air est lourd, saturé de l'odeur de la décomposition.")
    nar("Des ossements jonchent le sol. Certains semblent récents.")
    nar("Vous entendez des grattements dans les murs.")

    print("\n(1) Suivre le bruit vers la gauche")
    print("(2) Prendre le couloir de droite")
    print("(3) Allumer une torche trouvée au sol")
    choix = input("\nQuel est votre choix? (1, 2 ou 3) : ")

    if choix == "1":
        suivre_bruit_gauche()
    elif choix == "2":
        couloir_droite()
    elif choix == "3":
        allumer_torche()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        catacombes()

def suivre_bruit_gauche(): # Branche 2.1
    nar("\nVous avancez à tâtons vers la source du grattement.")
    nar("Quelque chose vous frôle dans le noir.")
    nar("Des yeux rouges s'allument devant vous. Des dizaines de paires.")

    print("\n(1) Reculer lentement")
    print("(2) Rester immobile")
    print("(3) Crier pour les effrayer")
    choix = input("\nQuel est votre choix? (1, 2 ou 3) : ")

    if choix == "1": # Branche 2.1.1
        nar("\nVous reculez mais trébuchez. Les créatures se jettent sur vous.")
        nar("\n=== FIN: Dévoré dans les Ténèbres ===")
        rejouer()
    elif choix == "2": # Branche 2.1.2
        rester_immobile()
    elif choix == "3": # Branche 2.1.3
        nar("\nVotre cri les affole.")
        nar("Elles vous dévorent dans une frénésie sanguinaire.")
        nar("\n=== FIN: Dévoré dans les Ténèbres ===")
        rejouer()

def rester_immobile(): # Branche 2.1.2
    nar("\nLes créatures vous reniflent mais passent leur chemin, vous épargnant.")
    nar("Elles chassent autres choses dans les profondeurs.")

    print("\n(1) Les suivre discrètement")
    print("(2) Continuer dans l'autre direction")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        suivre_créatures()
    elif choix == "2": # Branche 2.1.2.2
        nar("\nVous trouvez une sortie vers la surface.")
        nar("\n=== FIN : L'évasion des catacombes ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        rester_immobile()

def suivre_créatures(): # Branche 2.1.2.1
    nar("\nVous découvrez leur nid")
    nar("Au centre, un oeuf pulsant d'énergie.")

    print("\n(1) Détruire l'oeuf")
    print("(2) Le prendre")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        nar("\nL'œuf explose en une lumière aveuglante.")
        nar("Les créatures hurlent et s'effondrent. Vous êtes libre.")
        nar("\n=== FIN: L'Exterminateur ===")
        rejouer()
    elif choix == "2":
        nar("\nL'œuf fusionne avec vous. Vous devenez leur nouvelle reine.")
        nar("\n=== FIN: La Métamorphose ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        suivre_créatures()

def couloir_droite(): # Branche 2.2
    nar("\nCe passage est tapissé de racines noires et pulsantes.")
    nar("Elles semblent vivantes, respirant lentement.")
    nar("Au bout du couloir, une faible lueur.")
    
    print("\n(1) Toucher les racines")
    print("(2) Avancer vers la lumière")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        nar("\nLes racines s'enroulent autour de vous et vous drainent.")
        nar("\n=== FIN : Absorbé par la corruption ===")
        rejouer()
    elif choix == "2":
        avancer_vers_lumière()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        couloir_droite()

def avancer_vers_lumière(): # Branche 2.2.2
    nar("\nLa lumière provient d'une crypte avec un sarcophage ouvert.")
    nar("À l'intérieur repose un cadavre momifié tenant une épée.")

    print("\n(1) Prendre l'épée")
    print("(2) Examiner le corps")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        prendre_épée()
    elif choix == "2": # Branche 2.2.2.2
        nar("\nVous trouvez un médaillon sur le corps avec une inscription.")
        nar("« La vérité est dans le sang. » Énigmatique.")
        nar("\n=== FIN: Le Mystère Non Résolu ===")
        rejouer()
    else: 
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        avancer_vers_lumière()
    

def prendre_épée(): # Branche 2.2.2.1
    nar("\nL'épée s'illumine dans votre main. Une puissance ancienne vous envahit.")
    nar("Mais elle exige un tribut. Votre âme.")

    print("\n(1) Accepter le prix")
    print("(2) Lâcher l'épée")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        nar("\nVous devenez un guerrier immortel mais sans conscience.")
        nar("\n=== FIN: Le Champion Sans Âme ===")
        rejouer()
    elif choix == "2":
        nar("\nVous lâchez l'épée et quittez la crypte indemne.")
        nar("\n=== FIN: La Résistance à la Tentation ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        prendre_épée()

def allumer_torche(): # Branche 2.3
    nar("\nLa flamme révèle l'horreur autour de vous.")
    nar("Les murs sont couverts d'inscriptions sanglantes.")
    nar("'FUYEZ' 'NE DESCENDEZ PAS' 'IL NOUS REGARDE'")

    print("\n(1) Continuer malgré l'avertissement")
    print("(2) Remonter immédiatement")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 2.3.1
        nar("\nVous descendez plus profondément.")
        nar("Une voix résonne : 'Enfin, de la compagnie...'")
        nar("Quelque chose d'immense se déplace dans l'obscurité.")
        nar("\n=== FIN : Face au déchiqueteur d'âmes ===")
        rejouer()
    elif choix == "2": # Branche 2.3.2
        nar("\nVous remontez, mais la torche s'éteint soudainement.")
        nar("Vous êtes plongé dans l'obscurité totale.")
        nar("Des griffes vous attrapent et vous traînent dans les ténèbres.")
        nar("\n=== FIN : Enlevé par les ombres ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        allumer_torche()

def brouillard(): # Branche principale 3
    nar("\nLe brouillard est si dense que vous ne voyez pas vos propres mains.")
    nar("Le sol sous vos pieds est mou, presque vivant.")
    nar("Des silhouettes se dessinent au loin, immobiles.")
    nar("Vous entendez des pleurs d'enfant quelque part.")

    print("\n(1) Suivre les pleurs")
    print("(2) Approcher les silhouettes")
    print("(3) Avancer droit devant")
    choix = input("\nQuel est votre choix? (1, 2 ou 3) : ")

    if choix == "1":
        suivre_pleurs()
    elif choix == "2":
        approcher_les_silhouettes()
    elif choix == "3":
        avancer_droit_devant()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        brouillard()

def suivre_pleurs(): # Branche 3.1
    nar("\nLes pleurs vous guident à travers le brouillard.")
    nar("Vous trouvez un enfant recroquevillé, le visage caché.")
    nar("Quelque chose semble... incorrect.")

    print("\n(1) S'approcher de l'enfant")
    print("(2) Lui parler doucement")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 3.1.1
        nar("\nL'enfant se retourne. Son visage est une bouche béante.")
        nar("Il vous dévore avant que vous ne puissiez réagir.")
        nar("\n=== FIN : Dévoré par l'innocence ===")
        rejouer()
    elif choix == "2":
        parler_enfant()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        suivre_pleurs()

def parler_enfant(): # Branche 3.1.2
    nar("\n« Aidez-moi...» pleure-t-il. Sa voix devient grave et monstrueuse.")
    nar("Il se transforme en une abomination.")

    print("\n(1) Combattre")
    print("(2) Fuir")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 3.1.2.1
        nar("\nVous luttez avec courage mais êtes submergé.")
        nar("\n=== FIN: Le Combat Héroïque ===")
        rejouer()
    elif choix == "2": # Branche 3.1.2.2
        nar("\nVous fuyez à travers le brouillard, laissant derrière vous les cris de l'abomination.")
        nar("\n=== FIN : La fuite dans le brouillard ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        parler_enfant()

def approcher_les_silhouettes(): # Branche 3.2
    nar("\nLes silhouettes sont des statues de pierre.")
    nar("Elles représentent des gens ordinaires, figés dans leur dernière seconde.")
    nar("L'une d'elles vous ressemble étrangement.")

    print("\n(1) Toucher votre statue")
    print("(2) Examiner les autres statues")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 3.2.1
        nar("\nVous touchez la statue. Une vision vous submerge.")
        nar("Vous voyez votre propre mort, encore et encore.")
        nar("Vous devenez fou de cette connaissance.")
        nar("\n=== FIN : La folie de la connaissance ===")
        rejouer()
    elif choix == "2":
        examiner_autres_statues()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        approcher_les_silhouettes()

def examiner_autres_statues(): # Branche 3.2.2
    nar("\nChaque statue raconte une histoire de désespoir.")
    nar("Vous trouvez un journal à leurs pieds.")

    print("\n(1) Lire le journal")
    print("(2) L'ignorer")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 3.2.2.1
        nar("\nLe journal révèle la vérité : vous êtes déjà mort.")
        nar("Ce monde est votre purgatoire personnel.")
        nar("\n=== FIN : La révélation du purgatoire ===")
        rejouer()
    elif choix == "2": # Branche 3.2.2.2
        nar("\nVous partez, préservant votre ignorance.")
        nar("\n=== FIN : L'ignorance est une bénédiction ===")
        rejouer()

def avancer_droit_devant(): # Branche 3.3
    nar("\nVous marchez pendant ce qui semble des heures.")
    nar("Le brouillard commence à se dissiper.")
    nar("Vous découvrez un village abandonné.")

    print("\n(1) Explorer le village")
    print("(2) Le contourner")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        explorer_village()
    elif choix == "2":
        contourner_village()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        avancer_droit_devant()

def explorer_village(): # Branche 3.3.1
    nar("\nLes maisons sont vides mais les tables sont mises.")
    nar("Comme si les habitants avaient disparu soudainement.")
    nar("Au centre du village, un puits.")

    print("\n(1) Regarder dans le puits")
    print("(2) Fouiller les maisons")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1":
        regarder_puits()
    elif choix == "2": # Branche 3.3.1.2
        nar("\nVous trouvez un journal parlant d'un rituel raté.")
        nar("Le village entier a été sacrifié à une entité.")
        nar("\n=== FIN : Le sacrifice du village ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        explorer_village()

def regarder_puits(): # Branche 3.3.1.1
    nar("\nDans le puits, vous voyez des centaines de visages hurlants.")
    nar("Ils vous appellent. Vous tendent les bras vers l'enfer.")

    print("\n(1) Sauter pour les rejoindre")
    print("(2) Reculer horrifié")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 3.3.1.1.1
        nar("\nVous plongez dans l'abîme. Les âmes vous accueillent.")
        nar("\n=== FIN : L'union avec les damnés ===")
        rejouer()
    elif choix == "2": # Branche 3.3.1.1.2
        nar("\nVous fuyez le village, hanté par cette vision.")
        nar("\n=== FIN : Le témoin terrifié ===")
        rejouer()
    else:
        print("Saisie invalide. Entrez le nombre correspondant à votre choix.")
        regarder_puits()

def contourner_village(): # Branche 3.3.2
    nar("\nVous contournez le village.")
    nar("Au loin, vous apercevez une lumière. Un espoir?")

    print("\n(1) Marcher vers la lumière")
    print("(2) Rester dans l'obscurité familière")
    choix = input("\nQuel est votre choix? (1 ou 2) : ")

    if choix == "1": # Branche 3.3.2.1
        nar("\nLa lumière grandit. C'est un portail vers un autre monde.")
        nar("Vous le franchissez et trouvez peut-être la paix.")
        nar("\n=== FIN : Le nouveau départ ===")
        rejouer()
    elif choix == "2": # Branche 3.3.2.2
        nar("\nVous restez dans ce monde de brume pour l'éternité.")
        nar("\n=== FIN : L'éternité dans le brouillard ===")
        rejouer()
    

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