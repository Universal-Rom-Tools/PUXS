"""Main Script"""
from romfile import romfile
from ssdownload import downloadfile
from ssdownload import urlconstruct
from os.path import splitext
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='log.txt',level=logging.DEBUG)
rom = romfile("Sonic The Hedgehog (USA, Europe).zip")
logging.debug("parentpath : {}".format(rom.parentpath))
logging.info("name :{}".format(rom.name))
logging.debug("size :{}".format(rom.size))
logging.debug("crc32 :{}".format(rom.crc32))
logging.debug("md5 :{}".format(rom.md5))
logging.debug("sha1 :{}".format(rom.sha1))
ssurl = urlconstruct(rom,1)
ssxml = splitext(rom.name)[0] + '.xml'
result = downloadfile(ssurl, ssxml)
if result == True:
    logging.info("download OK")
else:
    logging.warning(result)
