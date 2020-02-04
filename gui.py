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
gui1.geometry('800x480')  

#Fullscreen ESC beendet
gui1.attributes('-fullscreen', False)
gui1.bind("<Escape>", quit)

gif_pfad = ""
qr_pfad = ""


##zum Testen ohne Picamera
#gif_pfad = "/home/pi/Lachmaschuen/Gif/2019-12-17_15:11:15.gif"
#gif = ImageTk.PhotoImage(Image.open(gif_pfad))
#label_gif = Label(gui1, image = gif)
#für Foto
#frames = [ImageTk.PhotoImage(file=gif_pfad, format = 'gif -index %i' %(i)) for i in range(4)]
#für Gif
#frames = [PhotoImage(file=gif_pfad,format = 'gif -index %i' %(i)) for i in range(4)]

#Funktionen definieren

##Gui starten
def start_gui():
    gui_frame.pack(pady=20)
    label_startfoto.pack()
    label_start.pack(pady=10)
    button_start.pack(side='bottom')
    

def losgehts_gui():
    gui_frame.pack(pady=20)
    label_losgehts.pack(pady=30)
    button_losgehts.pack(side='bottom')    
 
 
def dropbox_gui():
    gui_frame.pack(ipadx=10, ipady=40, pady=40)
    label_dropbox.pack()
    button_dropboxja.pack(side='left')
    button_dropboxnein.pack(side='right')

def restart_dropbox_ja_gui():
    gui_frame.pack(pady=20)
    label_restart.pack(pady=30)
    button_restart_dropbox_ja.pack(side='bottom')
    
def restart_dropbox_nein_gui():
    gui_frame.pack(pady=2)
    label_restart.pack(pady=30)
    button_restart_dropbox_nein.pack(side='bottom')

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
    #gui_frame.pack_forget()
    label_startfoto.pack_forget()
    label_losgehts.pack_forget()
    button_losgehts.pack_forget()

    label_bittewarten.pack()
    
    #Bilder für Gif erstellen - Kamera-Funktion aufrufen
    global gif_pfad
    gif_pfad = camera.camera_pic()
    global frames
    frames = [PhotoImage(file=gif_pfad,format = 'gif -index %i' %(i)) for i in range(4)]
    gui_frame.pack_forget()
    label_bittewarten.pack_forget()
    
    #Gif einbinden
    global gif_is_running
    gif_is_running = True
    label_gif.pack(pady=20)
    gui1.after(0, gif_einbinden, 0)
    
    #Label und Button für Dropbox einblenden
    dropbox_gui()

##Button Dropboxja
def clicked_button_dropboxja():
    #Gif-Darstellung beenden
    global gif_is_running
    gif_is_running = False
    label_gif.pack_forget()
    
    label_bittewarten.pack(pady=30)
        
    #Gif, Label und Button Dropbox ausblenden
    gui_frame.pack_forget()
    label_dropbox.pack_forget()
    button_dropboxja.pack_forget()
    button_dropboxnein.pack_forget()

    #GIF in Dropbox laden
    link_gif_dp, qr_name = dropbox_export.dropbox_ja(gif_pfad)
    
    
    #QR-Code-Pfad erstellen
    qr_pfad = os.path.join(qr_ordnerpfad, qr_name)
    global qr_bild
    qr_bild = ImageTk.PhotoImage(Image.open(qr_pfad))

    gui_frame.pack(pady=200)
    global label_bild_qr
    label_bild_qr = Label(gui_frame, image = qr_bild)
    global label_link_qr
    label_link_qr = Label(gui_frame, text = str(link_gif_dp), font = ("Arial", 20), bg= farbe_bg)

    #gui_frame.pack_forget()
    label_bittewarten.pack_forget()

    label_qr_erklärung.pack(ipady=40)
    label_bild_qr.pack()
    label_link_qr.pack(pady=30)

    restart_dropbox_ja_gui()


##Button Dropboxnein
def clicked_button_dropboxnein():
    #Gif-Darstellung beenden
    global gif_is_running
    gif_is_running = False
    label_gif.pack_forget()
    
    #Gif, Label und Button Dropbox ausblenden
    gui_frame.pack_forget()
    label_dropbox.pack_forget()
    button_dropboxja.pack_forget()
    button_dropboxnein.pack_forget()
    
    #Label und Button für Restart einblenden
    restart_dropbox_nein_gui()
    


##Button restart Dropbox ja
def clicked_button_restart_dropbox_ja():
    #Label restart und Button restart ausblenden
    gui_frame.pack_forget()
    label_qr_erklärung.pack_forget()
    label_bild_qr.pack_forget()
    label_link_qr.pack_forget()
    label_restart.pack_forget()
    button_restart_dropbox_ja.pack_forget()
    
    #Label Start und Button Start einblenden
    start_gui()
    
##Button restart Dropbox nein
def clicked_button_restart_dropbox_nein():
    #Label restart und Button restart ausblenden
    gui_frame.pack_forget()
    label_restart.pack_forget()
    button_restart_dropbox_nein.pack_forget()
    
    #Label Start und Button Start einblenden
    start_gui()

if __name__ == '__main__':
    # Ordner QR-Code erstellen
    script_path = os.path.dirname(os.path.abspath(__file__))
    qr_ordnerpfad = os.path.join(script_path, "QR_Codes")
    if not os.path.isdir(qr_ordnerpfad):
        os.mkdir(qr_ordnerpfad)

    #Button erstellen
    button_start = Button(gui_frame, text="Start", command=clicked_button_start, font=("Arial", 20), bg="black", fg="white")
    button_losgehts = Button(gui_frame, text="Los gehts", command=clicked_button_losgehts, font=("Arial", 20), bg="black", fg="white")
    
    button_dropboxja = Button(gui_frame, text="Ja, her damit", command=clicked_button_dropboxja, font=("Arial", 20), bg="black", fg="white")
    
    button_dropboxnein = Button(gui_frame, text="Nein, bloß nicht", command=clicked_button_dropboxnein, font=("Arial", 20), bg="black", fg="white")
    
    button_restart_dropbox_ja = Button(gui_frame, text = "von vorne", command= clicked_button_restart_dropbox_ja, font= ("Arial",20), bg="black", fg="white")
    
    button_restart_dropbox_nein = Button(gui_frame, text = "von vorne", command= clicked_button_restart_dropbox_nein, font= ("Arial",20), bg="black", fg="white")


    #Label erstellen
    label_start = Label(gui_frame, text ="Schün, dass du da bist.\nDrücke Start, um die Lachmaschün zu starten", font = ("Arial", 20), bg= farbe_bg)
    
    startfoto = ImageTk.PhotoImage(Image.open("startbild.jpg"))
    
    label_startfoto = Label(gui_frame, image = startfoto)
    
    label_losgehts = Label(gui_frame, text ="Bist du bereit?\nSetze dich bitte aufrecht auf den Stuhl und drücke auf 'Los gehts'.", font = ("Arial", 20), bg= farbe_bg)
    
    label_bittewarten = Label(gui_frame, text ="Die Lachmaschün ist beschäftigt.\nBitte warten!", font = ("Arial", 20), bg= farbe_bg)
    
    label_dropbox = Label(gui_frame, text ="Du hast jetzt die Möglichkeit, einen QR-Code zu erzeugen, um dein Gif herunterzuladen.\nDas Gif wird dazu in die Lachmaschün-Dropbox geladen.", font = ("Arial", 20), bg= farbe_bg)
    
    label_qr_erklärung = Label(gui_frame, text ="Unter folgendem QR-Code bzw. Link kannst du dir dein Gif herunterladen", font = ("Arial", 20), bg= farbe_bg)

    label_restart = Label(gui_frame, text ="Bitte hier klicken, um die Lachmaschün neu zu starten", font = ("Arial", 20), bg= farbe_bg)
    
    label_gif = Label(gui_frame, image = gif_pfad)

    #Gui starten
    start_gui()
    
    gui1.mainloop()


