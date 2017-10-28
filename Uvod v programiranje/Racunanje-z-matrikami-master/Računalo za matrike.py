import math
import tkinter as tk
import webbrowser
from tkinter import messagebox
import numpy as np


class ZacetniZaslon:
    def __init__(self,okno):

        prikaz_zaslona=tk.Frame()
        racunaj=tk.Button(prikaz_zaslona,text="Računaj",height=2,width=44,command=self.zacetek_racunanja)
        prikaz_zaslona.pack()
        donate=tk.Button(prikaz_zaslona,text="Donate",height=2,width=44, command=self.openurl)
        racunaj.pack()
        donate.pack()
    def openurl(self):
        webbrowser.open_new("https://www.paypal.me/MatejNeumann")

    def zacetek_racunanja(self):
        okno_1=tk.Tk()
        RacunanjeMatrik(okno_1)





class RacunanjeMatrik:
    def __init__(self,okno):
        self.okno=okno
        self.prikaz=tk.Frame(self.okno)
        self.prikaz_2=tk.Frame(self.okno)
        self.prikaz_3=tk.Frame(self.okno)
        self.prikaz.grid(row=1,column=1)
        self.prikaz_3.grid(row=1,column=2)
        self.prikaz_2.grid(row=1, column=3)
        gumb_ime_1 = tk.Label(self.prikaz, text="Prva Matrika",)
        gumb_ime_2 = tk.Label(self.prikaz_2, text="Druga Matrika")
        self.var1 = tk.StringVar(self.prikaz, "izbira")
        meni = tk.OptionMenu(self.prikaz_3, self.var1, 'Seštevanje', 'Odštevanje', 'Množenje', "Inverz", "Transponiranje",
                             "Determinanta", "Sled", )

        gumb_racunaj=tk.Button(self.prikaz_3,text="Računaj",command=self.racunaj)
        meni.configure(width=10)
        meni.configure(height=2)
        self.dolzina_1 = tk.Entry(self.prikaz,width=5)
        self.visina_1 = tk.Entry(self.prikaz,width=5)
        self.dolzina_2 = tk.Entry(self.prikaz_2,width=5)
        self.visina_2 = tk.Entry(self.prikaz_2,width=5)
        gumb_stevilke_1 = tk.Button(self.prikaz, text="vnesi številke", command=self.stevilke_1)
        gumb_stevilke_2 = tk.Button(self.prikaz_2, text="vnesi številke", command=self.stevilke_2)
        gumb_ime_1.grid(row=1,column=1,columnspan=3)
        meni.pack()
        gumb_racunaj.pack()
        gumb_ime_2.grid(row=1,column=1,columnspan=3)
        label=tk.Label(self.prikaz,text="X")
        label.grid(row=2,column=2)
        label_2 = tk.Label(self.prikaz_2, text="X")
        label_2.grid(row=2,column=2)
        gumb_stevilke_1.grid(row=3,column=1,columnspan=3,)
        gumb_stevilke_2.grid(row=3, column=1,columnspan=3)


        self.visina_1.grid(row=2,column=1)

        self.dolzina_1.grid(row=2,column=3)

        self.visina_2.grid(row=2,column=1)

        self.dolzina_2.grid(row=2,column=3)


    def stevilke_1(self):
            self.dolzina = int(self.dolzina_1.get())
            self.visina = int(self.visina_1.get())
            self.prva_matrika=Matrika(self.dolzina,self.visina,self.prikaz)

    def stevilke_2(self):

                self.dolzina = int(self.dolzina_2.get())
                self.visina = int(self.visina_2.get())
                self.druga_matrika=Matrika(self.dolzina,self.visina,self.prikaz_2)

    def racunaj(self):
        value=self.var1.get()
        if value=="Seštevanje":
            self.sestevanje_matrik()
        elif value=="Odštevanje":
            self.odstevanje_matrik()
        elif value=="Množenje":
            self.mnozenje_matrik()
        elif value=="Determinanta":
            self.determinanta_matrike()
        elif value=="Transponiranje":
            self.transponiranje()
        elif value=="Sled":
            self.sled_matrike()
        elif value=="Inverz":
            self.inverz_matrike()

    def sestevanje_matrik(self):
        if not self.prva_matrika.dolzina ==self.druga_matrika.dolzina or  not self.prva_matrika.visina==self.druga_matrika.visina :
             messagebox.showinfo("Napaka!", "Vnesi 2 enako veliki matriki!")
             self.okno.destroy()
        else:
         seznam=[]
         for i in range(self.prva_matrika.visina):
             vrstica=[]
             for j in range(self.prva_matrika.dolzina):

                vrstica.append(int(self.prva_matrika.gumbi[i][j].get())+int(self.druga_matrika.gumbi[i][j].get()))
             seznam.append(vrstica)

             self.prikaz_matrike = tk.Frame(self.okno)
             self.gumbi = []

         for i in range(self.prva_matrika.visina):
                 vrstica = []

                 for j in range(self.prva_matrika.dolzina):
                     gumb = tk.Entry(self.prikaz_matrike,width=7)
                     gumb.insert(0, seznam[i][j])
                     vrstica.append(gumb)
                     gumb.grid(row=i, column=j)
                 self.gumbi.append(vrstica)

                 self.prikaz_matrike.grid(row=2, column=2)

    def odstevanje_matrik(self):
        if not self.prva_matrika.dolzina == self.druga_matrika.dolzina or not self.prva_matrika.visina == self.druga_matrika.visina:
            messagebox.showinfo("Napaka!", "Vnesi 2 enako veliki matriki!")
            self.okno.destroy()
        else:
            seznam = []
            for i in range(self.prva_matrika.visina):
                vrstica = []
                for j in range(self.prva_matrika.dolzina):
                    vrstica.append(int(self.prva_matrika.gumbi[i][j].get()) - int(self.druga_matrika.gumbi[i][j].get()))
                seznam.append(vrstica)

                self.prikaz_matrike = tk.Frame(self.okno)
                self.gumbi = []

            for i in range(self.prva_matrika.visina):
                vrstica = []

                for j in range(self.prva_matrika.dolzina):
                    gumb = tk.Entry(self.prikaz_matrike,width=7)
                    gumb.insert(0, seznam[i][j])
                    vrstica.append(gumb)
                    gumb.grid(row=i, column=j)
                self.gumbi.append(vrstica)
                self.prikaz_matrike.grid(row=2, column=2)

    def mnozenje_matrik(self):
        if not self.prva_matrika.visina==self.druga_matrika.dolzina:
            messagebox.showinfo("Napaka!", "Število stolpcev prve matrike mora biti enako številu vrstic druge!")
            self.okno.destroy()
        else:

            seznam=[[0 for vrstica in range(self.druga_matrika.dolzina)] for stolpec in range(self.prva_matrika.visina)]


            for i in range(self.prva_matrika.visina):
                for j in range(self.druga_matrika.dolzina):
                    for k in range(self.prva_matrika.dolzina):

                        seznam[i][j] =seznam[i][j]+ (int(self.prva_matrika.gumbi[i][k].get()) * int(self.druga_matrika.gumbi[k][j].get()))

            self.prikaz_matrike = tk.Frame(self.okno)
            self.gumbi = []
            for i in range(self.prva_matrika.visina):
                vrstica = []

                for j in range(self.druga_matrika.dolzina):
                    gumb = tk.Entry(self.prikaz_matrike,width=7)
                    gumb.insert(0, seznam[i][j])
                    vrstica.append(gumb)
                    gumb.grid(row=i, column=j)
                self.gumbi.append(vrstica)
                self.prikaz_matrike.grid(row=2, column=2)

    def determinanta_matrike(self):
        if not self.prva_matrika.visina == self.prva_matrika.dolzina:
            messagebox.showinfo("Napaka!", "Vnesi kvadratno matriko")
            self.okno.destroy()

        else:
          seznam = [[0 for vrstica in range(self.prva_matrika.visina)] for stolpec in range(self.prva_matrika.dolzina)]
          for i in range(self.prva_matrika.visina):
              for j in range(self.prva_matrika.dolzina):
                seznam[i][j]=int(self.prva_matrika.gumbi[i][j].get())

          determinanta="{:10.0f}".format(np.linalg.det(seznam))
          self.prikaz_matrike = tk.Frame(self.okno)
          self.prikaz_matrike.grid(row=2,column=2)
          gumb=tk.Entry(self.prikaz_matrike,width=7)
          gumb.insert(0, determinanta)
          gumb.grid(row=1,column=1)

    def transponiranje(self):

          seznam = [[0 for vrstica in range(self.prva_matrika.dolzina)] for stolpec in range(self.prva_matrika.visina)]
          for i in range(self.prva_matrika.visina):
              for j in range(self.prva_matrika.dolzina):

                seznam[i][j]=int(self.prva_matrika.gumbi[i][j].get())
          transponirana_matrika=list(zip(*seznam))

          self.prikaz_matrike = tk.Frame(self.okno)
          self.gumbi = []
          self.prikaz_matrike.grid(row=2, column=2)

          for i in range(self.prva_matrika.dolzina):
             vrstica = []

             for j in range(self.prva_matrika.visina):
                 gumb = tk.Entry(self.prikaz_matrike,width=5)
                 gumb.insert(0, transponirana_matrika[i][j])
                 vrstica.append(gumb)
                 gumb.grid(row=i, column=j)
             self.gumbi.append(vrstica)

             self.prikaz_matrike.grid(row=2, column=2)
    def inverz_matrike(self):
        if not self.prva_matrika.visina == self.prva_matrika.dolzina:
            messagebox.showinfo("Napaka!", "Vnesi kvadratno matriko")
            self.okno.destroy()
        else:
            try:
                seznam = [[0 for vrstica in range(self.prva_matrika.visina)] for stolpec in range(self.prva_matrika.dolzina)]
                for i in range(self.prva_matrika.dolzina):
                    for j in range(self.prva_matrika.visina):
                        seznam[i][j] = int(self.prva_matrika.gumbi[i][j].get())

                inverz = np.linalg.inv(seznam)
                self.prikaz_matrike = tk.Frame(self.okno)
                self.gumbi = []
                for i in range(self.prva_matrika.dolzina):
                    vrstica = []

                    for j in range(self.prva_matrika.visina):
                        gumb = tk.Entry(self.prikaz_matrike,width=7)
                        gumb.insert(0, inverz[i][j])
                        vrstica.append(gumb)
                        gumb.grid(row=i, column=j)
                    self.gumbi.append(vrstica)
                    self.prikaz_matrike.grid(row=2, column=2)
            except:
                messagebox.showinfo("Napaka!", "Matrika nima inverza")
                self.okno.destroy()


    def sled_matrike(self):
        if not self.prva_matrika.visina == self.prva_matrika.dolzina:
            messagebox.showinfo("Napaka!", "Vnesi kvadratno matriko")
            self.okno.destroy()

        else:
            vsota=0
            seznam = [[0 for vrstica in range(self.prva_matrika.visina)] for stolpec in range(self.prva_matrika.dolzina)]
            for i in range(self.prva_matrika.dolzina):
                for j in range(self.prva_matrika.visina):
                    seznam[i][j] = int(self.prva_matrika.gumbi[i][j].get())
            for x in range(self.prva_matrika.dolzina):
                 vsota=vsota+int(seznam[x][x])
            self.prikaz_matrike = tk.Frame(self.okno)
            gumb=tk.Entry(self.prikaz_matrike,width=7)
            self.prikaz_matrike.grid(row=2, column=2)
            gumb.grid(row=1, column=1)
            gumb.insert(0,vsota)


class Matrika:
    def __init__(self,dolzina,visina,frame):
        self.dolzina=dolzina
        self.visina=visina
        self.prikaz_matrike=tk.Frame(frame)

        self.gumbi=[]

        for i in range(self.visina):
            vrstica=[]

            for j in range(self.dolzina):
                gumb=tk.Entry(self.prikaz_matrike,width=5)
                vrstica.append(gumb)
                gumb.grid(row=i, column=j)
            self.gumbi.append(vrstica)
            self.prikaz_matrike.grid(row=4,column=2)




okno=tk.Tk()
abc=ZacetniZaslon(okno)
okno.mainloop()
