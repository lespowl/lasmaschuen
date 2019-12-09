# Dokumentation Kamera

Anleitung zur GIF-Erstellung:
Um Kamera aus der GUI zu starten und GIF zu erzeugen:

import camera
pfad_gif = camera.camera_pic()
  Ausführen der Funktion camera_pic(), um Preview der Kamera zu starten und GIF zu speichern
  return der Funktion camera_pic(): Dateipfad zur eben erstellten GIF (pfad_gif_return)


Erklärung der Funktionsweise der Funktionen:

Zeile 19-32:
Konfiguation der Kamera-Einstellungen
Zeile 21:
Auflösung der Kamera reduzieren, um Speicherplatz zu reduzieren und typischen GIF-Look zu erzeugen
Zeile 24:
Bild horizontal spiegeln, falls dies nach Einbau notwendig ist
Zeile 28:
Belichtungsdauer anpassen, je nach Helligkeitsverhältnissen im Raum

Zeile 34-39:
Konfiguation des GIFs
Zeile 36:
Anzahl der Bilder
Zeile 39:
Dauer der Darstellung der einzelnen Bilder

Zeile 41-45:
Pfade, der temporär erzeugnten Bilder (Zeile 42) sowie der fertigen GIF (Zeile 45)

Zeile 49-59:
Funktion, welche die GIF erstellt
Eingabeparameter: Pfad zu den temporär erzeugten Bildern (werden in der camera_pic() erzeugt
Zeile 52-55:
Erzeugung eines eindeutigen Dateinamens (Jahr-Monat-Tag_Stunde:Minute:Sekunde.gif)
Speicherung des Pfades-Dateinamens in Variable: gif_pfad_name
Zeile 57-59:
Erzeugung der GIF und return gif_pfad_name
num_delay: Dauer der Bilder in Sek. (in Zeile 39 definiert)
-loop 0: Darstellung in Dauerschleife

Zeile 62-101:
Funktion, welche Kamera startet, Preview anzeigt, Bilder aufnimmt, in temporären Ordner speichert,
GIF erstellt (durch import der Funktion gif(), löschen des temporären Bild-Ordners
Zeile 65-69:
Starten der Preview (zu Testzewcken halbdurchsichtig - kann bei Endversion auskommentiert werden)
Nach Starten der Preview muss 2Sekunden gewartet werden (sleep(2)), damit sich der Sensor an die Umgebungsbedingungen 
anpassen kann
Zeile 71-73:
Erstellen des temporären Pfades zur Speicherung der Bilder
Zeile 76-78:
Anzahl der Bilder (num_pic in Zeile 36 definiert) wird mit Abstand von 0.5 Sek (Zeile 78) erstellt 
Zeile 81:
Beenden der Preview
Zeile 84:
Funktion gif() aufrufen,
Pfad mit dem gerade erzeugten Bildern wird als Eingabeparameter übergeben
Speicherung des Pfades der erstellten Gif in Variable pfad_gif_return
Zeile 88-95:
Inhalt sowie Ordner des temporär erzeugten Bilder-Ordners löschen

return der Funktion: pfad_gif_return (Pfad zur Gif)


