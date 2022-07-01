import numpy
import os
import time
# CREATE HOUDINI NODES FOR EXPORT MATCHING PATH GENERATOR
#// TEXT OUTPUT
output_file = 'PATH_TOPs_SET.txt'
textfile_output = open(output_file, 'w')
time.sleep(1.0)

# CREATE HOUDINI NODES FOR EXPORT MATCHING PATH GENERATOR
OBJ_PATH = '''/obj/PATH/'''

start = '''obj = hou.node("/obj/")'''
OBJ_start = '''OBJ_start = hou.node("/obj/PATH/")'''
TOP_start = '''TOP_start = hou.node("/obj/topnet1/")'''
print(OBJ_start)
textfile_output.write(OBJ_start) #START
textfile_output.write('\n') # newline
print(TOP_start)
textfile_output.write(TOP_start) #START
textfile_output.write('\n') # newline
PATH_set = "BASE"
PATH_type = "TURN"
PATH_DIR = "RU"
PATH_component = "COL_side"

NODE_EXPORT_start = '''$HIP/export/$HIPNAME`_``@wedgenum``_'''
NODE_EXPORT_end = '''`.fbx'''

PYNODE_create_start = ''' = OBJ_start.createNode('rop_fbx', '''
PYNODE_create_end = ''')'''
PYNODE_param_start = '''.setParms({'sopoutput':'''
PYNODE_param_quotes = """'"""
PYNODE_param_end = '''})'''

TOPWAITNODE_create_start = ''' = TOP_start.createNode('waitforall', '''
TOPWAITNODE_create_end = ''')'''

HDANODE_create_start = ''' = TOP_start.createNode('hdaprocessor', '''
HDANODE_create_end = ''')'''
HDANODE_DIRparam_start = '''.setParms({'hdap_DIRECTIONinput':'''
HDANODE_DIRBparam_start = '''.setParms({'hdap_input':'''
HDANODE_DIRparam_end = '''})'''
HDANODE_STARTparam_start = '''.setParms({'hdap_SWITCH_START':'''
HDANODE_STARTBparam_start = '''.setParms({'hdap_START':'''
HDANODE_ENDparam_start = '''.setParms({'hdap_SWITCH_END':'''
NODE_param_start = '''.setParms({'''
NODE_param_mid = ''':'''
NODE_param_end = '''})'''
HDANODE_OUTTAG1param_start = '''.setParms({'outputtag1':'''
HDANODE_OUTFILE1param_start = '''.setParms({'outputfile1':'''
HDANODE_OUTTAG1param_start = '''.setParms({'outputtag1':'''

HDA_fileinput = "inputfile"
HDA_Base_Path = "H:/HOUDINI/ZENV/otls/z_PATH_BASE.hda"
HDA_Ledge_Path = "H:/HOUDINI/ZENV/otls/z_PATH_LEDGE.hda"

PATH_DIR_ARRAY = ["TURN_RU","TURN_UL","TURN_LD","TURN_DR","TURN_RD","TURN_UR","TURN_LU","TURN_DL"]
PATH_DIR_START_ARRAY = ["START_R","START_U","START_L","START_D"]
PATH_DIR_END_ARRAY = ["END_L","END_D","END_R","END_U"]

PATH_DIR_ARRAY = numpy.concatenate(( PATH_DIR_ARRAY , PATH_DIR_START_ARRAY , PATH_DIR_END_ARRAY ))
#PATH_DIR_ARRAY = PATH_DIR_END_ARRAY # end only
#print(PATH_DIR_ARRAY)

MAIN_set_ARRAY = []
MAIN_component_ARRY = []
MAIN_component_num_ARRY = []
#//============================ MAKE THE ARRAYS for the pieces

#BASE
PATH_BASE_set = "BASE"
PATH_BASE_component_ARRAY = ["floor","startend","COL_side","COL_floor"]
i=0
for current_BASE_component in PATH_BASE_component_ARRAY:
  MAIN_set_ARRAY.append(PATH_BASE_set)
  MAIN_component_ARRY.append(current_BASE_component)
  MAIN_component_num_ARRY.append(i)
  i+=1

#//============================
#LEDGE_CLIFF
PATH_LEDGE_set = "LEDGE_CLIFF"
PATH_LEDGE_component_ARRAY = ["floor","bot","top","distant"]
k=0
for current_LEDGE_component in PATH_LEDGE_component_ARRAY:
  MAIN_set_ARRAY.append(PATH_LEDGE_set)
  MAIN_component_ARRY.append(current_LEDGE_component)
  MAIN_component_num_ARRY.append(k)
  k+=1

#//============================
#LEDGE_CAVE_STALAG
PATH_LEDGE_set = "LEDGE_CAVE_STALAG"
PATH_LEDGE_component_ARRAY = ["floor","bot","top","distant"]
k=0
for current_LEDGE_component in PATH_LEDGE_component_ARRAY:
  MAIN_set_ARRAY.append(PATH_LEDGE_set)
  MAIN_component_ARRY.append(current_LEDGE_component)
  MAIN_component_num_ARRY.append(k)
  k+=1

#//============================
#LEDGE_FOREST
PATH_LEDGE_set = "LEDGE_FOREST"
PATH_LEDGE_component_ARRAY = ["floor","bot","top","distant"]
k=0
for current_LEDGE_component in PATH_LEDGE_component_ARRAY:
  MAIN_set_ARRAY.append(PATH_LEDGE_set)
  MAIN_component_ARRY.append(current_LEDGE_component)
  MAIN_component_num_ARRY.append(k)
  k+=1

#//============================
#LEDGE_DIFF_REACTION
PATH_LEDGE_set = "DIFF_REACTION"
PATH_LEDGE_component_ARRAY = ["floor","bot","top","distant"]
k=0
for current_LEDGE_component in PATH_LEDGE_component_ARRAY:
  MAIN_set_ARRAY.append(PATH_LEDGE_set)
  MAIN_component_ARRY.append(current_LEDGE_component)
  MAIN_component_num_ARRY.append(k)
  k+=1

#//============================
#LEDGE_POOLS
PATH_LEDGE_set = "POOLS"
PATH_LEDGE_component_ARRAY = ["floor","bot","top","distant"]
k=0
for current_LEDGE_component in PATH_LEDGE_component_ARRAY:
  MAIN_set_ARRAY.append(PATH_LEDGE_set)
  MAIN_component_ARRY.append(current_LEDGE_component)
  MAIN_component_num_ARRY.append(k)
  k+=1


#print(MAIN_set_ARRAY)
#print(MAIN_component_ARRY)

def create_tops_code_gen(createnodes , connectnodes) :
  #//============================
  # CREATE THE PYTHON CODE TO CREATE HOUDINI TOP NETWORK for PDG wedges
  #print("==========================================================================")
  #print( "TOP" )
  #print("==========================================================================")
  MAIN_set_ARRAY_short =  list(set(MAIN_set_ARRAY))
  if ( createnodes == True ):
    for current_PATH_set in MAIN_set_ARRAY_short :
      TOP_WaitNODE_name = current_PATH_set + "_HDA_wait"
      TOPWAITNODE_create_final = TOP_WaitNODE_name + TOPWAITNODE_create_start + PYNODE_param_quotes + TOP_WaitNODE_name + PYNODE_param_quotes + TOPWAITNODE_create_end
      print(TOPWAITNODE_create_final)
      textfile_output.write(TOPWAITNODE_create_final) #START
      textfile_output.write('\n') # newline

  set_top_count = 0
  for current_PATH_set in MAIN_set_ARRAY_short :
    current_PATH_component = MAIN_component_ARRY[set_top_count]
    #print("==========================================================================")
    #print( current_PATH_set + "_" + current_PATH_component )
    #print("==========================================================================")
    dir_top_count = 0

    for PATH_typedir in PATH_DIR_ARRAY :
      PATH_name = current_PATH_set + "_" + PATH_typedir + "_" + current_PATH_component
      TOP_NODE_name = PATH_name + "_TOP_export"
      HDA_NODE_name = current_PATH_set + "_" + PATH_typedir + "_HDA"
      TOP_PARAM_name = OBJ_PATH + PATH_name + "_export" 
      TOP_WaitNODE_name = current_PATH_set + "_HDA_wait"
      
      if ( createnodes == True ):
        HDANODE_create_final = HDA_NODE_name + HDANODE_create_start + PYNODE_param_quotes + HDA_NODE_name + PYNODE_param_quotes + HDANODE_create_end
        print(HDANODE_create_final)
        textfile_output.write(HDANODE_create_final) #START
        textfile_output.write('\n') # newline
      else :
        HDA_NODE_name_define = '''hou.node("/obj/topnet1/''' + HDA_NODE_name + '''")'''
        HDA_NODE_name_define_final = HDA_NODE_name + " = " + HDA_NODE_name_define
        print(HDA_NODE_name_define_final)
        textfile_output.write(HDA_NODE_name_define_final) #START
        textfile_output.write('\n') # newline
      # set HDA
      HDA_Base_Path_current = HDA_Base_Path
      if ( current_PATH_set != "BASE") :
        HDA_Base_Path_current = HDA_Ledge_Path
      HDANODE_HDAparam_final = HDA_NODE_name + NODE_param_start + PYNODE_param_quotes + "inputfile" + PYNODE_param_quotes + NODE_param_mid + PYNODE_param_quotes + HDA_Base_Path_current + PYNODE_param_quotes + NODE_param_end
      print(HDANODE_HDAparam_final)
      textfile_output.write(HDANODE_HDAparam_final) #START
      textfile_output.write('\n') # newline
      #set num outputs
      HDANODE_NUMOutparam_final = HDA_NODE_name + NODE_param_start + PYNODE_param_quotes + "numberoutputs" + PYNODE_param_quotes + NODE_param_mid + PYNODE_param_quotes + "4" + PYNODE_param_quotes + NODE_param_end
      print(HDANODE_NUMOutparam_final)
      textfile_output.write(HDANODE_NUMOutparam_final) #START
      textfile_output.write('\n') # newline

      # set direction
      HDANODE_DIRparam_final = HDA_NODE_name + HDANODE_DIRparam_start + PYNODE_param_quotes + str(dir_top_count) + PYNODE_param_quotes + NODE_param_end
      print(HDANODE_DIRparam_final)
      textfile_output.write(HDANODE_DIRparam_final) #START
      textfile_output.write('\n') # newline
      HDANODE_DIRBparam_final = HDA_NODE_name + HDANODE_DIRBparam_start + PYNODE_param_quotes + str(dir_top_count) + PYNODE_param_quotes + NODE_param_end
      print(HDANODE_DIRBparam_final)
      textfile_output.write(HDANODE_DIRBparam_final) #START
      textfile_output.write('\n') # newline

      # set starts
      if ( "START" in PATH_typedir) :
        HDANODE_STARTparam_final = HDA_NODE_name + HDANODE_STARTparam_start + PYNODE_param_quotes + "1" + PYNODE_param_quotes + NODE_param_end
        print(HDANODE_STARTparam_final)
        textfile_output.write(HDANODE_STARTparam_final) #START
        textfile_output.write('\n') # newline
        HDANODE_STARTBparam_final = HDA_NODE_name + HDANODE_STARTBparam_start + PYNODE_param_quotes + "1" + PYNODE_param_quotes + NODE_param_end
        print(HDANODE_STARTBparam_final)
        textfile_output.write(HDANODE_STARTBparam_final) #START
        textfile_output.write('\n') # newline
      # set ends
      if ( "END" in PATH_typedir) :
        HDANODE_ENDparam_final = HDA_NODE_name + HDANODE_ENDparam_start + PYNODE_param_quotes + "1" + PYNODE_param_quotes + NODE_param_end
        print(HDANODE_ENDparam_final)
        textfile_output.write(HDANODE_ENDparam_final) #START
        textfile_output.write('\n') # newline


      #set input for ledge
      if ( current_PATH_set != "BASE") :
        HDANODE_INAparam_current = "$HIP/export/$HIPNAME`_``@wedgenum``_" + "BASE" + "_" + PATH_typedir + "_" + "floor" + "`.bgeo.sc"
        HDANODE_INAparam_final = HDA_NODE_name + NODE_param_start + PYNODE_param_quotes + "hdap_INPUT_0file" + PYNODE_param_quotes + NODE_param_mid + PYNODE_param_quotes + HDANODE_INAparam_current + PYNODE_param_quotes + NODE_param_end
        print(HDANODE_INAparam_final)
        textfile_output.write(HDANODE_DIRparam_final) #START
        textfile_output.write('\n') # newline
        HDANODE_INBparam_current = "$HIP/export/$HIPNAME`_``@wedgenum``_" + "BASE" + "_" + PATH_typedir + "_" + "startend" + "`.bgeo.sc"
        HDANODE_INBparam_final = HDA_NODE_name + NODE_param_start + PYNODE_param_quotes + "hdap_INPUT_1file" + PYNODE_param_quotes + NODE_param_mid + PYNODE_param_quotes + HDANODE_INBparam_current + PYNODE_param_quotes + NODE_param_end
        print(HDANODE_INBparam_final)
        textfile_output.write(HDANODE_INBparam_final) #START
        textfile_output.write('\n') # newline

      component_sub_count = 0
      # OUTPUT FILE PARAMETERS
      for current_COMPONENT_SUB_set in PATH_LEDGE_component_ARRAY :
        #$HIP/export/$HIPNAME`_``@wedgenum``_BASE_TURN_RU_floor`.bgeo.sc
        current_COMPONENT_overide = current_COMPONENT_SUB_set
        if ( current_PATH_set == "BASE") :
          current_COMPONENT_overide = PATH_BASE_component_ARRAY[component_sub_count]

        HDANODE_OUTparam_current = "$HIP/export/$HIPNAME`_``@wedgenum``_" + current_PATH_set + "_" + PATH_typedir + "_" + current_COMPONENT_overide + "`.bgeo.sc"
        HDANODE_OUTparam_final = HDA_NODE_name + NODE_param_start + PYNODE_param_quotes + "outputfile" + str(component_sub_count+1) + PYNODE_param_quotes + NODE_param_mid + PYNODE_param_quotes + HDANODE_OUTparam_current + PYNODE_param_quotes + NODE_param_end
        print(HDANODE_OUTparam_final)
        textfile_output.write(HDANODE_OUTparam_final) #START
        textfile_output.write('\n') # newline
        component_sub_count += 1

      if ( connectnodes == True ):
        current_wait_input = dir_top_count + set_top_count
        CONNECT_TOPWAITNODE_ROP = TOP_WaitNODE_name + ".setInput( " + str(current_wait_input) + " , "  + HDA_NODE_name + " )"
        print(CONNECT_TOPWAITNODE_ROP)
        textfile_output.write(CONNECT_TOPWAITNODE_ROP) #START
        textfile_output.write('\n') # newline
      dir_top_count += 1

    set_top_count+=1 # iterate the set number in tops

# MAIN 
# CREATE TOP HDA PROCESSORS FOR EACH DIR 
# 1. CREATE NODOES - if false then only UPDATE parameters on existing
# 2. CONNECT NODES
#create_tops_code_gen(True,True)  
create_tops_code_gen(False,False)  

time.sleep(2.0)
textfile_output.close