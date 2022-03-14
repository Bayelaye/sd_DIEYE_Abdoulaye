from tkinter import *
from tkinter import filedialog

# Création d'une instance du cadre tkinter
from functions import valide_file, valide_to_dico, dico_to_valide

ws = Tk()
ws.title("Menu de Selection de Fichiers")

# Définition de la géométrie du cadre tkinter
ws.geometry("750x350")
ws.eval('tk::PlaceWindow . center')


def get_file_path():
    global file_path1

    file_path1 = filedialog.askopenfilename(title="Select A File", filetypes=(('text files', '*.txt'),
                                                                              ('All files', '*.*')))
    if file_path1:
        Label(ws, text="File path: " + file_path1).pack()
        print(f"Le fichier sélectionné se trouve dans :\n{file_path1}")
        ws.destroy()


# Ajouter un widget label
label = Label(ws, text="Cliques sur le bouton Naviguez pour parcourir les fichiers", font='Georgia 18')
label.pack(pady=10)

# Création d'un bouton
Button(ws, text="Naviguez", command=get_file_path).pack(pady=10)

ws.mainloop()

if valide_file(file_path1):
    print("""
        1. Choisisser un format de sortie différent du format du fichier récupéré.
        0. Exit/Quit
        """)
    while True:
        choix = input()
        if choix == "1":
            print("Donner votre format de sortie ")
            while True:
                form = input()
                if file_path1.endswith(form.lower()):
                    print("Veuillez choisir un autre format différent du format choisi")
                elif form.lower() not in ['csv', 'json', 'yaml', 'xml']:
                    print("Veuillez choisir un format de fichier valide")
                else:
                    file_path1_to_dic = valide_to_dico(file_path1)
                    new_file = dico_to_valide(file_path1_to_dic, form)
                    new_path = "/".join(file_path1.split("/")[:-1])
                    new_path = new_path + "/new_file." + form
                    print(f"Le chemin absolu du fichier de sortie est :\n{new_path}")
                    break
            print("""
            1. Choisisser un autre format de sortie différent du format du fichier récupéré.
            0. Exit/Quit
            """)
        elif choix == "0":
            print("Au revoir !")
            break
else:
    print("Ce fichier n'est pas dans un format valide")
