# -*- coding: utf-8 -*-

# im Terminal ausführen
## Funktion ImageTk aus PIL installieren
# sudo apt-get install python-imaging-tk
# Tk installieren
# sudo apt-get install python3-tk

from Tkinter import *
from PIL import ImageTk, Image
import os
import time
import camera

#Gui konfigurieren
gui1 = Tk()
gui1.title("Lachmaschuen")
#Fenstergröße festlegen
gui1.geometry('1100x1000')

gif_pfad = ""


##zum Testen ohne Picamera
#gif_pfad = "Pfad zum Bild"
#gif = ImageTk.PhotoImage(Image.open(gif_pfad))
#label_gif = Label(gui1, image = gif)
#frames = [ImageTk.PhotoImage(file=gif_pfad, format = 'gif -index %i' %(i)) for i in range(4)]

#Funktionen definieren

##Gui starten
def start_gui():
    label_start.pack()
    button_start.pack()
    
def restart_gui():
    label_restart.pack()
    button_restart.pack()

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
    #Bilder für Gif erstellen - Kamera-Funktion aufrufen
    gif_pfad = camera.camera_pic()
    global frames
    frames = [PhotoImage(file=gif_pfad,format = 'gif -index %i' %(i)) for i in range(4)]
    
    #label_start und button_start löschen
    label_start.pack_forget()
    button_start.pack_forget()
    
    #Gif einbinden
    global gif_is_running
    gif_is_running = True
    label_gif.pack()
    gui1.after(0, gif_einbinden, 0)
    
    #Label und Button für Restart einblenden
    restart_gui()

##Button restart
def clicked_button_restart():
    #Gif-Darstellung beenden
    global gif_is_running
    gif_is_running = False
    label_gif.pack_forget()
    
    #Label restart unf Button restart ausblenden
    label_restart.pack_forget()
    button_restart.pack_forget()
    
    #Label Start und Button Start einblenden
    start_gui()

if __name__ == '__main__':
    #Button erstellen
    button_start = Button(gui1, text="Start", command=clicked_button_start, font=("Arial", 20))
    button_restart = Button(gui1, text = "von vorne", command= clicked_button_restart, font= ("Arial",20))
    label_gif = Label(gui1)

    #Label erstellen
    label_start = Label(gui1, text ="Drücke Start, um die Lachmaschuen zu starten", font = ("Arial", 20))
    label_restart = Label(gui1, text ="Bitte hier klicken, um zum Ausgangszustand zurückzukehren", font = ("Arial", 20))

    #Gui starten
    start_gui()
    
    gui1.mainloop()


