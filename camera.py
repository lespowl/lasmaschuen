# -*- coding: utf-8 -*-

'''
This project requires ImageMagick, a command-line program for image manipulation. To install ImageMagick, 
run the following commands in a terminal window:
sudo apt-get update
sudo apt-get install imagemagick -y
'''

#Bibliotheken importieren
from picamera import PiCamera, Color
import time
from datetime import datetime
import os


camera = PiCamera()

#Konfiguration Kamera
##Auflösung anpassen
camera.resolution = (1024, 768)

##horizontal spiegeln
#camera.rotation = 180

##Belichtung
### off, auto, night, nightpreview, backlight, spotlight, sports, snow, beach, verylong, fixedfps, antishake, fireworks
camera.exposure_mode = 'auto'

##Weißabgleich
### off, auto, sunlight, cloudy, shade, tungsten, fluorescent, flash, horizon
camera.awb_mode = 'fluorescent'

#Konfiguration GIF
#Anzahl Bilder in GIF
num_pic = 4

#Dauer der Bilder in GIF (in Millisekunden)
num_delay = 15

#Pfad Pics
pfad_pics = '/home/pi/Lachmaschuen/Pics_temp'

#Pfad Gif
pfad_gif = '/home/pi/Lachmaschuen/Gif/'



#Funktion zur Erstellung der Gif
def gif(pfad_pics_parameter):
    
    # eindeutigen Dateinamen erstellen
    now = datetime.now()
    dateiname = now.strftime("%Y-%m-%d_%H:%M:%S.gif")
    gif_pfad_name = pfad_gif + dateiname
    
    #Backticks `` Befehl wird ausgeführt und Ergebnis im String eingesetzt
    os.system('convert -delay ' + str(num_delay) + ' -loop 0 ' + pfad_pics_parameter + '/image*.jpg ' + gif_pfad_name)
    return gif_pfad_name  


#Funktion zur Aufnahme der Bilder sowie Erstellung der Gifs
def camera_pic():
    try:
        #alpha: Preview halb-durchsichtig starten (0-255) alpha = 200
        camera.start_preview(alpha = 200, fullscreen = True) 
        # Text konfigurieren
        camera.annotate_text_size = 160 #6-160
        camera.annotate_background = Color('black')
        camera.annotate_foreground = Color('white')
        
        # Kamera wartet 2 Sekunden, bevor der Countdown startet
        time.sleep(2)  
        
        # Countdown läuft runter 5.. 4..
        for i in range(5,2,-1):
            camera.annotate_text = "%s" % i
            time.sleep(1)
        camera.annotate_text = ""
                                      
        
        # Pfad für die Bilder erstellen
        pfad_temp = pfad_pics + '/pics_session'
        os.mkdir(pfad_temp)
        
        # bei 3 startet die Kamera mit der Aufnahme
        for i in range(num_pic):
            camera.capture(pfad_temp + '/image{0:02d}.jpg'.format(i))
            time.sleep(0.5)
            
        #Preview wird beendet    
        camera.stop_preview()                           
        
        # Funktion gif aufrufen, temporären Pics-session-Ordner übergeben
        pfad_gif_return = gif(pfad_temp)
        
        
        # Inhalt des Pics-session-Ordner löschen
        for root, dirs, files in os.walk(pfad_temp, topdown=False):
            for name in files:
                os.remove(os.path.join(root, name))
            for name in dirs:
                os.rmdir(os.path.join(root, name))
        # Pics-session-Ordner löschen
        os.rmdir(pfad_temp)
        
        return pfad_gif_return

    except KeyboardInterrupt:
        #bei Unterbrechen des Programms mittels ctrl+c wird die preview beendet                         
        camera.stop_preview()



#Funktion camera_pic() wird ausgeführt
if __name__ == '__main__':
    print(camera_pic())
    print('fertisch')

