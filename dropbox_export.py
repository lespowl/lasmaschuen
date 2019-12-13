import dropbox
import os

db = dropbox.Dropbox("JOBzoGZ5CMAAAAAAAAAAC_TwWPLaz_udrVSWBC9WDfAGhyCy9P79f8RUC8u0PuHc")

#print('Account infos: ', db.users_get_current_account())

#gif_pfad = "/home/pi/Lachmaschuen/Gif/2019-12-13_14:28:51.gif"


def dropbox_ja(gif_pfad):
    pic = open(gif_pfad, "rb")
    gif_name = os.path.basename(gif_pfad)
    pic_dropbox = "/" + gif_name
    response = db.files_upload(pic.read(), pic_dropbox)
    pic.close()


if __name__ == '__main__':
    dropbox_ja(gif_pfad)
    print('uploaded')


