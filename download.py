"""
Function to download
"""

from urllib import request
from urllib import parse
from urllib import error
from romfile import romfile
from os.path import splitext
from base64 import b64decode
import pickle

httperrordef = {100: "Continue",
                101: "Switching Protocols",
                102: "Processing",
                200: "OK",
                201: "Created",
                202: "Accepted",
                203: "Non-Authoritative Information",
                204: "No Content",
                205: "Reset Content",
                206: "Partial Content",
                207: "Multi-Status",
                208: "Already Reported",
                210: "Content Different",
                226: "IM Used",
                300: "Multiple Choices",
                301: "Moved Permanently",
                302: "Moved Temporarily",
                303: "See Other",
                304: "Not Modified",
                305: "Use Proxy",
                306: "(aucun)",
                307: "Temporary Redirect",
                308: "Permanent Redirect",
                310: "Too many Redirects",
                400: "Bad Request",
                401: "Unauthorized",
                402: "Payment Required",
                403: "Forbidden",
                404: "Not Found",
                405: "Method Not Allowed",
                406: "Not Acceptable",
                407: "Proxy Authentication Required",
                408: "Request Time-out",
                409: "Conflict",
                410: "Gone",
                411: "Length Required",
                412: "Precondition Failed",
                413: "Request Entity Too Large",
                414: "Request-URI Too Long",
                415: "Unsupported Media Type",
                416: "Requested range unsatisfiable",
                417: "Expectation failed",
                418: "I’m a teapot",
                421: "Bad mapping / Misdirected Request",
                422: "Unprocessable entity",
                423: "Locked",
                424: "Method failure",
                425: "Unordered Collection",
                426: "Upgrade Required",
                428: "Precondition Required",
                429: "Too Many Requests",
                431: "Request Header Fields Too Large",
                449: "Retry With",
                450: "Blocked by Windows Parental Controls",
                451: "Unavailable For Legal Reasons",
                456: "Unrecoverable Error",
                444: "No Response",
                495: "SSL Certificate Error",
                496: "SSL Certificate Required",
                497: "HTTP Request Sent to HTTPS Port",
                499: "Client Closed Request",
                500: "Internal Server Error",
                501: "Not Implemented",
                502: "Bad Gateway ou Proxy Error",
                503: "Service Unavailable",
                504: "Gateway Time-out",
                505: "HTTP Version not supported",
                506: "Variant Also Negotiates",
                507: "Insufficient storage",
                508: "Loop detected",
                509: "Bandwidth Limit Exceeded",
                510: "Not extended",
                511: "Network authentication required"}

sserrordef = {400: "URL missing parameters",
              401: "API closed for non suscriber user",
              403: "Dev login error",
              404: "Game not found",
              423: "API closed",
              426: "Scrapper version obsolete",
              429: "Maximum threads allowed already used"}


def downloadfile(url, path):
    """
    this function will download the url to the xml
    return True or Error message
    """
    
    if "screenscraper.fr" in url:
        errordef = sserrordef
    else:
        errordef = httperrordef

    try:
        con = request.urlopen(url)
    except error.HTTPError as e:
        return ("{} - HTTP error : {}".format(e.code, errordef[e.code]))
    except error.URLError as e:
        return ("URL error : {}".format(e.reason))
    else:
        request.urlretrieve(url, path)
        return True


def urlconstruct(rom, systemid='', ssid='', sspassword=''):
    """
    this function will return the constructed screecnscraper url
    """
    with open('devlogin', 'rb') as fichier:
        devlogin = pickle.Unpickler(fichier).load()

    url = "https://www.screenscraper.fr/api2/jeuInfos.php?" \
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
    return url


if __name__ == "__main__":
    rom = romfile("Sonic The Hedgehog (USA, Europe).zip")
    url = urlconstruct(rom, 1)
    path = splitext(rom.name)[0] + '.xml'
    result = downloadfile(url, path)
    if result == True:
        print("download OK")
    else:
        print(result)
