# -*- coding: utf-8 -*-

# im Terminal ausführen
## Funktion ImageTk aus PIL installieren
# sudo apt-get install python-imaging-tk
# Tk installieren
# sudo apt-get install python3-tk
'''

from Tkinter import *
import ttk
from PIL import ImageTk, Image
import os
import time
import camera


gui = Tk()
gui.title("Lachmaschuen")

#Fenstergröße festlegen
gui.geometry('800x600')

gif_pfad = ""

# Definieren, was passiert, wenn Buttons geklickt werden
# Muss vor der Definition des Buttons getan werden!!!
# Button 1 Definition
def clicked_button_start():
    camera.camera_pic()
    label.pack()
    gui.after(0, update, 0)
    # label_gif.pack()
    label_restart.pack()
    button_restart.pack()


## zur Ausgangs-Gui zurückkehren 
def clicked_button_restart():
    pass





gif_pfad = camera.camera_pic()
#gif = ImageTk.PhotoImage(Image.open(gif_pfad))
#label_gif = Label(gui, image = gif)



frames = [ImageTk.PhotoImage(file=gif_pfad, format = 'gif -index %i' %(i)) for i in range(4)]


def update(ind):

    frame = frames[ind]
    ind += 1
    ind = ind%len(frames)
    time.sleep(1)
    label.configure(image=frame)
    gui.after(4, update, ind)
    
label = Label(gui)
label.pack()
gui.after(0, update, 0)


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

'''



from Tkinter import *
import time
import os
import camera
root = Tk()

gif_pfad = camera.camera_pic()
frames = [PhotoImage(file=gif_pfad,format = 'gif -index %i' %(i)) for i in range(4)]

def update(ind):

    frame = frames[ind]
    ind += 1
    ind = ind%len(frames)
    time.sleep(1)
    label.configure(image=frame)
    root.after(4, update, ind)
label = Label(root)
label.pack()
root.after(0, update, 0)
root.mainloop()


