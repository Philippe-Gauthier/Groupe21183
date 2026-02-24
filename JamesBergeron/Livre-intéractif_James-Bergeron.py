"""
Auteur: James Bergeron
Date: 2026-02-03
Description: Script Python pour le projet de livre interactif.
"""
from socket import close

class Page:
    # Initialisation d'une page avec un numéro, du texte et des choix
    def __init__(self, numero, texte_initial=""):
        self.numero = numero
        self.textes = []
        if texte_initial:
            self.textes.append(texte_initial)
        self.choix = {}
# Ajout de texte et de choix à une page
    def ajouter_texte(self, texte):
        self.textes.append(texte)
# Ajout d'un choix à une page, avec un code de choix, une description et la page suivante associée
    def ajouter_choix(self, code, description, page_suivante):
        self.choix[code] = {
            "description": description,
            "suivante": page_suivante
        }
# Affichage du contenu d'une page, y compris le texte et les choix disponibles
    def afficher(self):
        print(f"\n--- Page {self.numero} ---")
        for ligne in self.textes:
            print(ligne)
# Affichage des choix disponibles sur la page
        if self.choix:
            print("\nVos choix :")
            for code, info in self.choix.items():
                print(f"{code} - {info['description']}")
# Page de mon livres 1 à 94 (Désolé, je voulais que mon histoire soit complète)
if __name__ == "__main__":
        livre = {}

        page1 = Page(1)
page1.ajouter_texte("Le chemin non prévu.")
page1.ajouter_texte("Par James Bergeron")
page1.ajouter_texte("2026-02-03")
page1.ajouter_choix("enter", "Commencer l'histoire", 2)
livre[1] = page1

page2 = Page(2, "Situation initiale.")
page2.ajouter_texte("Shade est un jeune cartographe talentueux qui explore une île mystérieuse.")
page2.ajouter_texte("Il arrive devant une intersection du sentier, dont il suivait depuis plusieurs heures.")
page2.ajouter_texte("Il doit choisir entre deux chemins : l'un mène vers une forêt dense, l'autre vers une grotte sinueuse dans une montagne menant à un village inconnu.")
page2.ajouter_choix("a", "Prendre le chemin de la forêt dense", 3)
page2.ajouter_choix("b", "Prendre le chemin vers la grotte sinueuse", 4)
livre[2] = page2

page3 = Page(3, "Shade prend le chemin de la forêt dense.")
page3.ajouter_texte("Il marche pendant des heures, entouré par les arbres imposants et les bruits de la nature.")
page3.ajouter_texte("Il découvre un vieux temple abandonné.")
page3.ajouter_texte("Il doit décider s'il veut explorer le temple ou continuer à suivre le sentier dans la forêt.")
page3.ajouter_choix("a1", "Explorer le temple", 5)
page3.ajouter_choix("b1", "Continuer dans la forêt", 6)
livre[3] = page3

page4 = Page(4, "Shade prend le chemin de droite vers la grotte sinueuse.")
page4.ajouter_texte("Il arrive devant l'entrée de la grotte et il voit un sentier se dévoilant sur le côté de la montagne.")
page4.ajouter_texte("Il doit choisir s'il veut entrer dans la grotte ou suivre le sentier de montagne.")
page4.ajouter_choix("a3", "Entrer dans la grotte", 7)
page4.ajouter_choix("b3", "Suivre le sentier", 8)
livre[4] = page4

page5 = Page(5, "Shade décide d'explorer le temple abandonné.")
page5.ajouter_texte("À l'intérieur du temple, il trouve deux leviers mystérieux.")
page5.ajouter_texte("Il doit choisir lequel tirer pour découvrir les secrets du temple.")
page5.ajouter_choix("a4", "Tirer le levier gauche", 9)
page5.ajouter_choix("b4", "Tirer le levier droit", 10)
livre[5] = page5

page6 = Page(6, "Shade décide de continuer dans la forêt.")
page6.ajouter_texte("Il continue à marcher dans la forêt dense.")
page6.ajouter_texte("Il arrive devant une rivière large et rapide.")
page6.ajouter_texte("Il peut choisir de traverser la rivière à la nage ou chercher un pont pour la traverser.")
page6.ajouter_choix("a2", "Traverser la rivière à la nage", 11)
page6.ajouter_choix("b2", "Chercher un pont", 12)
livre[6] = page6

page7 = Page(7, "Shade entre dans la grotte.")
page7.ajouter_texte("À l'intérieur de la grotte, il fait sombre et il doit trouver un moyen de s'éclairer.")
page7.ajouter_texte("Il voit au loin un chariot de lanternes éteintes avec un vieux combustible à côté.")
page7.ajouter_texte("Il doit choisir s'il veut allumer une lanterne ou utiliser sa lampe de poche pour explorer la grotte.")
page7.ajouter_choix("a5", "Allumer une lanterne", 13)
page7.ajouter_choix("b5", "Utiliser la lampe de poche", 14)
livre[7] = page7

page8 = Page(8, "Shade décide de suivre le sentier de montagne.")
page8.ajouter_texte("Le sentier de montagne est escarpé et difficile à suivre.")
page8.ajouter_texte("Il arrive devant une paroi rocheuse infranchissable à pied, car le sentier a été détruit par un éboulement de roches.")
page8.ajouter_texte("Il doit choisir s'il veut contourner la paroi rocheuse avec du matériel d'escalade ou retourner en arrière pour trouver un autre chemin.")
page8.ajouter_choix("a6", "Contourner avec matériel d'escalade", 15)
page8.ajouter_choix("b6", "Retourner en arrière", 16)
livre[8] = page8

page9 = Page(9, "Shade décide de tirer le levier gauche.")
page9.ajouter_texte("En tirant le levier gauche, une porte secrète s'ouvre dans le mur du temple.")
page9.ajouter_texte("Il doit choisir s'il veut ouvrir la porte secrète ou rester dans la salle pour explorer davantage.")
page9.ajouter_choix("a7", "Entrer dans la porte secrète", 17)
page9.ajouter_choix("b7", "Rester dans la salle", 18)
livre[9] = page9

page10 = Page(10, "Shade décide de tirer le levier droit.")
page10.ajouter_texte("En tirant le levier droit, le sol tremble et un passage secret s'ouvre à ses pieds, le faisant tomber dans une glissade en pierre.")
page10.ajouter_texte("Il glisse dans un tunnel sombre et se retrouve dans une salle souterraine mystérieuse.")
page10.ajouter_texte("L'exploreur atterit dans une salle avec deux passages : l'un mène vers une lumière au loin, l'autre vers une obscurité totale.")
page10.ajouter_choix("a8", "Se diriger vers la lumière", 19)
page10.ajouter_choix("b8", "Se diriger vers l'obscurité", 20)
livre[10] = page10

page11 = Page(11, "Shade traverse la rivière à la nage.")
page11.ajouter_texte("La rivière est froide et rapide, mais Shade parvient à nager jusqu'à l'autre rive.")
page11.ajouter_texte("Il arrive de l'autre côté de la rivière et voit de vielles ruines d'une civilisation ancienne.")
page11.ajouter_texte("Il doit choisir s'il veut explorer les ruines ou chercher un autre chemin à travers la forêt.")
page11.ajouter_choix("a9", "Explorer les ruines", 21)
page11.ajouter_choix("b9", "S'aventurer dans la forêt", 22)
livre[11] = page11

page12 = Page(12, "Shade cherche un pont afin de traverser la rivière.")
page12.ajouter_texte("Après avoir marché le long de la rivière, Shade trouve un vieux pont en bois qui semble encore solide.")
page12.ajouter_texte("Il doit choisir s'il veut traverser le pont ou retourner en arrière pour trouver un autre chemin à travers la forêt.")
page12.ajouter_choix("a10", "Traverser le pont", 23)
page12.ajouter_choix("b10", "Retourner en arrière", 24)
livre[12] = page12

page13 = Page(13, "Shade allume une lanterne avec le vieux combustible.")
page13.ajouter_texte("La lanterne s'allume et éclaire la grotte d'une lumière chaude et vacillante.")
page13.ajouter_texte("Il voit des inscriptions anciennes sur les murs de la grotte, révélant des secrets sur l'île mystérieuse.")
page13.ajouter_texte("Il doit choisir s'il veut explorer la grotte plus en profondeur ou rester à l'entrée pour étudier les inscriptions.")
page13.ajouter_choix("a11", "Explorer la grotte en profondeur", 25)
page13.ajouter_choix("b11", "Rester à l'entrée pour étudier les inscriptions", 26)
livre[13] = page13

page14 = Page(14, "Shade décide d'utiliser la lampe de poche.")
page14.ajouter_texte("La lampe de poche éclaire les passages sombres de la grotte.")
page14.ajouter_texte("Il voit des stalactites et des stalagmites impressionnantes, ainsi que des peintures rupestres anciennes sur les murs.")
page14.ajouter_texte("Il doit choisir s'il veut explorer la grotte plus en profondeur ou rester à l'entrée pour étudier les peintures rupestres.")
page14.ajouter_choix("a12", "Explorer la grotte en profondeur", 27)
page14.ajouter_choix("b12", "Rester à l'entrée pour étudier les peintures rupestres", 28)
livre[14] = page14

page15 = Page(15, "Shade contourne le sentier détruit avec son matériel d'escalade pour continuer à suivre le sentier plus loin.")
page15.ajouter_texte("Il parvient à contourner la paroi rocheuse et continue à suivre le sentier de montagne.")
page15.ajouter_texte("Il continue à marcher le long du sentier escarpé et s'approche du village inconnu au loin.")
page15.ajouter_texte("Shade soudainement trouve une vieille plume d'oiseau sur la roche du sentier.")
page15.ajouter_texte("Il doit choisir s'il veut ramasser la plume d'oiseau ou l'ignorer et continuer à suivre le sentier vers le village.")
page15.ajouter_choix("a13", "Ramasser la plume d'oiseau", 29)
page15.ajouter_choix("b13", "Ignorer la plume et continuer", 30)
livre[15] = page15

page16 = Page(16, "Shade retourne en arrière à l'entrée de la grotte.")
page16.ajouter_texte("Il décide de rentrer dans la grotte pour trouver un autre chemin à travers la montagne.")
page16.ajouter_texte("Il arrive à une intersection dans la grotte, avec deux tunnels différents devant lui.")
page16.ajouter_choix("a14", "Prendre le chemin de gauche vers un vieux mécanisme ressemblant à une ascenseur", 31)
page16.ajouter_choix("b14", "Prendre le chemin de droite et suivre les empreintes de pas", 32)
livre[16] = page16

page17 = Page(17, "Shade décide d'entrer dans la pièce secrète derrière la porte du temple.")
page17.ajouter_texte("En entrant dans la pièce secrète, Shade découvre une salle remplie de trésors anciens et d'artefacts mystérieux.")
page17.ajouter_texte("Il peut soit voler une partie du trésor pour lui-même, soit laisser le trésor intact et continuer à explorer la pièce secrète.")
page17.ajouter_choix("a15", "Voler une partie du trésor", 33)
page17.ajouter_choix("b15", "Laisser le trésor intact et continuer à explorer", 34)
livre[17] = page17

page18 = Page(18, "Shade investige la salle avec les deux passages.")
page18.ajouter_texte("Il remarque une ombre étrange sur le mur de la salle, qui semble se déplacer lentement.")
page18.ajouter_texte("Il peut soit s'excuser à l'ombre et essayer de communiquer avec elle, soit attaquer l'ombre.")
page18.ajouter_choix("a16", "S'excuser à l'ombre et essayer de communiquer avec elle", 35)
page18.ajouter_choix("b16", "Attaquer l'ombre", 36)
livre[18] = page18

page19 = Page(19, "Shade décide de prendre le passage lumineux.")
page19.ajouter_texte("Tout à coup, un mûr de roche ferme l'entrée du passage lumineux derrière lui, le piégeant dans la salle souterraine.")
page19.ajouter_texte("Shade voit de la lave couler lentement dans la salle souterraine, se rapprochant de lui.")
page19.ajouter_texte("Il peut essayer de miner le mûr bloquant le passage lumineux pour s'échapper ou rester dans la salle et attendre que la lave l'atteigne.")
page19.ajouter_choix("a17", "Essayer de miner le mur", 37)
page19.ajouter_choix("b17", "Rester dans la salle et attendre que la lave l'atteigne", 38)
livre[19] = page19

page20 = Page(20, "Shade reste dans la salle et prends le passage plongé dans l'obscurité.")
page20.ajouter_texte("En prenant le passage plongé dans l'obscurité, Shade se retrouve dans une salle sombre et silencieuse.")
page20.ajouter_texte("Puis, les mûrs commencent à trembler tellement fort que des morceaux de roche tombent du plafond, menaçant de l'écraser.")
page20.ajouter_texte("Tout d'un coup, le passage s'ouvre montrant l'extérieur et aveuglant Shade avec la lumière du soleil.")
page20.ajouter_texte("Il se retrouve à l'extérieur et une drôle de boule de roche tombe sur le sol à côté de lui.")
page20.ajouter_texte("Il doit choisir s'il veut ramasser la boule de roche ou l'ignorer et s'avancer ver le village.")
page20.ajouter_choix("a18", "Ramasser la boule de roche et s'avancer vers le village", 39)
page20.ajouter_choix("b18", "Ignorer la boule de roche et s'avancer vers le village", 40)
livre[20] = page20

page21 = Page(21, "Shade décide d'explorer les ruines de la civilisation ancienne.")
page21.ajouter_texte("En explorant les ruines, Shade découvre des artefacts anciens et des inscriptions mystérieuses qui révèlent des secrets sur l'île.")
page21.ajouter_texte("Il se fait prendre au piège dans les ruines par le peuple inconnu du village.")
page21.ajouter_texte("Il peut essayer de s'excuser auprès du peuple inconnu pour éviter d'être capturé ou essayer de s'échapper en courant à travers les ruines.")
page21.ajouter_choix("a19", "S'excuser auprès du peuple inconnu", 41)
page21.ajouter_choix("b19", "Essayer de s'échapper en courant à travers les ruines", 42)
livre[21] = page21

page22 = Page(22, "Shade décide de s'aventurer dans la forêt au lieu d'explorer les ruines.")
page22.ajouter_texte("En s'aventurant dans la forêt, Shade découvre des plantes et des animaux étranges, ainsi que des sons mystérieux qui résonnent à travers les arbres.")
page22.ajouter_texte("Puis, il se fait surprendre par le peuple inconnu du village qui le capture et l'emmène dans leur village.")
page22.ajouter_texte("Shade peut essayer de s'excuser auprès du peuple inconnu pour éviter d'être capturé ou essayer de s'échapper en courant à travers la forêt.")
page22.ajouter_choix("a20", "S'excuser auprès du peuple inconnu", 43)
page22.ajouter_choix("b20", "Essayer de s'échapper en courant à travers la forêt", 44)
livre[22] = page22

page23 = Page(23, "Shade décide de traverser le pont en bois.")
page23.ajouter_texte("En traversant le pont, Shade entend des craquements inquiétants sous ses pieds.")
page23.ajouter_texte("Soudainement, le pont s'effondre et Shade tombe dans la rivière en contrebas.")
page23.ajouter_texte("Il se débat dans l'eau froide et rapide, essayant de nager vers la rive.")
page23.ajouter_texte("Il doit choisir s'il veut nager vers la rive ou essayer de se laisser porter par le courant pour trouver un endroit plus calme.")
page23.ajouter_choix("a21", "Nager vers la rive", 45)
page23.ajouter_choix("b21", "Se laisser porter par le courant", 46)
livre[23] = page23

page24 = Page(24, "Shade décide de retourner en arrière pour trouver un autre chemin à travers la forêt.")
page24.ajouter_texte("En retournant en arrière, Shade se perd dans la forêt dense et ne parvient pas à retrouver le sentier.")
page24.ajouter_texte("Une créature mystérieuse commence à le suivre dans la forêt, émettant des bruits étranges et inquiétants.")
page24.ajouter_texte("Il peut continuer à marcher ou commencer à courir le plus vite possible.")
page24.ajouter_choix("a22", "Continuer à marcher", 47)
page24.ajouter_choix("b22", "Commencer à courir", 48)
livre[24] = page24

page25 = Page(25, "Shade décide d'explorer la grotte en profondeur après avoir allumé la lanterne.")
page25.ajouter_texte("En explorant la grotte en profondeur, Shade découvre une salle secrète remplie de trésors anciens et d'artefacts mystérieux.")
page25.ajouter_texte("Il peut soit voler une partie du trésor pour lui-même, soit laisser le trésor intact et continuer à explorer la salle secrète.")
page25.ajouter_choix("a23", "Voler une partie du trésor", 49)
page25.ajouter_choix("b23", "Laisser le trésor intact   et continuer à explorer", 50)
livre[25] = page25

page26 = Page(26, "Shade décide de rester à l'entrée de la grotte pour étudier les inscriptions après avoir allumé la lanterne.")
page26.ajouter_texte("En étudiant les inscriptions, Shade découvre des informations précieuses sur l'histoire de l'île mystérieuse et les secrets qu'elle recèle.")
page26.ajouter_texte("Il se fait capturer par des scouts du peuple inconnu du village qui le prennent pour un intrus.")
page26.ajouter_texte("Il peut essayer de s'excuser auprès du peuple inconnu pour éviter d'être capturé ou essayer de s'échapper en courant à travers la grotte.")
page26.ajouter_choix("a24", "S'excuser auprès du peuple inconnu", 51)
page26.ajouter_choix("b24", "Essayer de s'échapper en courant à travers la grotte", 52)
livre[26] = page26

page27 = Page(27, "Shade décide d'explorer la grotte en profondeur après avoir utilisé sa lampe de poche.")
page27.ajouter_texte("En explorant la grotte en profondeur, sa lampe s'éteint soudainement, le laissant dans l'obscurité totale.")
page27.ajouter_texte("Il entend des bruits étranges et inquiétants résonner à travers la grotte, ce qui le rend encore plus nerveux dans l'obscurité.")
page27.ajouter_texte("Il doit trouver un moyen de rallumer sa lampe de poche ou trouver une autre source de lumière pour continuer à explorer la grotte.")
page27.ajouter_choix("a25", "Essayer de rallumer la lampe de poche", 53)
page27.ajouter_choix("b25", "Chercher une autre source de lumière", 54)
livre[27] = page27

page28 = Page(28, "Shade décide de rester à l'entrée de la grotte pour étudier les peintures rupestres après avoir utilisé sa lampe de poche.")
page28.ajouter_texte("En étudiant les peintures rupestres, Shade découvre des informations précieuses sur l'histoire de l'île mystérieuse et les secrets qu'elle recèle.")
page28.ajouter_texte("Il se fait capturer par des scouts du peuple inconnu du village qui le prennent pour un intrus.")
page28.ajouter_texte("Il peut essayer de s'excuser auprès du peuple inconnu pour éviter d'être capturé ou essayer de s'échapper en courant à travers la grotte.")
page28.ajouter_choix("a26", "S'excuser auprès du peuple inconnu", 55) 
page28.ajouter_choix("b26", "Essayer de s'échapper en courant à travers la grotte", 56)
livre[28] = page28

page29 = Page(29, "Shade décide de ramasser la plume d'oiseau trouvée sur le sentier de montagne.")
page29.ajouter_texte("En ramassant la plume d'oiseau, Shade découvre que la plume est en fait un artefact ancien.")
page29.ajouter_texte("Il continu de marcher sur le sentier et arrive au village inconnu, où il est accueilli par les habitants du village qui le prennent pour un héros.")
page29.ajouter_texte("Le peuple le remerci pour avoir trouvé l'artefact ancien et lui offre une place d'honneur dans leur village.")
page29.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page29.ajouter_choix("a27", "Accepter l'offre du peuple inconnu et rester dans le village", 57)
page29.ajouter_choix("b27", "Refuser l'offre et continuer à explorer l'île mystérieuse", 58)
livre[29] = page29

page30 = Page(30, "Shade décide d'ignorer la plume d'oiseau trouvée sur le sentier de montagne et continue à suivre le sentier vers le village.")
page30.ajouter_texte("En continuant à suivre le sentier, Shade arrive au village inconnu, où il est capturé par les habitants du village qui le prennent pour un intrus.")
page30.ajouter_texte("Il peut essayer de s'excuser auprès du peuple inconnu pour éviter d'être capturé ou essayer de s'échapper en courant à travers le village.")
page30.ajouter_choix("a28", "S'excuser auprès du peuple inconnu", 59)
page30.ajouter_choix("b28", "Essayer de s'échapper en courant à travers le village", 60)
livre[30] = page30

page31 = Page(31, "Shade décide de prendre le chemin de gauche vers un vieux mécanisme ressemblant à une ascenseur dans la grotte.")
page31.ajouter_texte("En prenant le chemin de gauche, Shade découvre un vieux mécanisme ressemblant à une ascenseur.")
page31.ajouter_texte("Puis, l'ascenseur s'active, mais il est instable et commence à tomber rapidement dans un puits sombre.")
page31.ajouter_texte("Il doit essayer de ralentir la chute en utilisant les parois du puits ou se laisser tomber et espérer atterrir sur quelque chose de mou.")
page31.ajouter_choix("a29", "Essayer de ralentir la chute en utilisant les parois du puits", 61)
page31.ajouter_choix("b29", "Se laisser tomber et espérer atterrir sur quelque chose de mou", 62)
livre[31] = page31

page32 = Page(32, "Shade décide de prendre le chemin de droite et suivre les empreintes de pas dans la grotte.")
page32.ajouter_texte("En prenant le chemin de droite, Shade suit les empreintes de pas à travers la grotte, qui le mènent à une salle secrète remplie de trésors anciens et d'artefacts mystérieux.")
page32.ajouter_texte("Il peut soit voler une partie du trésor pour lui-même, soit laisser le trésor intact et continuer à explorer la salle secrète.")
page32.ajouter_choix("a30", "Voler une partie du trésor", 63)
page32.ajouter_choix("b30", "Laisser le trésor intact et continuer à explorer", 64)
livre[32] = page32

page33 = Page(33, "Shade décide de voler une partie du trésor dans la salle secrète du temple.")
page33.ajouter_texte("En volant une partie du trésor, Shade déclenche un piège qui libère une créature gardienne du trésor.")
page33.ajouter_texte("La créature attaque Shade, qui doit choisir s'il veut se défendre en combattant la créature ou essayer de s'échapper en courant à travers le temple.")
page33.ajouter_choix("a31", "Se défendre en combattant la créature", 65)
page33.ajouter_choix("b31", "Essayer de s'échapper en courant à travers le temple", 66)
livre[33] = page33

page34 = Page(34, "Shade décide de laisser le trésor intact et continuer à explorer la salle secrète du temple.")
page34.ajouter_texte("En laissant le trésor intact, Shade se fait transporter au village inconnu par une force mystérieuse.")
page34.ajouter_texte("Il est accueilli par les habitants du village qui le prennent pour un héros en raison de sa découverte du temple.")
page34.ajouter_texte("Le peuple le remercie pour avoir découvert le temple et lui offre une place d'honneur dans leur village.")
page34.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page34.ajouter_choix("a32", "Accepter l'offre du peuple inconnu et rester dans le village", 67)
page34.ajouter_choix("b32", "Refuser l'offre et continuer à explorer l'île mystérieuse", 68)
livre[34] = page34

page35 = Page(35, "Shade décide de s'excuser à l'ombre et essayer de communiquer avec elle dans la salle souterraine.")
page35.ajouter_texte("En s'excusant à l'ombre, Shade découvre que l'ombre est en fait un esprit protecteur de l'île mystérieuse.")
page35.ajouter_texte("L'esprit lui révèle des secrets sur l'île et lui offre son aide pour naviguer à travers les dangers de l'île.")
page35.ajouter_texte("Il peut choisir d'accepter l'aide de l'esprit protecteur ou refuser l'aide et continuer à explorer l'île par lui-même.")
page35.ajouter_choix("a33", "Accepter l'aide de l'esprit protecteur", 69)
page35.ajouter_choix("b33", "Refuser l'aide et continuer à explorer l'île par lui-même", 70)
livre[35] = page35

page36 = Page(36, "Shade décide d'attaquer l'ombre dans la salle souterraine.")
page36.ajouter_texte("En attaquant l'ombre, Shade découvre que l'ombre est en fait un esprit protecteur de l'île mystérieuse.")
page36.ajouter_texte("L'esprit se défend contre l'attaque de Shade et le combat devient de plus en plus intense.")
page36.ajouter_texte("Finalement, Shade ne parvient pas à vaincre l'esprit et est gravement blessé dans le combat.")
page36.ajouter_texte("Il doit choisir s'il veut continuer à se battre contre l'esprit ou essayer de s'échapper en courant à travers la salle souterraine.")
page36.ajouter_choix("a34", "Continuer à se battre contre l'esprit", 71)
page36.ajouter_choix("b34", "Essayer de s'échapper en courant à travers la salle souterraine", 72)
livre[36] = page36

page37 = Page(37, "Shade décide d'essayer de miner le mur bloquant le passage lumineux dans la salle souterraine.")
page37.ajouter_texte("En essayant de miner le mur, Shade découvre que le mur est en fait une paroi de roche solide et il ne parvient pas à le miner.")
page37.ajouter_texte("La lave continue de se rapprocher de lui, menaçant de l'atteindre.")
page37.ajouter_texte("Il doit choisir s'il veut continuer à essayer de miner le mur ou essayer de trouver une autre solution pour s'échapper de la salle souterraine.")
page37.ajouter_choix("a35", "Continuer à essayer de miner le mur", 73)
page37.ajouter_choix("b35", "Essayer de trouver une autre solution pour s'échapper de la salle souterraine", 74)
livre[37] = page37

page38 = Page(38, "Shade décide de rester dans la salle souterraine et attendre que la lave l'atteigne.")
page38.ajouter_texte("En restant dans la salle souterraine, Shade est finalement atteint par la lave et meurt dans la salle souterraine.")
page38.ajouter_texte("Fin de l'histoire.")
livre[38] = page38

page39 = Page(39, "Shade décide de ramasser la boule de roche trouvée à l'extérieur de la grotte.")
page39.ajouter_texte("En ramassant la boule de roche, Shade découvre que la boule de roche est en fait un artefact ancien.")
page39.ajouter_texte("Il continue à marcher vers le village inconnu, où il est accueilli par les habitants du village qui le prennent pour un héros en raison de sa découverte de l'artefact ancien.")
page39.ajouter_texte("Le peuple le remercie pour avoir trouvé l'artefact ancien et lui offre une place d'honneur dans leur village.")
page39.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page39.ajouter_choix("a36", "Accepter l'offre du peuple inconnu et rester dans le village", 75)
page39.ajouter_choix("b36", "Refuser l'offre et continuer à explorer l'île mystérieuse", 76)
livre[39] = page39

page40 = Page(40, "Shade décide d'ignorer la boule de roche trouvée à l'extérieur de la grotte et s'avance vers le village.")
page40.ajouter_texte("En continuant à avancer vers le village, Shade arrive au village inconnu, où il est capturé par les habitants du village qui le prennent pour un intrus.")
page40.ajouter_texte("Il peut essayer de s'excuser auprès du peuple inconnu pour éviter d'être capturé ou essayer de s'échapper en courant à travers le village.")
page40.ajouter_choix("a37", "S'excuser auprès du peuple inconnu", 77)
page40.ajouter_choix("b37", "Essayer de s'échapper en courant à travers le village", 78)
livre[40] = page40

page41 = Page(41, "Shade décide de s'excuser auprès du peuple inconnu pour éviter d'être capturé dans les ruines.")
page41.ajouter_texte("En s'excusant auprès du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page41.ajouter_texte("Le peuple inconnu accepte les excuses de Shade et lui offre une place d'honneur dans leur village.")
page41.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page41.ajouter_choix("a38", "Accepter l'offre du peuple inconnu et rester dans le village", 79)
page41.ajouter_choix("b38", "Refuser l'offre et continuer à explorer l'île mystérieuse", 80)
livre[41] = page41

page42 = Page(42, "Shade décide d'essayer de s'échapper en courant à travers les ruines.")
page42.ajouter_texte("En essayant de s'échapper en courant à travers les ruines, Shade est finalement capturé par le peuple inconnu du village.")
page42.ajouter_texte("Le peuple inconnu ne prend pas de pitié pour Shade et le condamne à être emprisonné dans une cage en bois dans le village.")
page42.ajouter_texte("Fin de l'histoire.")
livre[42] = page42

page43 = Page(43, "Shade décide de s'excuser auprès du peuple inconnu pour éviter d'être capturé dans la forêt.")
page43.ajouter_texte("En s'excusant auprès du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page43.ajouter_texte("Le peuple inconnu accepte les excuses de Shade et lui offre une place d'honneur dans leur village.")
page43.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page43.ajouter_choix("a39", "Accepter l'offre du peuple inconnu et rester dans le village", 81)
page43.ajouter_choix("b39", "Refuser l'offre et continuer à explorer l'île mystérieuse", 82)
livre[43] = page43

page44 = Page(44, "Shade décide d'essayer de s'échapper en courant à travers la forêt.")
page44.ajouter_texte("En essayant de s'échapper en courant à travers la forêt, Shade est finalement capturé par le peuple inconnu du village.")
page44.ajouter_texte("Le peuple inconnu ne prend pas de pitié pour Shade et le condamne à être emprisonné dans une cage en bois dans le village.")
page44.ajouter_texte("Fin de l'histoire.")
livre[44] = page44

page45 = Page(45, "Shade décide de nager vers la rive après que le pont en bois s'effondre.")
page45.ajouter_texte("En nageant vers la rive, Shade ne parvient pas à atteindre la rive en toute sécurité, car un animal marin l'attaque.")
page45.ajouter_texte("Il essaye de se sauver de l'attaque de l'animal marin, mais il est finalement submergé et meurt dans la rivière.")
page45.ajouter_texte("Fin de l'histoire.")
livre[45] = page45

page46 = Page(46, "Shade décide de se laisser porter par le courant après que le pont en bois s'effondre.")
page46.ajouter_texte("En se laissant porter par le courant, il échappe à l'attaque de l'animal marin, car une vague le pousse loin de l'animal marin et le sauve de l'attaque.")
page46.ajouter_texte("En se laissant porter par le courant, Shade trouve un endroit plus calme de la rivière et parvient à atteindre la rive en toute sécurité.")
page46.ajouter_texte("Il arrive au village inconnu, où il est accueilli par les habitants du village qui le prennent pour un héros en raison de sa survie à l'attaque de l'animal marin.")
page46.ajouter_texte("Le peuple le félicite pour avoir survécu à l'attaque de l'animal marin et lui offre une place d'honneur dans leur village.")
page46.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page46.ajouter_choix("a40", "Accepter l'offre du peuple inconnu et rester dans le village", 83)
page46.ajouter_choix("b40", "Refuser l'offre et continuer à explorer l'île mystérieuse", 84)
livre[46] = page46

page47 = Page(47, "Shade décide de continuer à marcher malgré la créature mystérieuse qui le suit dans la forêt.")
page47.ajouter_texte("En continuant à marcher, Shade se fait blesser par la créature mystérieuse, qui le rattrape et le capture.")
page47.ajouter_texte("Le peuple inconnu du village ne prend pas de pitié pour Shade et le condamne à être emprisonné dans une cage en bois dans le village.")
page47.ajouter_texte("Fin de l'histoire.")
livre[47] = page47

page48 = Page(48, "Shade décide de commencer à courir le plus vite possible malgré la créature mystérieuse qui le suit dans la forêt.")
page48.ajouter_texte("En commençant à courir, Shade parvient à semer la créature mystérieuse dans la forêt et trouve un endroit sûr pour se cacher.")
page48.ajouter_texte("Il continue à courir à travers la forêt et arrive au village inconnu, où il est accueilli par les habitants du village qui le prennent pour un héros en raison de sa survie à l'attaque de la créature mystérieuse.")
page48.ajouter_texte("Le peuple le félicite pour avoir survécu à l'attaque de la créature mystérieuse et lui offre une place d'honneur dans leur village.")
page48.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page48.ajouter_choix("a41", "Accepter l'offre du peuple inconnu et rester dans le village", 85)
page48.ajouter_choix("b41", "Refuser l'offre et continuer à explorer l'île mystérieuse", 86)
livre[48] = page48

page49 = Page(49, "Shade décide de voler une partie du trésor dans la salle secrète de la grotte.")
page49.ajouter_texte("En volant une partie du trésor, Shade déclenche un piège qui libère une créature gardienne du trésor.")
page49.ajouter_texte("La créature attaque Shade et le combat devient de plus en plus intense.")
page49.ajouter_texte("Finalement, Shade ne parvient pas à vaincre la créature et est gravement blessé dans le combat.")
page49.ajouter_texte("Il doit choisir s'il veut continuer à se battre contre la créature ou essayer de s'échapper en courant à travers la salle secrète.")  
page49.ajouter_choix("a42", "Continuer à se battre contre la créature", 87)
page49.ajouter_choix("b42", "Essayer de s'échapper en courant à travers la salle secrète", 88)
livre[49] = page49

page50 = Page(50, "Shade décide de laisser le trésor intact et continuer à explorer la salle secrète de la grotte.")
page50.ajouter_texte("En laissant le trésor intact, Shade se fait transporter au village inconnu par une force mystérieuse.")
page50.ajouter_texte("Il est accueilli par les habitants du village qui le prennent pour un héros en raison de sa découverte de la salle secrète.")
page50.ajouter_texte("Le peuple le remercie pour avoir découvert la salle secrète et lui offre une place d'honneur dans leur village.")
page50.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page50.ajouter_choix("a43", "Accepter l'offre du peuple inconnu et rester dans le village", 89)
page50.ajouter_choix("b43", "Refuser l'offre et continuer à explorer l'île mystérieuse", 90)
livre[50] = page50

page51 = Page(51, "Shade décide de s'excuser auprès du peuple inconnu pour éviter d'être capturé dans la grotte.")
page51.ajouter_texte("En s'excusant auprès du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page51.ajouter_texte("Le peuple inconnu accepte les excuses de Shade et lui offre une place d'honneur dans leur village.")
page51.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page51.ajouter_choix("a44", "Accepter l'offre du peuple inconnu et rester dans le village", 91)
page51.ajouter_choix("b44", "Refuser l'offre et continuer à explorer l'île mystérieuse", 92)
livre[51] = page51

page52 = Page(52, "Shade décide d'essayer de s'échapper en courant à travers la grotte.")
page52.ajouter_texte("En essayant de s'échapper en courant à travers la grotte, Shade est finalement capturé par le peuple inconnu du village.")
page52.ajouter_texte("Le peuple inconnu ne prend pas de pitié pour Shade et le condamne à être emprisonné dans une cage en bois dans le village.")
page52.ajouter_texte("Fin de l'histoire.")  
livre[52] = page52

page53 = Page(53, "Shade décide d'essayer de rallumer sa lampe de poche dans la grotte.")
page53.ajouter_texte("En essayant de rallumer sa lampe de poche, Shade découvre que les piles de sa lampe de poche sont mortes et il ne parvient pas à rallumer la lampe de poche.")
page53.ajouter_texte("Il se fait attaquer par des créatures mystérieuses dans la grotte.")
page53.ajouter_texte("Il se fait submerger par les créatures mystérieuses et meurt dans la grotte.")
page53.ajouter_texte("Fin de l'histoire.")
livre[53] = page53

page54 = Page(54, "Shade décide de chercher une autre source de lumière dans la grotte.")
page54.ajouter_texte("En cherchant une autre source de lumière, Shade se fait attaquer par des créatures mystérieuses dans la grotte.")
page54.ajouter_texte("Il se fait submerger par les créatures mystérieuses et meurt dans la grotte.")
page54.ajouter_texte("Fin de l'histoire.")
livre[54] = page54

page55 = Page(55, "Shade décide de s'excuser auprès du peuple inconnu pour éviter d'être capturé dans la grotte après avoir étudié les peintures rupestres.")
page55.ajouter_texte("En s'excusant auprès du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page55.ajouter_texte("Le peuple inconnu accepte les excuses de Shade et lui offre une place d'honneur dans leur village.")
page55.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page55.ajouter_choix("a45", "Accepter l'offre du peuple inconnu et rester dans le village", 93)
page55.ajouter_choix("b45", "Refuser l'offre et continuer à explorer l'île mystérieuse", 94)
livre[55] = page55

page56 = Page(56, "Shade décide d'essayer de s'échapper en courant à travers la grotte après avoir étudié les peintures rupestres.")
page56.ajouter_texte("En essayant de s'échapper en courant à travers la grotte, Shade est finalement capturé par le peuple inconnu du village.")
page56.ajouter_texte("Le peuple inconnu ne prend pas de pitié pour Shade et le condamne à être emprisonné dans une cage en bois dans le village.")
page56.ajouter_texte("Fin de l'histoire.") 
livre[56] = page56

page57 = Page(57, "Shade décide d'accepter l'offre du peuple inconnu et de rester dans le village.")
page57.ajouter_texte("En acceptant l'offre du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page57.ajouter_texte("Shade s'intègre dans le village et devient un membre respecté de la communauté.")
page57.ajouter_texte("Il vit heureux dans le village inconnu et découvre des secrets sur l'île mystérieuse grâce à sa nouvelle vie dans le village.")
page57.ajouter_texte("Fin de l'histoire.")
livre[57] = page57

page58 = Page(58, "Shade décide de refuser l'offre du peuple inconnu et de continuer à explorer l'île mystérieuse.")
page58.ajouter_texte("En refusant l'offre du peuple inconnu, Shade continue à explorer l'île mystérieuse et découvre de nouveaux secrets et de nouvelles aventures.")
page58.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse et découvre des trésors cachés et des mystères anciens.")
page58.ajouter_texte("Fin de l'histoire.")
livre[58] = page58

page59 = Page(59, "Shade décide de s'excuser auprès du peuple inconnu pour éviter d'être capturé dans le village.")
page59.ajouter_texte("En s'excusant auprès du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page59.ajouter_texte("Le peuple inconnu accepte les excuses de Shade et lui offre une place d'honneur dans leur village.")
page59.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page59.ajouter_choix("a46", "Accepter l'offre du peuple inconnu et rester dans le village", 95)
page59.ajouter_choix("b46", "Refuser l'offre et continuer à explorer l'île mystérieuse", 96)
livre[59] = page59

page60 = Page(60, "Shade décide d'essayer de s'échapper en courant à travers le village.")
page60.ajouter_texte("En essayant de s'échapper en courant à travers le village, Shade est finalement capturé par le peuple inconnu du village.")
page60.ajouter_texte("Le peuple inconnu ne prend pas de pitié pour Shade et le condamne à être emprisonné dans une cage en bois dans le village.")
page60.ajouter_texte("Fin de l'histoire.")  
livre[60] = page60

page61 = Page(61, "Shade décide d'essayer de ralentir la chute en utilisant les parois du puits.")
page61.ajouter_texte("En essayant de ralentir la chute, Shade ne parvient pas à ralentir la chute et tombe dans le puits sombre, sur des pierres tranchantes qui le blessent gravement.")
page61.ajouter_texte("Finalement, Shade meurt de ses blessures dans le puits sombre.")
page61.ajouter_texte("Fin de l'histoire.")
livre[61] = page61

page62 = Page(62, "Shade décide de se laisser tomber et espérer atterrir sur quelque chose de mou.")
page62.ajouter_texte("En se laissant tomber, Shade atterrit sur un tas de pics de roche pointus qui le blessent gravement.")
page62.ajouter_texte("Finalement, Shade meurt de ses blessures dans le puits sombre.")
page62.ajouter_texte("Fin de l'histoire.") 
livre[62] = page62

page63 = Page(63, "Shade décide de voler une partie du trésor dans la salle secrète de la grotte.")
page63.ajouter_texte("En volant une partie du trésor, Shade déclenche un piège qui libère une créature gardienne du trésor.")
page63.ajouter_texte("La créature attaque Shade et le combat devient de plus en plus intense.")
page63.ajouter_texte("Finalement, Shade ne parvient pas à vaincre la créature et est gravement blessé dans le combat.")
page63.ajouter_texte("Il succombe à ses blessures dans la salle secrète de la grotte.")
page63.ajouter_texte("Fin de l'histoire.")  
livre[63] = page63

page64 = Page(64, "Shade décide de laisser le trésor intact et continuer à explorer la salle secrète de la grotte.")
page64.ajouter_texte("En laissant le trésor intact, Shade se fait transporter au village inconnu par une force mystérieuse.")
page64.ajouter_texte("Il est accueilli par les habitants du village qui le prennent pour un héros en raison de sa découverte de la salle secrète.")
page64.ajouter_texte("Le peuple le remercie pour avoir découvert la salle secrète et lui offre une place d'honneur dans leur village.")
page64.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page64.ajouter_choix("a47", "Accepter l'offre du peuple inconnu et rester dans le village", 97)
page64.ajouter_choix("b47", "Refuser l'offre et continuer à explorer l'île mystérieuse", 98)
livre[64] = page64

page65 = Page(65, "Shade décide de se défendre en combattant la créature gardienne du trésor dans la salle secrète du temple.")
page65.ajouter_texte("En se défendant en combattant la créature gardienne du trésor, Shade ne parvient pas à vaincre la créature et à s'emparer du trésor.")
page65.ajouter_texte("La créature gardienne du trésor le blesse gravement dans le combat et Shade meurt de ses blessures dans la salle secrète du temple.")
page65.ajouter_texte("Fin de l'histoire.")
livre[65] = page65

page66 = Page(66, "Shade décide d'essayer de s'échapper en courant à travers le temple.")
page66.ajouter_texte("En essayant de s'échapper en courant à travers le temple, Shade est finalement capturé par le peuple inconnu du village.")
page66.ajouter_texte("Le peuple inconnu ne prend pas de pitié pour Shade et le condamne à être emprisonné dans une cage en bois dans le village.")
page66.ajouter_texte("Fin de l'histoire.")
livre[66] = page66

page67 = Page(67, "Shade décide d'accepter l'offre du peuple inconnu et de rester dans le village après avoir découvert la salle secrète de la grotte.")
page67.ajouter_texte("En acceptant l'offre du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page67.ajouter_texte("Shade s'intègre dans le village et devient un membre respecté de la communauté.")
page67.ajouter_texte("Il vit heureux dans le village inconnu et découvre des secrets sur l'île mystérieuse grâce à sa nouvelle vie dans le village.")
page67.ajouter_texte("Fin de l'histoire.")
livre[67] = page67

page68 = Page(68, "Shade décide de refuser l'offre du peuple inconnu et de continuer à explorer l'île mystérieuse après avoir découvert la salle secrète de la grotte.")
page68.ajouter_texte("En refusant l'offre du peuple inconnu, Shade continue à explorer l'île mystérieuse et découvre de nouveaux secrets et de nouvelles aventures.")
page68.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse et découvre des trésors cachés et des mystères anciens.")
page68.ajouter_texte("Fin de l'histoire.")
livre[68] = page68

page69 = Page(69, "Shade décide d'accepter l'aide de l'esprit protecteur dans la salle souterraine.")
page69.ajouter_texte("En acceptant l'aide de l'esprit protecteur, Shade découvre que l'esprit protecteur est en fait un guide spirituel qui lui offre des conseils et des protections pour naviguer à travers les dangers de l'île mystérieuse.")
page69.ajouter_texte("Avec l'aide de l'esprit protecteur, Shade parvient à surmonter les obstacles et les dangers de l'île mystérieuse et découvre des secrets cachés sur l'île.")
page69.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse avec l'aide de l'esprit protecteur et découvre des trésors cachés et des mystères anciens.")
page69.ajouter_texte("Fin de l'histoire.")
livre[69] = page69

page70 = Page(70, "Shade décide de refuser l'aide de l'esprit protecteur et de continuer à explorer l'île par lui-même dans la salle souterraine.")
page70.ajouter_texte("En refusant l'aide de l'esprit protecteur, Shade continue à explorer l'île par lui-même et se fait attaquer par des créatures mystérieuses dans la salle souterraine.")
page70.ajouter_texte("Il se fait submerger par les créatures mystérieuses et meurt dans la salle souterraine.")
page70.ajouter_texte("Fin de l'histoire.")
livre[70] = page70

page71 = Page(71, "Shade décide de continuer à se battre contre l'esprit protecteur dans la salle souterraine.")
page71.ajouter_texte("En continuant à se battre contre l'esprit protecteur, Shade ne parvient pas à vaincre l'esprit et est gravement blessé dans le combat.")
page71.ajouter_texte("Finalement, Shade meurt de ses blessures dans la salle souterraine.")
page71.ajouter_texte("Fin de l'histoire.")
livre[71] = page71

page72 = Page(72, "Shade décide d'essayer de s'échapper en courant à travers la salle souterraine.")
page72.ajouter_texte("En essayant de s'échapper en courant à travers la salle souterraine, Shade est finalement capturé par le peuple inconnu du village.")
page72.ajouter_texte("Le peuple inconnu ne prend pas de pitié pour Shade et le condamne à être emprisonné dans une cage en bois dans le village.")
page72.ajouter_texte("Fin de l'histoire.")
livre[72] = page72

page73 = Page(73, "Shade décide de continuer à essayer de miner le mur bloquant le passage lumineux dans la salle souterraine.")
page73.ajouter_texte("En continuant à essayer de miner le mur, Shade ne parvient pas à miner le mur et la lave continue de se rapprocher de lui, menaçant de l'atteindre.")
page73.ajouter_texte("Finalement, Shade est atteint par la lave et meurt dans la salle souterraine.")
page73.ajouter_texte("Fin de l'histoire.")  
livre[73] = page73

page74 = Page(74, "Shade décide d'essayer de trouver une autre solution pour s'échapper de la salle souterraine.")
page74.ajouter_texte("En essayant de trouver une autre solution pour s'échapper de la salle souterraine, Shade découvre une sortie secrète dans la salle souterraine qui le mène à l'extérieur de la grotte.")
page74.ajouter_texte("Il arrive au village inconnu, où il est accueilli par les habitants du village qui le prennent pour un héros en raison de sa survie à l'attaque de la lave.")
page74.ajouter_texte("Le peuple le félicite pour avoir survécu à l'attaque de la lave et lui offre une place d'honneur dans leur village.")
page74.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page74.ajouter_choix("a48", "Accepter l'offre du peuple inconnu et rester dans le village", 99)
page74.ajouter_choix("b48", "Refuser l'offre et continuer à explorer l'île mystérieuse", 100)
livre[74] = page74  

page75 = Page(75, "Shade décide d'accepter l'offre du peuple inconnu et de rester dans le village après avoir trouvé l'artefact ancien.")
page75.ajouter_texte("En acceptant l'offre du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page75.ajouter_texte("Shade s'intègre dans le village et devient un membre respecté de la communauté.")
page75.ajouter_texte("Il vit heureux dans le village inconnu et découvre des secrets sur l'île mystérieuse grâce à sa nouvelle vie dans le village.")
page75.ajouter_texte("Fin de l'histoire.")
livre[75] = page75

page76 = Page(76, "Shade décide de refuser l'offre du peuple inconnu et de continuer à explorer l'île mystérieuse après avoir trouvé l'artefact ancien.")
page76.ajouter_texte("En refusant l'offre du peuple inconnu, Shade continue à explorer l'île mystérieuse et découvre de nouveaux secrets et de nouvelles aventures.")
page76.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse et découvre des trésors cachés et des mystères anciens.")
page76.ajouter_texte("Fin de l'histoire.")
livre[76] = page76

page77 = Page(77, "Shade décide de s'excuser auprès du peuple inconnu pour éviter d'être capturé dans le village après avoir été accueilli par les habitants du village.")
page77.ajouter_texte("En s'excusant auprès du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page77.ajouter_texte("Le peuple inconnu accepte les excuses de Shade et lui offre une place d'honneur dans leur village.")
page77.ajouter_texte("Il peut choisir d'accepter l'offre du peuple inconnu et rester dans le village ou refuser l'offre et continuer à explorer l'île mystérieuse.")
page77.ajouter_choix("a49", "Accepter l'offre du peuple inconnu et rester dans le village", 101)
page77.ajouter_choix("b49", "Refuser l'offre et continuer à explorer l'île mystérieuse", 102)
livre[77] = page77

page78 = Page(78, "Shade décide d'essayer de s'échapper en courant à travers le village après avoir été accueilli par les habitants du village.")
page78.ajouter_texte("En essayant de s'échapper en courant à travers le village, Shade est finalement capturé par le peuple inconnu du village.")
page78.ajouter_texte("Le peuple inconnu ne prend pas de pitié pour Shade et le condamne à être emprisonné dans une cage en bois dans le village.")
page78.ajouter_texte("Fin de l'histoire.")
livre[78] = page78

page79 = Page(79, "Shade décide d'accepter l'offre du peuple inconnu et de rester dans le village après avoir été accueilli par les habitants du village.")
page79.ajouter_texte("En acceptant l'offre du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page79.ajouter_texte("Shade s'intègre dans le village et devient un membre respecté de la communauté.")
page79.ajouter_texte("Il vit heureux dans le village inconnu et découvre des secrets sur l'île mystérieuse grâce à sa nouvelle vie dans le village.")
page79.ajouter_texte("Fin de l'histoire.")
livre[79] = page79

page80 = Page(80, "Shade décide de refuser l'offre du peuple inconnu et de continuer à explorer l'île mystérieuse après avoir été accueilli par les habitants du village.")
page80.ajouter_texte("En refusant l'offre du peuple inconnu, Shade continue à explorer l'île mystérieuse et découvre de nouveaux secrets et de nouvelles aventures.")
page80.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse et découvre des trésors cachés et des mystères anciens.")
page80.ajouter_texte("Fin de l'histoire.")
livre[80] = page80

page81 = Page(81, "Shade décide d'accepter l'offre du peuple inconnu et de rester dans le village après avoir été accueilli par les habitants du village.")
page81.ajouter_texte("En acceptant l'offre du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page81.ajouter_texte("Shade s'intègre dans le village et devient un membre respecté de la communauté.")
page81.ajouter_texte("Il vit heureux dans le village inconnu et découvre des secrets sur l'île mystérieuse grâce à sa nouvelle vie dans le village.")
page81.ajouter_texte("Fin de l'histoire.")
livre[81] = page81

page82 = Page(82, "Shade décide de refuser l'offre du peuple inconnu et de continuer à explorer l'île mystérieuse après avoir été accueilli par les habitants du village.")
page82.ajouter_texte("En refusant l'offre du peuple inconnu, Shade continue à explorer l'île mystérieuse et découvre de nouveaux secrets et de nouvelles aventures.")
page82.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse et découvre des trésors cachés et des mystères anciens.")
page82.ajouter_texte("Fin de l'histoire.")
livre[82] = page82

page83 = Page(83, "Shade décide d'accepter l'offre du peuple inconnu et de rester dans le village après avoir été accueilli par les habitants du village.")
page83.ajouter_texte("En acceptant l'offre du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page83.ajouter_texte("Shade s'intègre dans le village et devient un membre respecté de la communauté.")
page83.ajouter_texte("Il vit heureux dans le village inconnu et découvre des secrets sur l'île mystérieuse grâce à sa nouvelle vie dans le village.")
page83.ajouter_texte("Fin de l'histoire.")
livre[83] = page83

page84 = Page(84, "Shade décide de refuser l'offre du peuple inconnu et de continuer à explorer l'île mystérieuse après avoir été accueilli par les habitants du village.")
page84.ajouter_texte("En refusant l'offre du peuple inconnu, Shade continue à explorer l'île mystérieuse et découvre de nouveaux secrets et de nouvelles aventures.")
page84.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse et découvre des trésors cachés et des mystères anciens.")
page84.ajouter_texte("Fin de l'histoire.")
livre[84] = page84 

page85 = Page(85, "Shade décide d'accepter l'offre du peuple inconnu et de rester dans le village après avoir été accueilli par les habitants du village.")
page85.ajouter_texte("En acceptant l'offre du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page85.ajouter_texte("Shade s'intègre dans le village et devient un membre respecté de la communauté.")
page85.ajouter_texte("Il vit heureux dans le village inconnu et découvre des secrets sur l'île mystérieuse grâce à sa nouvelle vie dans le village.")
page85.ajouter_texte("Fin de l'histoire.")
livre[85] = page85

page86 = Page(86, "Shade décide de refuser l'offre du peuple inconnu et de continuer à explorer l'île mystérieuse après avoir été accueilli par les habitants du village.")
page86.ajouter_texte("En refusant l'offre du peuple inconnu, Shade continue à explorer l'île mystérieuse et découvre de nouveaux secrets et de nouvelles aventures.")
page86.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse et découvre des trésors cachés et des mystères anciens.")
page86.ajouter_texte("Fin de l'histoire.")
livre[86] = page86

page87 = Page(87, "Shade décide de continuer à se battre contre la créature gardienne du trésor dans la salle secrète du temple après avoir déclenché le piège en volant une partie du trésor.")
page87.ajouter_texte("En continuant à se battre contre la créature gardienne du trésor, Shade ne parvient pas à vaincre la créature et est gravement blessé dans le combat.")
page87.ajouter_texte("Finalement, Shade meurt de ses blessures dans la salle secrète du temple.")
page87.ajouter_texte("Fin de l'histoire.")
livre[87] = page87

page88 = Page(88, "Shade décide d'essayer de s'échapper en courant à travers la salle secrète après avoir déclenché le piège en volant une partie du trésor.")
page88.ajouter_texte("En essayant de s'échapper en courant à travers la salle secrète, Shade est finalement capturé par le peuple inconnu du village.")
page88.ajouter_texte("Le peuple inconnu ne prend pas de pitié pour Shade et le condamne à être emprisonné dans une cage en bois dans le village.")
page88.ajouter_texte("Fin de l'histoire.") 
livre[88] = page88

page89 = Page(89, "Shade décide d'accepter l'offre du peuple inconnu et de rester dans le village après avoir découvert la salle secrète de la grotte.")
page89.ajouter_texte("En acceptant l'offre du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page89.ajouter_texte("Shade s'intègre dans le village et devient un membre respecté de la communauté.")
page89.ajouter_texte("Il vit heureux dans le village inconnu et découvre des secrets sur l'île mystérieuse grâce à sa nouvelle vie dans le village.")
page89.ajouter_texte("Fin de l'histoire.")
livre[89] = page89

page90 = Page(90, "Shade décide de refuser l'offre du peuple inconnu et de continuer à explorer l'île mystérieuse après avoir découvert la salle secrète de la grotte.")
page90.ajouter_texte("En refusant l'offre du peuple inconnu, Shade continue à explorer l'île mystérieuse et découvre de nouveaux secrets et de nouvelles aventures.")
page90.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse et découvre des trésors cachés et des mystères anciens.")
page90.ajouter_texte("Fin de l'histoire.")
livre[90] = page90

page91 = Page(91, "Shade décide d'accepter l'offre du peuple inconnu et de rester dans le village après avoir étudié les peintures rupestres.")
page91.ajouter_texte("En acceptant l'offre du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page91.ajouter_texte("Shade s'intègre dans le village et devient un membre respecté de la communauté.")
page91.ajouter_texte("Il vit heureux dans le village inconnu et découvre des secrets sur l'île mystérieuse grâce à sa nouvelle vie dans le village.")
page91.ajouter_texte("Fin de l'histoire.")
livre[91] = page91

page92 = Page(92, "Shade décide de refuser l'offre du peuple inconnu et de continuer à explorer l'île mystérieuse après avoir étudié les peintures rupestres.")
page92.ajouter_texte("En refusant l'offre du peuple inconnu, Shade continue à explorer l'île mystérieuse et découvre de nouveaux secrets et de nouvelles aventures.")
page92.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse et découvre des trésors cachés et des mystères anciens.")
page92.ajouter_texte("Fin de l'histoire.")
livre[92] = page92

page93 = Page(93, "Shade décide d'accepter l'offre du peuple inconnu et de rester dans le village après avoir étudié les peintures rupestres.")
page93.ajouter_texte("En acceptant l'offre du peuple inconnu, Shade découvre que le peuple inconnu est en fait un groupe de personnes pacifiques qui vivent sur l'île mystérieuse.")
page93.ajouter_texte("Shade s'intègre dans le village et devient un membre respecté de la communauté.")
page93.ajouter_texte("Il vit heureux dans le village inconnu et découvre des secrets sur l'île mystérieuse grâce à sa nouvelle vie dans le village.")
page93.ajouter_texte("Fin de l'histoire.")
livre[93] = page93

page94 = Page(94, "Shade décide de refuser l'offre du peuple inconnu et de continuer à explorer l'île mystérieuse après avoir étudié les peintures rupestres.")
page94.ajouter_texte("En refusant l'offre du peuple inconnu, Shade continue à explorer l'île mystérieuse et découvre de nouveaux secrets et de nouvelles aventures.")
page94.ajouter_texte("Il continue à vivre des aventures passionnantes sur l'île mystérieuse et découvre des trésors cachés et des mystères anciens.")
page94.ajouter_texte("Fin de l'histoire.")
livre[94] = page94


#Boucle principale de code pour naviguer dans le livre interactif   
page_actuelle = 1
#Affichage de la page actuelle et des choix disponibles pour le lecteur
while True:
    page = livre[page_actuelle]
    page.afficher()
#Vérification de la présence de choix disponibles pour le lecteur et fin de l'histoire si aucun choix n'est disponible
    if not page.choix:
        print("\nFin de l'histoire.")
        break
#Attente de l'entrée du lecteur pour choisir une option et navigation vers la page suivante en fonction du choix du lecteur
    while True:
        choix = input("Votre choix : ").lower()
#Vérification de la validité du choix du lecteur et navigation vers la page suivante en fonction du choix du lecteur
        if choix in page.choix:
            page_actuelle = page.choix[choix]["suivante"]
            break
        else:
            print("Choix invalide.")
