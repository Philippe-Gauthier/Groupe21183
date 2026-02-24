"""
Livre incroyable
Nom:Léonard Lefebvre
"""

import time
import customtkinter as ctk

# creer the UI
fenêtre = ctk.CTk()
fenêtre.geometry("800x300")
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
fenêtre.title("livre interactif")
# valeur des boutons et leurs liste
button_counter = ["D"]
button1_value = "A"
button2_value = "B"
button3_value = "C"

textes = ctk.CTkLabel(fenêtre, text="Si vous étiez en prison, comment vous pourriez vous échappez")
textes.pack(pady=20)



# code pour changer le texte des boutons ainsi que leurs ligne de ref dans le code ajouter un for
def bouton1_activé():
    button_counter.extend(button1_value)    
    print(button_counter)

    if button_counter == ['D', 'A']:
        
        for bouton, texte_btn in zip(boutons, boutonD_A):
            bouton.configure(text = texte_btn)
        textes.configure(text = texte_D_A)



    if button_counter == ['D', 'A', 'A']:
        my_entry.pack(pady=20)
        for bouton, texte_btn in zip(boutons, boutonD_A_A):
            bouton.configure(text = texte_btn)

        textes.configure(text=texte_D_A_A)

    if button_counter == ['D', 'B', 'A']:
        textes.configure(text=texte_D_B_A)
        fenêtre.after(2000, fenêtre.destroy)

    if button_counter == ['D', 'A', 'A', 'A']:

        for bouton, texte_btn in zip(boutons, boutonD_A_A_A):
            my_entry.pack_forget()
            bouton.configure(text = texte_btn)
            bouton.pack(pady=10)
            name = my_entry.get()
        textes.configure(text = f"okay {name} how about tu fait de quoi de productif a la place de jouer a un jeux nul tu te get un nom qui est mieux que ça")
        textes.pack(pady=20)
    if button_counter == ['D', 'A', 'B', 'A']:
        textes.configure(text=texte_D_A_B_A)
        for bouton, texte_btn in zip(boutons, boutonD_A_B_A):
            bouton.configure(text = texte_btn)
    if button_counter == ['D', 'A', 'B', 'A']:
        textes.configure(text=texte_D_A_B_A_A)
        fenêtre.after(2000, fenêtre.destroy)

    if button_counter == ['D', 'A','C', 'A']:
        
        for bouton, texte_btn in zip(boutons, boutonD_A_C_A):
            bouton.configure(text = texte_btn)
        textes.configure(text = texte_D_A_C_A)
    if button_counter == ['D', 'A','C', 'A','A']:
        textes.configure(text=texte_D_A_C_A_A)
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'B','B', 'A']:
        textes.configure(text=texte_D_B_B_A)
    if button_counter == ['D', 'B', 'B', 'B','A']:
        textes.configure(text=texte_D_B_B_B_A)
        for bouton, texte_btn in zip(boutons, boutonD_B_B_B_A):
            bouton.configure(text = texte_btn)  
    if button_counter == ['D', 'B', 'B', 'B','A','A']:
        textes.configure(text=texte_D_B_B_B_A_A) 
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'B', 'B', 'B','A','B']:
        textes.configure(text=texte_D_B_B_B_A_B)
        for bouton, texte_btn in zip(boutons, boutonD_B_B_B_A_B):
            bouton.configure(text = texte_btn)
    if button_counter == ['D', 'B', 'B', 'B','C']:
        textes.configure(text=texte_D_B_B_B_C)
        for bouton, texte_btn in zip(boutons, boutonD_B_B_B_C_A):
            bouton.configure(text = texte_btn)
    if button_counter == ['D', 'B', 'B', 'B','A','B','A']:
        textes.configure(text=texte_D_B_B_B_A_B_A)
        fenêtre.after(2000, fenêtre.destroy)
def bouton2_activé():
    print("bouton2")
    button_counter.extend(button2_value)
    print(button_counter)

    
    if button_counter == ['D', 'B']:
        for bouton, texte_btn in zip(boutons, boutonD_B):
            bouton.configure(text = texte_btn)
            bouton.pack(pady=10)
            textes.configure(text = texte_D_B)
    if button_counter == ['D', 'B','B']:
        for bouton, texte_btn in zip(boutons, boutonD_B_B):
            bouton.configure(text = texte_btn)
            bouton.pack(pady=10)
        textes.configure(text=texte_D_B_B)
        textes.pack(pady=20)

    if button_counter == ['D', 'A', 'B']:
        for bouton, texte_btn in zip(boutons, boutonD_A_B):
            bouton.configure(text = texte_btn)

        textes.configure(text=texte_D_A_B)

    if button_counter == ['D', 'A', 'B', 'B']:
        textes.configure(text=texte_D_A_B_B)
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'A', 'B']:
        my_entry.pack(pady=20)
        for bouton, texte_btn in zip(boutons, boutonD_A_B):
            bouton.configure(text = texte_btn)

        textes.configure(text=texte_D_A_B)

    if button_counter == ['D', 'A','C', 'A','B']:
        textes.configure(text = texte_D_A_C_A_B)
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'B', 'B', 'B']:
        textes.configure(text=texte_D_B_B_B)
        for bouton, texte_btn in zip(boutons, boutonD_B_B_B):
            bouton.configure(text = texte_btn)
    if button_counter == ['D', 'A','B', 'A','B']:
        textes.configure(text = texte_D_A_C_A_B)
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'B', 'B', 'B','B']:
        textes.configure(text=texte_D_B_B_B_B)
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'B', 'B', 'B','C','B']:
        textes.configure(text=texte_D_B_B_B_C_B) 
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'B', 'B', 'B','A','B','B']:
        textes.configure(text=texte_D_B_B_B_A_B_B)
        fenêtre.after(2000, fenêtre.destroy)
def bouton3_activé():
    print("bouton3")
    button_counter.extend(button3_value)
    print(button_counter)
    if button_counter == ['D', 'C']:
        textes.configure(text=texte_D_C)
        fenêtre.after(3000, fenêtre.destroy)
    if button_counter == ['D', 'A', 'B', 'C']:
        textes.configure(text=texte_D_A_B_C)
        
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'A','C']:
        
        for bouton, texte_btn in zip(boutons, boutonD_A_C):
            bouton.configure(text = texte_btn)
        textes.configure(text = texte_D_A_C)
    if button_counter == ['D', 'B','C']:
        
        for bouton, texte_btn in zip(boutons, boutonD_B_C):
            bouton.configure(text = texte_btn)
        textes.configure(text = texte_D_B_C)

    if button_counter == ['D', 'A','C','B']:
        textes.configure(text=texte_D_A_C_B)
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'A','C','B']:
        textes.configure(text=texte_D_B_B_C)
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'A','B','A','C']:
        textes.configure(text=texte_D_A_B_A_C)
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'B', 'B', 'B','C']:
        textes.configure(text=texte_D_B_B_B_C)
        for bouton, texte_btn in zip(boutons, boutonD_B_B_B_C):
            bouton.configure(text = texte_btn)
    if button_counter == ['D', 'B', 'B', 'B','C']:
        textes.configure(text=texte_D_B_B_B_C)
        for bouton, texte_btn in zip(boutons, boutonD_B_B_B_C):
            bouton.configure(text = texte_btn)
    if button_counter == ['D', 'B', 'B', 'B','A','C','C']:
        textes.configure(text=texte_D_B_B_B_A_C) 
        fenêtre.after(2000, fenêtre.destroy)
    if button_counter == ['D', 'B', 'B', 'B','C']:
        textes.configure(text=texte_D_B_B_B_C_C)
        for bouton, texte_btn in zip(boutons, boutonD_B_B_B_C_C):
            bouton.configure(text = texte_btn)
    if button_counter == ['D', 'B', 'B', 'B','A','B','C']:
        textes.configure(text=texte_D_B_B_B_A_B_C)
        fenêtre.after(2000, fenêtre.destroy)
# texte du bouton 1
button1_text = "je m'echapperais de la prison a travers un tunnel"
button1_text_D_A = "Qu'est-ce que je pourrais faire pour m'échapper alors?"
button1_text_D_B = "pourquoi toute des john?"
button1_text_D_A_A = "voici mon nom"
button1_text_D_A_B = "Je sais pas ce que j'ai fait pour me rendre ici je suis innocent"
button1_text_D_A_A_A = "moi je trouve que c'est un beau nom"
button1_text_D_A_C = "euhhh, cahngement de plan"
button1_text_D_A_B_A = "je suis pas vraiment un spécialiste la dedans, moi ce que je fait c'est la comptabilité"
button1_text_D_B_C = "je sais pas comment je doit le prendre..."
button1_text_D_A_C_A = "tu veux vraiment pas me voir réussir hein"
button1_text_D_B_B = "écoute je suis pas parfait et on fait chacun les choses a notre manière"
button1_text_D_B_B_B = "en fait pour m'aider ça prendrais un peu ça"
button1_text_D_B_B_B_A = "Je peux creuser un trou?"
button1_text_D_B_B_B_C = "wow j'aime pas ou ça va"
button1_text_D_B_B_B_A_B = "pas très gentil tout ça"
button1_text_D_B_B_B_C_A = "parfait"
button1_text_D_B_B_B_C_C = "je m'en vais"
# texte du bouton 2
button2_text = "je ne m'échapperais pas je ferait partie de la gang la plus tough"
button2_text_D_A = "je veux m'échapper de la prison, laisse moi tranquille!!!"
button2_text_D_B = "J'ai pas pensé jusqu'a la pour être honnête..."
button2_text_D_A_A = "J'ai pas envie d'avoir un nom"
button2_text_D_A_B = "Bon raisonnement ça fait un gros débat sur la sociologie humaine"
button2_text_D_A_A_A = "bon bin j'ai pas envie de me faire juger comme ça est-ce que on peut passer a autre chose"
button2_text_D_A_C = "ok, je fait pas exprès, mais j'échappe le savon."
button2_text_D_A_B = "Bin si tu sais comment checker les fichier, je veux dire tu t'y connais mieux que moi"
button2_text_D_B_C = "C'est pas très gentil tout ça, mais c'est corrct je le prend pas mal"
button2_text_D_A_C_A = "est-ce que quelqu'un est frustré que je le outsmart?"
button2_text_D_B_B = "tout le monde font les chose a leur façon y a pas vraiment de façon uniformisé pour ça"
button2_text_D_A_B_A ="T'es pas censé pouvoir vérifier ça, je veux dire c'est ton jeux"
button2_text_D_B_B_B = "J'ai pas envie de m'imposer, mais ça serait un peux ce qu'il faudrait pour moi"
button2_text_D_B_B_B_A = "Je veux acheter un poster de golorak"
button2_text_D_B_B_B_C = "J'aimerais ne pas trop me salir"
button2_text_D_B_B_B_A_B = "j'aimerais que t'arrête les micro aggressions"
button2_text_D_B_B_B_C_A = "parfait"
button2_text_D_B_B_B_C_C ="je m'en vais"
# texte du bouton 3
button3_text = "j'ai pas envie de parler aujourd'hui"
button3_text_D_A = "Je veux juste trouver une cuillère."
button3_text_D_B = "Je m'échappe avec eux pour devenir un des hommes les plus recherché au monde"
button3_text_D_A_A = "J'ai pas envie de te le dire, c'est quand même personnel comme info"
button3_text_D_A_B = "est-ce que tu veux vraiment m'aider ou t'es la pour gosser"
button3_text_D_A_C = "Tu veux pas que je réussisse hein"
button3_text_D_A_A_A = "Mele toi de tes affaire steplait"
button3_text_D_B_C = "bien sur smart guy tu connais le nombre de push up que je peux faire"
button3_text_D_A_C_A = "je suis tanné de jouer on peux tu arrêter, sort moi de prison."
button3_text_D_B_B = "peux tu enfin arrêter de me gocer"
button3_text_D_A_B_A ="A ce te point la qu'est-ce que ça change?"
button3_text_D_B_B_B = "Je vais essayer de me débrouiller"
button3_text_D_B_B_B_A ="Je veux devenir un vendeur de drogue"
button3_text_D_B_B_B_C ="Je creuse un trou très profond"
button3_text_D_B_B_B_A_B = "peux tu me laisser tranquille"
button3_text_D_B_B_B_C_A = "parfait"
button3_text_D_B_B_B_C_C = "je m'en vais"
# texte pour fin
"""
fenêtre.after(2000, fenêtre.destroy)
"""
# créations des 3 boutons
bouton1 = ctk.CTkButton(fenêtre, text=button1_text,command=bouton1_activé)
bouton1.pack(pady=10)

bouton2 = ctk.CTkButton(fenêtre, text=button2_text,command=bouton2_activé)
bouton2.pack(pady=10)

bouton3 = ctk.CTkButton(fenêtre, text=button3_text,command=bouton3_activé)
bouton3.pack(pady=10)

my_entry = ctk.CTkEntry(fenêtre,
	placeholder_text="Enter Your Name",
	height=50,
	width=200,
	font=("Helvetica", 18),
	corner_radius=50,
	text_color="green",
	placeholder_text_color="darkblue",
	fg_color=("blue","lightblue"),  # outer, inner
	state="normal",
)
name = my_entry.get()
# texte du texte
texte_D_A = "vous échapper de vos problèmes, est-ce que c'est ce que vous vouer vraiment un jour il faudra y faire face"# fait
texte_D_B= "Okay original gangster, voici les membres de ton gang, john, johnn, jon et finallement jhon tu fait quoi"# fait
texte_D_C = "ok"# fin,fait
texte_D_A_A = "ben je sais pas, fait ce que tu veux, moi je suis pas maitre de toi, pour le prouver tu peux même ecrire ton nom ici dit moi quand c'est fait"# fait
#texte_D_A_A_A dans son if et fait
texte_D_A_B = "pas vraiment envie qu'est-ce que j'y gagne moi? un criminel est libre, je me sentirais coupable."# fait
texte_D_A_C = "alright tu prend ton lunch, je te préviens, mais après c'est la douche, échappe pas le savon."
texte_D_A_B_B = "mot trop compliqué je suis pu, bye"# fin et fait
texte_D_A_B_C = "pour gosser bye"# fin et fait
texte_D_B_A = "pourquoi pas, tu pose trop de question bye"# fin et fait
texte_D_B_C = "tu peux même pas faire 20 push up sans suer qu'est-ce qui te fait croire que tu peux courir toute ta vie"# fait
texte_D_A_C_A = "C'est ce que je pensais, maintenant tu fait quoi?"# fait
texte_D_A_C_B = "non, non, je veux même pas m'imaginer ça tu peux pas, pus jamais" # fin et fait
texte_D_B_B = "wow c'est vraiment bien tu sais pas ce que tu fait, ça me met en confiance"# fait
texte_D_A_B_A = "disons que je te crois, comment je peux vérifier ça"# fait
texte_D_A_C_A_A = "vraiment pas"# fin et fait
texte_D_A_C_A_B = " arrête, je fait les options je suis déja tanné de toi." # fin et fait
texte_D_B_B_A = "gneh gneh gneh je suis a plaindre arrête de pleurer pis je ferme le jeux"#fin et fait
texte_D_B_B_B= "tu veux quoi, une formation professionnelle?"# fait
texte_D_B_B_C= "ok"  #fin et fait
texte_D_A_B_A_A = "maudit nerd vas-t-en je veux pas que t'infecte mon ordi arrête de jouer" # fin et fait
texte_D_A_B_A_B = "t'as pas l'air cool comme gars"# fin et fait
texte_D_A_B_A_C = "pas grand chose"#fin et fait
texte_D_B_B_B_A=  "Débrouille toi"# fait
texte_D_B_B_B_B= "fait toi plaisir j'imagine revient quand c'est fait"#fin et fait
texte_D_B_B_B_C= "débrouille toi pis fini ce que tu veux faire"# fait
texte_D_B_B_B_A_A ="non"#fin et fait
texte_D_B_B_B_A_B = "vieillard"# fait
texte_D_B_B_B_A_C = "non"#fin et fait
texte_D_B_B_B_C_A = "moi non plus je veux finir mon travail"# fait
texte_D_B_B_B_C_B = "tes dans une prison si tu veux pas te salir vas t-en"# fin et fait
texte_D_B_B_B_C_C = "pour aller ou au pôle nord?"# fait
texte_D_B_B_B_A_B_A = "non"# fin
texte_D_B_B_B_A_B_B = "non"# fin
texte_D_B_B_B_A_B_C = "oui"# fin


boutons = [bouton1, bouton2, bouton3]

# listes
boutonD_A = [button1_text_D_A, button2_text_D_A, button3_text_D_A]
boutonD_B = [button1_text_D_B, button2_text_D_B, button3_text_D_B]
boutonD_A_A = [button1_text_D_A_A, button2_text_D_A_A, button3_text_D_A_A]
boutonD_A_B = [button1_text_D_A_B, button2_text_D_A_B, button3_text_D_A_B]
boutonD_A_A_A = [button1_text_D_A_A_A, button2_text_D_A_A_A, button3_text_D_A_A_A]
boutonD_A_C = [button1_text_D_A_C, button2_text_D_A_C, button3_text_D_A_C]
boutonD_B_C = [button1_text_D_B_C, button2_text_D_B_C, button3_text_D_B_C]
boutonD_A_C_A = [button1_text_D_A_C_A, button2_text_D_A_C_A, button3_text_D_A_C_A]
boutonD_B_B = [button1_text_D_B_B, button2_text_D_B_B, button3_text_D_B_B]
boutonD_A_B_A = [button1_text_D_A_B_A, button2_text_D_A_B_A, button3_text_D_A_B_A]
boutonD_B_B_B = [button1_text_D_B_B_B, button2_text_D_B_B_B, button3_text_D_B_B_B]
boutonD_B_B_B_A = [button1_text_D_B_B_B_A, button2_text_D_B_B_B_A, button3_text_D_B_B_B_A]
boutonD_B_B_B_C = [button1_text_D_B_B_B_C, button2_text_D_B_B_B_C, button3_text_D_B_B_B_C]
boutonD_B_B_B_A_B = [button1_text_D_B_B_B_A_B, button2_text_D_B_B_B_A_B, button3_text_D_B_B_B_A_B]
boutonD_B_B_B_C_A = [button1_text_D_B_B_B_C_A, button2_text_D_B_B_B_C_A, button3_text_D_B_B_B_C_A]
boutonD_B_B_B_C_C =[button1_text_D_B_B_B_C_C, button2_text_D_B_B_B_C_C, button3_text_D_B_B_B_C_C]
fenêtre.mainloop()
