import dropbox
import qrcode
import os
import requests  # Für Fehlermeldung falls keine Internetverbindung vorhanden

db = dropbox.Dropbox("JOBzoGZ5CMAAAAAAAAAAC_TwWPLaz_udrVSWBC9WDfAGhyCy9P79f8RUC8u0PuHc")

def dropbox_ja(gif_pfad):
    pic = open(gif_pfad, "rb")
    gif_name = os.path.basename(gif_pfad)
    pic_dropbox = "/" + gif_name
    try:
        response = db.files_upload(pic.read(), pic_dropbox)
    except requests.exceptions.ConnectionError:
        print("Keine Internetverbindung vorhanden")
        return None

    pic.close()

    # Link zur GIF freigeben
    freigegebener_link = db.sharing_create_shared_link_with_settings(pic_dropbox)

    # QR-Code konfigurieren
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_H,
        box_size = 2,
        border = 4,)
    
    # QR-Code erstellen
    qr.add_data(freigegebener_link)
    qr.make(fit=True)
    # Bild aus dem QR-Code erstellen
    img = qr.make_image()
    # QR-Code speichern
    qr_name = os.path.splitext(gif_name)[0]+ ".jpg"
    script_path = os.path.dirname(os.path.abspath(__file__))
    qr_pfad = os.path.join(script_path, "QR_Codes", qr_name)
    img.save(qr_pfad)

    return freigegebener_link.url, qr_name



if __name__ == '__main__':
    #zum Testen lokale GIF in den Pfad einfügen
    gif_pfad = "/Users/stephanielist/Desktop/PiTest/1838696_1920.jpg"
    link_gif_dp = dropbox_ja(gif_pfad)
    if link_gif_dp is not None:
        print(link_gif_dp)

    
