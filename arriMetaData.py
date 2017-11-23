import os
import re

selectedNode = nuke.selectedNode()
nodeName = selectedNode.name()
node = nuke.toNode(nodeName)
if nuke.getNodeClassName(node) != 'Read':
    nuke.message('Please select a read Node')
    print 'Please select a read Node'

metaData = node.metadata()

FD = metaData['exr/FocusDistance']
act = metaData['exr/LensModel']

first = node.firstFrame()
last = node.lastFrame()
#ret = nuke.getFramesAndViews( 'Create Camera from Metadata', '%s-%s' %( first, last )  )
#frameRange = nuke.FrameRange( ret[0] )
#camViews = (ret[1])

#print FD, frameRange

#FD_num = re.findall(r"[-+]?\d*\.\d+|\d+",metaData['exr/FocusDistance'])

#print FD_num

cam = nuke.nodes.Camera (name="Camera %s" % act)

cam['focal_point'].setAnimated()


f = open('data.txt', 'a')

for index in range(0,300):
    frame = index
    nuke.activeViewer().frameControl(frame)
    FD_num = re.findall(r"[-+]?\d*\.\d+|\d+",node.metadata('exr/FocusDistance',index))
    print frame, FD_num[0]
    f.write(str(FD_num))	
    cam['focal_point'].setValueAt(float(FD_num[0]), frame)

f.close()
