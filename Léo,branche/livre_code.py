import time
import math
import customtkinter as ctk


# creer the UI
fenêtre = ctk.CTk()
fenêtre.geometry("700x700")
ctk.set_appearance_mode("system")
ctk.set_default_color_theme("blue")
fenêtre.title("livre interactif")
# valeur des boutons et leurs liste
button_counter = ["D"]
button1_value = "A"
button2_value = "B"
button3_value = "C"


# code pour changer le texte des boutons ainsi que leurs ligne de ref dans le code ajouter un for
def bouton1_activé():
    button_counter.extend(button1_value)
    print(button_counter)
def bouton2_activé():
    print("bouton2")
    button_counter.extend(button2_value)
    print(button_counter)
def bouton3_activé():
    print("bouton3")
    button_counter.extend(button3_value)
    print(button_counter)

# créations des 3 boutons
bouton1 = ctk.CTkButton(fenêtre, text="start",command=bouton1_activé)
bouton1.pack(pady=10)

bouton2 = ctk.CTkButton(fenêtre, text="stop",command=bouton2_activé)
bouton2.pack(pady=10)

bouton3 = ctk.CTkButton(fenêtre, text="maybe",command=bouton3_activé)
bouton3.pack(pady=10)

fenêtre.mainloop()





        
