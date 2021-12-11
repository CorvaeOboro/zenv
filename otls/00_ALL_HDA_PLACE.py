# FOR EACH HDA IN FOLDER PLACE THEM IN HOUDINI FOR QA of lib
# THIS CREATES THE PYTHON CODE TO THEN BE PASTED INTO SHELL
OBJ_start = '''OBJ_start = hou.node("/obj/ALL_HDA")'''
print(OBJ_start)
PYquotes = """'"""
HDA_path = "H:/MODELS/HOUDINI/00_OTL_DIGITALASSET/Z/otls"

NODE_create_start = """ = OBJ_start.createNode('"""
NODE_create_name = "EXAMPLE"
NODE_create_mid = """', """
NODE_create_end = ''')'''

#NODE_param_start = '''.setParms({'sopoutput':'''
#NODE_param_end = '''})'''

import os

directory = HDA_path
for filename in os.listdir(directory):
  if filename.endswith(".hda") :
    filenameonly = filename.replace('.hda', '')

    NODE_create_name = filenameonly
    NODE_name = filenameonly
    #PARAM_name = NODE_EXPORT_start + PATH_name + NODE_EXPORT_end

    PYNODE_create_final = NODE_name + NODE_create_start + NODE_create_name + NODE_create_mid + PYquotes + NODE_name + PYquotes + NODE_create_end
    #PYNODE_param_final = NODE_name + PYNODE_param_start + PYquotes + PARAM_name + PYquotes + NODE_param_end
    print(PYNODE_create_final)
    print("time.sleep(1)")