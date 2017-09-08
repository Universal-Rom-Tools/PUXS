"""Main Script"""

from romfile import romfile
from download import downloadfile
from download import urlconstruct
from xmlreader import xmlvalue
from os.path import splitext
from os.path import join
from os import walk
import logging
import sys
import pathlib

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='log.txt', filemode='w', level=logging.DEBUG)

# this is extension you want to detect
extension = (".zip", ".gen", ".bin", ".MD")
# This is the path where you want to search
path = r'C:\Developpement\Github\roms\megadrive'

pathlib.Path(join(sys.path[0],'cache','xml')).mkdir(parents=True, exist_ok=True)
filenames = []

for root, dirs, files in walk(path):
    for file in files:
        if file.endswith(extension):
            filenames.append(join(root, file)[len(path) + 1:])

for files in filenames:
    logging.info("files : {}".format(join(path,files)))
    rom = romfile(join(path,files))
    logging.debug("parentpath : {}".format(rom.parentpath))
    logging.info("name :{}".format(rom.name))
    logging.debug("size :{}".format(rom.size))
    logging.debug("crc32 :{}".format(rom.crc32))
    logging.debug("md5 :{}".format(rom.md5))
    logging.debug("sha1 :{}".format(rom.sha1))
    url = urlconstruct(rom, 1)
    xmlpath = join(sys.path[0],'cache','xml',splitext(rom.name)[0] + '.xml')
    result = downloadfile(url, xmlpath)
    if result == True:
        logging.info("download OK")
        xmlvalue(xmlpath, 'media', '', 'jeu', 'box-2D', 'eu')
    else:
        logging.warning(result)
