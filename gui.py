# -*- coding: utf-8 -*-

# im Terminal ausführen
## Funktion ImageTk aus PIL installieren
# sudo apt-get install python-imaging-tk
# Tk installieren
# sudo apt-get install python3-tk

from tkinter import *
from PIL import ImageTk, Image
import os
import time
import camera
import dropbox_export

#Gui konfigurieren
gui1 = Tk()
farbe_bg = "white"
gui1.configure(bg= farbe_bg)
gui_frame = Frame(gui1, bg= farbe_bg)
gui1.title("Lachmaschuen")
#Fenstergröße festlegen
#gui1.geometry('1100x1000')  

#Fullscreen ESC beendet
gui1.attributes('-fullscreen', True)
gui1.bind("<Escape>", quit)

gif_pfad = ""


##zum Testen ohne Picamera
#gif_pfad = "Pfad zum Bild"
#gif = ImageTk.PhotoImage(Image.open(gif_pfad))
#label_gif = Label(gui1, image = gif)
#frames = [ImageTk.PhotoImage(file=gif_pfad, format = 'gif -index %i' %(i)) for i in range(4)]

#Funktionen definieren

##Gui starten
def start_gui():
    gui_frame.pack(pady=200)
    label_startfoto.pack()
    label_start.pack(pady=30)
    button_start.pack(side='bottom')
    

def losgehts_gui():
    gui_frame.pack(pady=200)
    label_losgehts.pack(pady=30)
    button_losgehts.pack(side='bottom')    
 
 
def dropbox_gui():
    gui_frame.pack(ipadx=20, ipady=40, pady=40)
    label_dropbox.pack()
    button_dropboxja.pack(side='left')
    button_dropboxnein.pack(side='right')
    
        
def restart_gui():
    gui_frame.pack(pady=200)
    label_restart.pack(pady=30)
    button_restart.pack(side='bottom')

##Gif in Gui einbinden
def gif_einbinden(ind):
    if gif_is_running: 
        frame = frames[ind]
        ind += 1
        ind = ind%len(frames)
        #time.sleep(0.15)
        label_gif.configure(image=frame)
        gui1.after(100, gif_einbinden, ind)


#Funktionen der Buttons definieren
##Button Start
def clicked_button_start():
    gui_frame.pack_forget()
    label_start.pack_forget()
    button_start.pack_forget()
    losgehts_gui()
    
##Button los gehts
def clicked_button_losgehts():
    #Label start und Button start ausblenden
    gui_frame.pack_forget()
    label_startfoto.pack_forget()
    label_losgehts.pack_forget()
    button_losgehts.pack_forget()

    
    #Bilder für Gif erstellen - Kamera-Funktion aufrufen
    global gif_pfad
    gif_pfad = camera.camera_pic()
    global frames
    frames = [PhotoImage(file=gif_pfad,format = 'gif -index %i' %(i)) for i in range(4)]
    

    
    #Gif einbinden
    global gif_is_running
    gif_is_running = True
    label_gif.pack(pady=20)
    gui1.after(0, gif_einbinden, 0)
    
    #Label und Button für Dropbox einblenden
    dropbox_gui()

##Button Dropboxja
def clicked_button_dropboxja():
    #GIF in Dropbox laden
    dropbox_export.dropbox_ja(gif_pfad)
    
    #Gif-Darstellung beenden
    global gif_is_running
    gif_is_running = False
    label_gif.pack_forget()
    
    #Label restart und Button restart ausblenden
    gui_frame.pack_forget()
    label_dropbox.pack_forget()
    button_dropboxja.pack_forget()
    button_dropboxnein.pack_forget()
    
    #Label und Button für Restart einblenden
    restart_gui()

##Button Dropboxnein
def clicked_button_dropboxnein():
    #Gif-Darstellung beenden
    global gif_is_running
    gif_is_running = False
    label_gif.pack_forget()
    
    #Label restart und Button restart ausblenden
    gui_frame.pack_forget()
    label_dropbox.pack_forget()
    button_dropboxja.pack_forget()
    button_dropboxnein.pack_forget()
    
    #Label und Button für Restart einblenden
    restart_gui()
    


##Button restart
def clicked_button_restart():
    #Label restart und Button restart ausblenden
    gui_frame.pack_forget()
    label_restart.pack_forget()
    button_restart.pack_forget()
    
    #Label Start und Button Start einblenden
    start_gui()

if __name__ == '__main__':
    #Button erstellen
    button_start = Button(gui_frame, text="Start", command=clicked_button_start, font=("Arial", 20), bg="black", fg="white")
    button_losgehts = Button(gui_frame, text="Los gehts", command=clicked_button_losgehts, font=("Arial", 20), bg="black", fg="white")
    
    button_dropboxja = Button(gui_frame, text="Ja, hochladen", command=clicked_button_dropboxja, font=("Arial", 20), bg="green")
    
    button_dropboxnein = Button(gui_frame, text="Nein, nicht hochladen", command=clicked_button_dropboxnein, font=("Arial", 20), bg="red")
    
    button_restart = Button(gui_frame, text = "von vorne", command= clicked_button_restart, font= ("Arial",20), bg="black", fg="white")
    label_gif = Label(gui1)

    #Label erstellen
    label_start = Label(gui_frame, text ="Schün, dass du da bist.\nDrücke Start, um die Lachmaschün zu starten", font = ("Arial", 20), bg= farbe_bg)
    
    startfoto = ImageTk.PhotoImage(Image.open("startbild.jpg"))
    
    label_startfoto = Label(gui_frame, image = startfoto)
    
    label_losgehts = Label(gui_frame, text ="Bist du bereit?\nSetze dich bitte aufrecht auf den Stuhl und drücke auf 'Los gehts'.", font = ("Arial", 20), bg= farbe_bg)
    
    label_dropbox = Label(gui_frame, text ="Darf das GIF in die Dropbox geladen werden?", font = ("Arial", 20), bg= farbe_bg)
    
    label_restart = Label(gui_frame, text ="Bitte hier klicken, um die Lachmaschün neu zu starten", font = ("Arial", 20), bg= farbe_bg)

    #Gui starten
    start_gui()
    
    gui1.mainlmoop()


