nuke.menu( 'Nodes' ).addCommand( 'Other/L_Grain', lambda: nuke.createNode( 'L_Grain_v05' ) )
nuke.menu( 'Nodes' ).addCommand( 'Other/L_Fuse', lambda: nuke.createNode( 'L_Fuse_v06' ) )
nuke.menu( 'Nodes' ).addCommand( 'Other/ScreenCorrect', lambda: nuke.createNode( 'screenCorrect' ) )

nuke.addOnUserCreate(lambda:nuke.thisNode()['first_frame'].setValue(nuke.frame()), nodeClass='FrameHold')

m=nuke.menu('Nuke')
r=m.addMenu('CardToTrack',icon='Me.png')
r.addCommand('CardToTrack gizmo', 'nuke.createNode(\'CardToTrack\')',icon='my.png')
