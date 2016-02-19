import json
import os

def _saveParm():
    dict = {}
    
    #for node in hou.selectedNodes():     
    for node in hou.node("/obj").allSubChildren():
        
        dict[node.path()] = [{x.name():x.eval()} for x in node.parms() if x.name().startswith('shop')]
        #dict[node.name()] = [{x.name():x.eval()} for x in node.parms() if x.name().startswith('ar')]
        
    return dict            
            
xxx=_saveParm()
f_name='/home/victor/Documents/H_test/unkas_alembic_set_node_01.json'

with open(f_name, 'wb') as outfile:
    json.dump(xxx, outfile)

#print xxx
#for _name in xxx:
#    print _name, xxx[_name]
