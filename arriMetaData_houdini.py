import hou

def keyParmFromFile(f, node, parmName, pasteFromFrame):
    f = open(f, 'r')
    str = f.read()
    str = [x.replace("']", "") for x in str.split("['")][1:]
    digits = [float(x) for x in str]
    
    parm = node.parm(parmName)   
    parm.deleteAllKeyframes()
    frame = pasteFromFrame
    for value in digits:
        time = (frame - 1)/hou.fps()
        parm.setKeyframe(hou.Keyframe(value, time))
        frame += 1
    f.close()


keyParmFromFile('/tmp/data_fd.txt', hou.selectedNodes()[0], 'focus', 1)
