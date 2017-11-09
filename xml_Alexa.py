import xml.etree.cElementTree as ET
tree = ET.ElementTree(file='/mnt/sda5/shrimo/Projects/ddog/heli_0010/A013C002_170628_R6Y8.xml')
root = tree.getroot()

for _xml in root.findall('PropertyStrings'):
    nameLT = _xml.find('LensType')
    nameAR = _xml.find('AlexaReel')
    nameWB = _xml.find('WhiteBalance')
    print nameLT.text, nameAR.text,nameWB.text,

nuke.nodes.StickyNote(label='LensType -'+nameLT.text+'\n'+" Reel - "+nameAR.text+'\n'+" WB - "+nameWB.text)
