"""Main Script"""
from romfile import romfile
from download import ssdownloadfile
from download import ssurlconstruct
from xmlreader import xmlvalue
from os.path import splitext
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='log.txt', filemode='w', level=logging.DEBUG)
rom = romfile("Sonic The Hedgehog (USA, Europe).zip")
logging.debug("parentpath : {}".format(rom.parentpath))
logging.info("name :{}".format(rom.name))
logging.debug("size :{}".format(rom.size))
logging.debug("crc32 :{}".format(rom.crc32))
logging.debug("md5 :{}".format(rom.md5))
logging.debug("sha1 :{}".format(rom.sha1))
ssurl = ssurlconstruct(rom, 1)
ssxml = splitext(rom.name)[0] + '.xml'
result = ssdownloadfile(ssurl, ssxml)
if result == True:
    logging.info("download OK")
    xmlvalue(ssxml, 'media', '', 'jeu', 'box-2D', 'eu')
else:
    logging.warning(result)
