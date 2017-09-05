from puxsroms import catchssxml
from xml.etree import ElementTree

import encryptor

print(login)

# catchssxml('aof.zip', 75)
# with open('test.xml', 'rt') as f:
#     tree = ElementTree.parse(f)
#
# for node in tree.iter('media'):
#     xmlparent = node.attrib.get('parent')
#     xmltype = node.attrib.get('type')
#     xmlregion = node.attrib.get('region')
#     if xmlparent=='jeu' and xmltype=='flyer' and xmlregion=='wor':
#         print(' %s' % xmlparent)
#         print('     %s' % xmltype)
#         print('        %s' % xmlregion)
#         print('------------> %s' % node.text)