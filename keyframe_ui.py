import maya.cmds as cmds
import keyframe_helpers
from functools import partial


def do_insert_keyframes(on_twos_cb, skip_existing_cb, force_override_cb, *args):
    skip_existing = cmds.checkBox(skip_existing_cb, q=True, value=True)
    force_override = cmds.checkBox(force_override_cb, q=True, value=True)
    
    interval=1
    if cmds.checkBox(on_twos_cb, q=True, value=True):
        interval=2
        
    keyframe_times = keyframe_helpers.get_keyframe_times(skip_existing, interval)
    keyframe_helpers.insert_keyframes(keyframe_times, force_override)

    

def display(window_name):
    if cmds.window(window_name, exists=True):
        cmds.deleteUI(window_name)
    
    window = cmds.window(window_name, title="Keyframe Tool Mini", width=270)
    column_layout = cmds.columnLayout(parent=window, adjustableColumn=True)
    on_twos_cb = cmds.checkBox(parent=column_layout, label="Add frames on 2's")                                                
    skip_existing_cb = cmds.checkBox(label="Skip existing frames", parent=column_layout)
    force_override_cb = cmds.checkBox(label="Force override on existing frames", parent=column_layout)
    
    row_layout = cmds.rowLayout(parent=window, numberOfColumns=2, adjustableColumn2=True )
    keyframe_btn = cmds.button(label="Add Keyframes", parent=row_layout)
    
    cmds.button(keyframe_btn, 
                edit=True, 
                command=partial(do_insert_keyframes, on_twos_cb, skip_existing_cb, force_override_cb))
    
    cmds.showWindow(window)    

if __name__ == "__main__":
    display("LayoutExampleUI")
    