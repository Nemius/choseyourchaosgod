import sys
import os
import json
import tkinter as tk
from bazaslika import *
from PIL import Image, ImageTk
from main import *

chaosChosen = 0

#pravi json fajl ako ne postoji ili je obrisan
def napraviJson():
    f = open("izbor.json", "w")
    f.write("[{\"izbor\" : \"niko\"}]")
    f.close()

#proverava koji je izbor i vraca rezultat
def proveraIzbora():
    fajl = "izbor.json"
    with open(fajl, "r") as f:
        data = json.load(f)
        prvIzb = (data[0]["izbor"])
        return prvIzb

def akojeVecIzabrao():

    def resetIzbora():
        fajl = "izbor.json"
        novi_unos = []
        with open (fajl, "r") as f:
            userChoice = json.load(f)
            i = 0
            for entry in userChoice:
                if i == 0:
                    name = entry["izbor"]
                    name = "niko"
                    novi_unos.append({"izbor" : name})
        with open (fajl, "w") as f:
            json.dump(novi_unos, f, indent=4)
        window.destroy()
        exit()

    chaosChosen = proveraIzbora()
    izabraniBog = ""
    if chaosChosen == "Khorne":
        izabraniBog = kornW
        izabraniTitle = "You are serving Wrathful Khorne"
    elif chaosChosen == "Nurgle":
        izabraniBog = nurglW
        izabraniTitle = "You are serving Pestilential Nurgle"
    elif chaosChosen == "Slaanesh":
        izabraniBog = slaneshW
        izabraniTitle = "You are serving Cruel Slaanesh"
    elif chaosChosen == "Tzeentch":
        izabraniBog = tzentchW
        izabraniTitle = "You are serving Devious Tzeentch"
    else:
        pass

    window = tk.Tk()
    window.title("Chose Your Chaos God!")
    app_x = 600
    app_y = 500
    scr_x = window.winfo_screenwidth()
    scr_y = window.winfo_screenheight()
    xx= (scr_x / 2) - (app_x / 2)
    yy= (scr_y / 2) - (app_y / 2)
    window.geometry(f'{app_x}x{app_y}+{int(xx)}+{int(yy)}')

    pozadinaIzbora = tk.PhotoImage(file= izabraniBog)
    chaosGod = tk.Label(text=izabraniTitle)
    chaosGod.pack(padx=5, pady=5)
    slkImg = tk.Label(window, image= pozadinaIzbora)
    slkImg.pack()
    reset = tk.Button(window, text="CHOSE AGAIN", command=resetIzbora)
    reset.pack(padx=5, pady=5)

    window.mainloop()

#upisuje izbor korisnika koji se generise odabirm slike/dugmeta
def upisivanjeIzbora(chaosChosen):
    fajl = "izbor.json"
    novi_unos = []
    with open (fajl, "r") as f:
        userChoice = json.load(f)
        i = 0
        for entry in userChoice:
            if i == 0:
                name = entry["izbor"]
                name = chaosChosen
                novi_unos.append({"izbor" : name})
    with open (fajl, "w") as f:
        json.dump(novi_unos, f, indent=4)

#glavni prozor aplikacija
def program():

    #funkcija vezana za dugme Enter the Warp, pravi novi prozor i postavlja slike
    def klikUlaz():

        def izlaz():
            root.destroy()
            exit()
    #naredne cetiri funkcije hvataju ako si kliknuo na neku od slika i upisuje je u json fajl
        def korn():
            slan_btn.destroy()
            tzch_btn.destroy()
            nurgl_btn.destroy()
            pobednik = tk.Label(text="YOU CHOSE WISELY!!")
            pobednik.grid(row=3, column=2)
            exitBtn = tk.Button(text="EXIT THE WARP!", command=izlaz)
            exitBtn.grid(row=3, column=6, padx=5, pady=5)
            chaosChosen = "Khorne"

            upisivanjeIzbora(chaosChosen)

        def nurgle():
            slan_btn.destroy()
            korn_btn.destroy()
            tzch_btn.destroy()
            pobednik = tk.Label(text="YOU CHOSE WISELY!!")
            pobednik.grid(row=3, column=3)
            exitBtn = tk.Button(text="EXIT THE WARP!", command=izlaz)
            exitBtn.grid(row=3, column=6, padx=5, pady=5)
            chaosChosen = "Nurgle"

            upisivanjeIzbora(chaosChosen)

        def slanesh():
            korn_btn.destroy()
            tzch_btn.destroy()
            nurgl_btn.destroy()
            pobednik = tk.Label(text="YOU CHOSE WISELY!!")
            pobednik.grid(row=3, column=4)
            exitBtn = tk.Button(text="EXIT THE WARP!", command=izlaz)
            exitBtn.grid(row=3, column=6, padx=5, pady=5)
            chaosChosen = "Slaanesh"

            upisivanjeIzbora(chaosChosen)

        def tzentch():
            slan_btn.destroy()
            korn_btn.destroy()
            nurgl_btn.destroy()
            pobednik = tk.Label(text="YOU CHOSE WISELY!!")
            pobednik.grid(row=3, column=5)
            exitBtn = tk.Button(text="EXIT THE WARP!", command=izlaz)
            exitBtn.grid(row=3, column=6, padx=5, pady=5)
            chaosChosen = "Tzeentch"

            upisivanjeIzbora(chaosChosen)

        window.destroy()

        root = tk.Tk()
        root.title("Chose Your Chaos God!")
        app_x = 565
        app_y = 250
        scr_x = root.winfo_screenwidth()
        scr_y = root.winfo_screenheight()
        xx= (scr_x / 2) - (app_x / 2)
        yy= (scr_y / 2) - (app_y / 2)
        root.geometry(f'{app_x}x{app_y}+{int(xx)}+{int(yy)}')

        #nazivi iznad slika
        zvz1_label = tk.Label(text="****")
        zvz1_label.grid(row=1, column=1, padx=5, pady=5)

        korn_label = tk.Label(text="Wrathful Korne!")
        korn_label.grid(row=1, column=2, padx=5, pady=5)

        nurgl_label = tk.Label(text="Pestilential Nurgle")
        nurgl_label.grid(row=1, column=3, padx=5, pady=5)

        slanes_label = tk.Label(text="Cruel Slaanesh")
        slanes_label.grid(row=1, column=4, padx=5, pady=5)

        tzinch_label = tk.Label(text="Devious Tzeentch")
        tzinch_label.grid(row=1, column=5, padx=5, pady=5)

        zvz2_label = tk.Label(text="****")
        zvz2_label.grid(row=1, column=6, padx=5, pady=5)

        #kreiranje dugmadi sa slikom
        korn_slk = tk.PhotoImage(file=izaberi_K)
        korn_btn = tk.Button(root, image=korn_slk, command=korn)
        korn_btn.grid(row=2, column=2, padx=5, pady=5)

        nurgl_slk = tk.PhotoImage(file=izaberi_N)
        nurgl_btn = tk.Button(root, image=nurgl_slk, command=nurgle)
        nurgl_btn.grid(row=2, column=3, padx=5, pady=5)

        slan_slk = tk.PhotoImage(file=izaberi_S)
        slan_btn = tk.Button(root, image=slan_slk, command=slanesh)
        slan_btn.grid(row=2, column=4, padx=5, pady=5)

        tzch_slk = tk.PhotoImage(file=izaberi_T)
        tzch_btn = tk.Button(root, image=tzch_slk, command=tzentch)
        tzch_btn.grid(row=2, column=5, padx=5, pady=5)

        root.mainloop()

    window = tk.Tk()
    app_x = 600
    app_y = 400
    scr_x = window.winfo_screenwidth()
    scr_y = window.winfo_screenheight()
    xx= (scr_x / 2) - (app_x / 2)
    yy= (scr_y / 2) - (app_y / 2)
    window.geometry(f'{app_x}x{app_y}+{int(xx)}+{int(yy)}')
    window.title("Chose Your Chaos God!")
    pozadinaPortal = tk.PhotoImage(file=portal)
    limg = tk.Label(window, image= pozadinaPortal)
    limg.pack()

    enterBtn = tk.Button(text="ENTER THE WARP!", command=klikUlaz)
    enterBtn.place(x=250, y=200)

    window.mainloop()

