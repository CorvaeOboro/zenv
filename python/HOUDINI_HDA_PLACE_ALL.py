# // PLACE ALL HDA
# FOR EACH HDA IN FOLDER PLACE THEM IN HOUDINI 
HDA_path = "H:/HOUDINI/ZENV/otls" # directory of hda
# //==================
import os
import time
#// TEXT OUTPUT
output_file = 'HDA_PLACE_ALL.txt'
textfile_output = open(output_file, 'w')
time.sleep(1.0)

#// START NODE
OBJ_start = '''OBJ_start = hou.node("/obj/ALL_HDA")'''
print(OBJ_start)
textfile_output.write(OBJ_start) #START
textfile_output.write('\n') # newline

PYquotes = """'"""
NODE_create_start = """ = OBJ_start.createNode('"""
NODE_create_name = "EXAMPLE" # this is overwrite by hda name
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
    textfile_output.write(PYNODE_create_final) #START
    textfile_output.write('\n') # newline
    print("time.sleep(1)")
time.sleep(2.0)
textfile_output.close