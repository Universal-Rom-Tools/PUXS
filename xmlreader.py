"""Read XML information from ScreenScraper XML"""

from xml.etree import ElementTree
import logging

logging.basicConfig(format='%(asctime)s - %(levelname)s - (XML) - %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p',filename='logXML.txt',level=logging.DEBUG)

def xmlvalue(xmlfile, xmlnode, xmlid='', xmlparent='', xmltype='', xmlregion='', xmllangue=''):
    """
    this function return the XML value or nothing from ScreenScraper XML
    """
    with open(xmlfile, 'rt') as hxmlfile:
        xmltree = ElementTree.parse(hxmlfile)

    for node in xmltree.iter(xmlnode):
        attribid = node.attrib.get('id')
        attribparent = node.attrib.get('parent')
        attribtype = node.attrib.get('type')
        attribregion = node.attrib.get('region')
        attriblangue = node.attrib.get('langue')

        if (xmlid == '' or attribid == xmlid) and \
                (xmlparent == '' or attribparent == xmlparent) and \
                (xmltype == '' or attribtype == xmltype) and \
                (xmlregion == '' or attribregion == xmlregion) and \
                (xmllangue == '' or attriblangue == xmllangue):
            logging.debug("id = {}".format(attribid))
            logging.debug("parent = {}".format(attribparent))
            logging.debug("type = {}".format(attribtype))
            logging.debug("region = {}".format(attribregion))
            logging.debug("langue = {}".format(attriblangue))
            logging.info("------------> {}".format(node.text))

if __name__ == "__main__":
    xmlvalue('Sonic The Hedgehog (USA, Europe).xml', 'media','','jeu','box-2D','eu')