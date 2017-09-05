"""
Function to download from ScreenScraper
"""

from urllib import request
from urllib import parse
from urllib import error
from romfile import romfile
from os.path import splitext
from base64 import b64decode
import pickle


def downloadfile(ssurl, ssxml):
    """
    this function will download the ssurl to the ssxml
    return True or Error message
    """
    screenscrapererror = {400: "URL missing parameters",
                          401: "API closed for non suscriber user",
                          403: "Dev login error",
                          404: "Game not found",
                          423: "API closed",
                          426: "Scrapper version obsolete",
                          429: "Maximum threads allowed already used"}
    try:
        con = request.urlopen(ssurl)
    except error.HTTPError as e:
        return ("{} - HTTP error : {}".format(e.code, screenscrapererror[e.code]))
    except error.URLError as e:
        return ("URL error : {}".format(e.reason))
    else:
        request.urlretrieve(ssurl, ssxml)
        return True


def urlconstruct(rom, systemid='', ssid='', sspassword=''):
    """
    this function will return the constructed ssurl
    """
    with open('devlogin', 'rb') as fichier:
        devlogin = pickle.Unpickler(fichier).load()

    ssurl = "https://www.screenscraper.fr/api2/jeuInfos.php?" \
            "devid={}" \
            "&devpassword={}" \
            "&softname=PUXS" \
            "&output=xml" \
            "&ssid={}" \
            "&sspassword={}" \
            "&crc={}" \
            "&md5={}" \
            "&sha1={}" \
            "&systemeid={}" \
            "&romtype=rom" \
            "&romnom={}" \
            "&romtaille={}" \
        .format(b64decode(devlogin["devid"]).decode("utf-8", "ignore"),
                b64decode(devlogin["devpassword"]).decode("utf-8", "ignore"),
                ssid,
                sspassword,
                rom.crc32,
                rom.md5,
                rom.sha1,
                systemid,
                parse.quote_plus(rom.name), rom.size)
    return ssurl


if __name__ == "__main__":
    rom = romfile("Sonic The Hedgehog (USA, Europe).zip")
    ssurl = urlconstruct(rom,1)
    ssxml = splitext(rom.name)[0] + '.xml'
    result = downloadfile(ssurl, ssxml)
    if result == True:
        print("download OK")
    else:
        print(result)
