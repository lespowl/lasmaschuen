# -*- coding: utf-8 -*-

# im Terminal ausführen
## Funktion ImageTk aus PIL installieren
# sudo apt-get install python-imaging-tk
# Tk installieren
# sudo apt-get install python3-tk


from Tkinter import *
import ttk
from PIL import ImageTk, Image
import camera


gui = Tk()
gui.title("Lachmaschuen")

#Fenstergröße festlegen
gui.geometry('800x600')


# Definieren, was passiert, wenn Buttons geklickt werden
# Muss vor der Definition des Buttons getan werden!!!
# Button 1 Definition
def clicked_button_start():
    # label_gif.pack()
    camera.camera_pic()
    gif_gui.pack()
    label_restart.pack()
    button_restart.pack()

    
    


## zur Ausgangs-Gui zurückkehren 
def clicked_button_restart():
    camera.camera_pic()
    gif_gui.pack()
    label_restart.pack()
    button_restart.pack()



#gif = PhotoImage(file = "/Users/stephanielist/Desktop/Studium_Human_Factors/2.Semester/Ingenieurwissenschaften/Programmierung/Projekt_Raspberry_Pi/blurred.gif")
#gif = ImageTk.PhotoImage(Image.open("/home/pi/Desktop/hund.gif"))
#label_gif = Label(gui, image = gif)

gif_pfad = camera.camera_pic()
gif = ImageTk.PhotoImage(Image.open(gif_pfad))
gif_gui = Label(gui, image = gif)



#Label erstellen (im Fenster)
label_1 = Label(gui, text ="Drücke Start, um die Lachmaschuen zu starten", font = ("Arial", 20))
label_restart = Label(gui, text ="Bitte hier klicken, um zum Ausgangszustand zurückzukehren", font = ("Arial", 20))

#Button erstellen
button_start = Button(gui, text="Start", command=clicked_button_start, font=("Arial", 20))
button_restart = Button(gui, text = "von vorne", command= clicked_button_restart, font= ("Arial",20))

##zur Darstellung im Darkmode auf dem Mac
#button_start = ttk.Button(gui, text="Start", command=clicked_button_start)



#Button und Labels von oben nach unten erstellen
label_1.pack()
button_start.pack()





gui.mainloop()



