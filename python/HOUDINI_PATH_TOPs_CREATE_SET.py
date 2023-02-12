import numpy
import os
import time
# CREATE HOUDINI NODES FOR EXPORT MATCHING PATH GENERATOR
#// TEXT OUTPUT
output_file = 'PATH_TOPs_SET.txt'
textfile_output = open(output_file, 'w')
time.sleep(1.0)

#//========================================================================
# CREATE HOUDINI NODES FOR EXPORT MATCHING PATH GENERATOR
OBJ_PATH = '''/obj/PATH/'''

start = '''obj = hou.node("/obj/")'''
OBJ_start = '''OBJ_start = hou.node("/obj/PATH/")'''
TOP_start = '''TOP_start = hou.node("/obj/topnet1/")'''
WEDGE_start = '''WEDGE_start = hou.node("/obj/topnet1/wedge1")'''
print(OBJ_start)
textfile_output.write(OBJ_start) #START
textfile_output.write('\n') # newline
print(TOP_start)
textfile_output.write(TOP_start) #START
textfile_output.write('\n') # newline
textfile_output.write(WEDGE_start) #START
textfile_output.write('\n') # newline

NODE_EXPORT_start = '''$HIP/geo/`PATH_``@wedgenum``_'''
#NODE_EXPORT_start = '''$HIP/geo/$HIPNAME`_``@wedgenum``_'''
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
HDANODE_STRAIGHTparam_start = '''.setParms({'hdap_STRAIGHT':'''
NODE_param_start = '''.setParms({'''
NODE_param_mid = ''':'''
NODE_param_end = '''})'''
HDANODE_OUTTAG1param_start = '''.setParms({'outputtag1':'''
HDANODE_OUTFILE1param_start = '''.setParms({'outputfile1':'''
HDANODE_OUTTAG1param_start = '''.setParms({'outputtag1':'''

HDANODE_BASEDIRXparam_start = '''.setParms({'hdap_input_positionx':'''
HDANODE_BASEDIRZparam_start = '''.setParms({'hdap_input_positionz':'''

HDANODE_LEDGETOPDIRXparam_start = '''.setParms({'hdap_TOP_DIRECTIONinput_DIRx':'''
HDANODE_LEDGETOPDIRZparam_start = '''.setParms({'hdap_TOP_DIRECTIONinput_DIRz':'''
HDANODE_LEDGEBOTDIRXparam_start = '''.setParms({'hdap_BOT_DIRECTIONinput_DIR2x':'''
HDANODE_LEDGEBOTDIRZparam_start = '''.setParms({'hdap_BOT_DIRECTIONinput_DIR2z':'''

HDANODE_JITTERA_start = '''.setParms({'hdap_JITTERAscale':'''
HDANODE_JITTERB_start = '''.setParms({'hdap_JITTERBscale2':'''
HDANODE_JITTERC_start = '''.setParms({'hdap_JITTERCscale3':'''

HDA_fileinput = "inputfile"
#HDA_Path = "H:/HOUDINI/ZENV/hda/"
HDA_Path = "H:/MODELS/HOUDINI/00_OTL_DIGITALASSET/Z/hda/"
HDA_Base_Path = HDA_Path + "z_PATH_BASE.hda"
HDA_Ledge_Path = HDA_Path + "z_PATH_LEDGE.hda"
HDA_Ledge_Pools_Path = HDA_Path + "z_PATH_LEDGE_POOLS.hda"
HDA_Ledge_Preview_Path = HDA_Path + "z_PATH_LEDGE_POOLS.hda"
HDA_Ledge_Forest_Path = HDA_Path + "z_PATH_LEDGE_FOREST.hda"
HDA_Ledge_CaveStalag_Path = HDA_Path + "z_PATH_LEDGE_CAVE_STALAG.hda"

PATH_LEDGEDIR_ARRAY = ["U","D","R","L"] # grouped such that the opposite is missing ( U = RLU , no down ) 
PATH_LEDGEDIRU_ARRAY = ["30","-60","-30","60"]
#PATH_LEDGEDIRD_ARRAY = ["30","-60","-30","60"]
PATH_LEDGEDIRD_ARRAY = ["-30","60","30","-60"]
PATH_LEDGEDIRR_ARRAY = ["60","-30","-60","30"]
#PATH_LEDGEDIRL_ARRAY = ["60","-30","-60","30"]
PATH_LEDGEDIRL_ARRAY = ["-60","30","60","-30"]


# a list of the nodes that should be excluded from directinal groups , end piece directions are reversed
PATH_LEDGEDIRU_ANTI_ARRAY = ["TURN_LD","TURN_DR","TURN_DL","TURN_RD","START_D","END_U","STRAIGHT_D"]
PATH_LEDGEDIRD_ANTI_ARRAY = ["TURN_RU","TURN_UL","TURN_LU","TURN_UR","START_U","END_D","STRAIGHT_U"]
PATH_LEDGEDIRR_ANTI_ARRAY = ["TURN_UL","TURN_LD","TURN_LU","TURN_DL","START_L","END_R","STRAIGHT_L"]
PATH_LEDGEDIRL_ANTI_ARRAY = ["TURN_RU","TURN_DR","TURN_RD","TURN_UR","START_R","END_L","STRAIGHT_R"]

#PATH_DIR_ARRAY = ["TURN_RU","TURN_UL","TURN_LD","TURN_DR","TURN_LU","TURN_DL","TURN_RD","TURN_UR"]
PATH_DIR_ARRAY = ["TURN_RU","TURN_UL","TURN_LD","TURN_DR","TURN_RD","TURN_UR","TURN_LU","TURN_DL"]
PATH_DIR_ARRAY_NUM = ["0","1","2","3","4","5","6","7"]
PATH_DIR_START_ARRAY = ["START_R","START_U","START_L","START_D"]
PATH_DIR_START_ARRAY_NUM = ["0","1","2","3"]
PATH_DIR_END_ARRAY = ["END_L","END_D","END_R","END_U"]
PATH_DIR_END_ARRAY_NUM = ["0","1","2","3"]
PATH_DIR_STRAIGHT_ARRAY = ["STRAIGHT_R","STRAIGHT_U","STRAIGHT_L","STRAIGHT_D"]
PATH_DIR_STRAIGHT_ARRAY_NUM = ["0","1","2","3"]

PATH_DIR_ARRAY = numpy.concatenate(( PATH_DIR_ARRAY , PATH_DIR_START_ARRAY , PATH_DIR_END_ARRAY ,PATH_DIR_STRAIGHT_ARRAY ))
PATH_DIR_ARRAY_NUM = numpy.concatenate(( PATH_DIR_ARRAY_NUM , PATH_DIR_START_ARRAY_NUM , PATH_DIR_END_ARRAY_NUM ,PATH_DIR_STRAIGHT_ARRAY_NUM ))
#PATH_DIR_ARRAY = PATH_DIR_END_ARRAY # end only
#print(PATH_DIR_ARRAY)
#PATH_LEDGE_SET_ARRAY = ["LEDGECLIFF","LEDGECAVESTALAG","LEDGEFOREST","DIFFREACTION","POOLS","PREVIEW"]
#PATH_LEDGE_SET_ARRAY = ["PREVIEW"]
PATH_LEDGE_SET_ARRAY = ["LEDGE"]
#//========================================================================

MAIN_set_ARRAY = []
MAIN_component_ARRY = []
MAIN_component_num_ARRY = []
#//============================ MAKE THE ARRAYS for the pieces

#BASE
PATH_BASE_set = "BASE"
PATH_BASE_component_ARRAY = ["floor","startend","COL_side","COL_floor"]
i=0
for current_BASE_component in PATH_BASE_component_ARRAY:
  #MAIN_set_ARRAY.append(PATH_BASE_set) # disabling BASE , moved into LEDGE nodes
  MAIN_component_ARRY.append(current_BASE_component)
  MAIN_component_num_ARRY.append(i)
  i+=1

#//===============================================================================
#LEDGE SET LOOPs
for current_LEDGE_SET in PATH_LEDGE_SET_ARRAY:
  PATH_LEDGE_set = current_LEDGE_SET
  PATH_LEDGE_component_ARRAY = ["floor","bot","top","distant","collision"]
  k=0
  for current_LEDGE_component in PATH_LEDGE_component_ARRAY:
    MAIN_set_ARRAY.append(PATH_LEDGE_set)
    MAIN_component_ARRY.append(current_LEDGE_component)
    MAIN_component_num_ARRY.append(k)
    k+=1
    
print(MAIN_set_ARRAY)
print(MAIN_component_ARRY)

def create_tops_code_gen(createnodes , connectnodes) :
  #//============================
  # CREATE THE PYTHON CODE TO CREATE HOUDINI TOP NETWORK for PDG wedges
  #print("==========================================================================")
  #print( "TOP" )
  #print("==========================================================================")
  MAIN_set_ARRAY_short =  list(set(MAIN_set_ARRAY))
  if ( createnodes == True ):
    for current_PATH_set in MAIN_set_ARRAY_short :
      for PATH_ledgedir in PATH_LEDGEDIR_ARRAY :
        TOP_WaitNODE_name = current_PATH_set + "_" + PATH_ledgedir + "_HDA_wait"
        TOPWAITNODE_create_final = TOP_WaitNODE_name + TOPWAITNODE_create_start + PYNODE_param_quotes + TOP_WaitNODE_name + PYNODE_param_quotes + TOPWAITNODE_create_end
        print(TOPWAITNODE_create_final)
        textfile_output.write(TOPWAITNODE_create_final) #TOP WAIT NODE
        textfile_output.write('\n') # newline

  set_top_count = 0
  for current_PATH_set in MAIN_set_ARRAY_short :
    current_PATH_component = MAIN_component_ARRY[set_top_count]
    #print("==========================================================================")
    #print( current_PATH_set + "_" + current_PATH_component )
    #print("==========================================================================")
    ledgedir_top_count = 0
    for PATH_ledgedir in PATH_LEDGEDIR_ARRAY :
      dir_top_count = 0
      for PATH_typedir in PATH_DIR_ARRAY :
        PATH_name = current_PATH_set + "_" + PATH_ledgedir + "_" + PATH_typedir + "_" + current_PATH_component
        TOP_NODE_name = PATH_name + "_TOP_export"
        HDA_NODE_name = current_PATH_set + "_" + PATH_ledgedir + "_" + PATH_typedir + "_HDA"
        TOP_PARAM_name = OBJ_PATH + PATH_name + "_export" 
        TOP_WaitNODE_name = current_PATH_set + "_" + PATH_ledgedir + "_HDA_wait"
        
        if ( createnodes == True ):
          HDANODE_create_final = HDA_NODE_name + HDANODE_create_start + PYNODE_param_quotes + HDA_NODE_name + PYNODE_param_quotes + HDANODE_create_end
          print(HDANODE_create_final)
          textfile_output.write(HDANODE_create_final) #CREATE
          textfile_output.write('\n') # newline
          
        else :
          HDA_NODE_name_define = '''hou.node("/obj/topnet1/''' + HDA_NODE_name + '''")'''
          HDA_NODE_name_define_final = HDA_NODE_name + " = " + HDA_NODE_name_define
          print(HDA_NODE_name_define_final)
          textfile_output.write(HDA_NODE_name_define_final) #NAME EXISTING NODE
          textfile_output.write('\n') # newline
        # set HDA ====================================================================================================
        HDA_Base_Path_current = HDA_Base_Path
        if ( current_PATH_set == "BASE") :
          HDA_Base_Path_current = HDA_Base_Path
        if ( current_PATH_set == "LEDGE") :
          HDA_Base_Path_current = HDA_Ledge_Path
        if ( current_PATH_set == "POOLS") :
          HDA_Base_Path_current = HDA_Ledge_Pools_Path
        if ( current_PATH_set == "PREVIEW") :
          HDA_Base_Path_current = HDA_Ledge_Preview_Path
        if ( current_PATH_set == "LEDGEFOREST") :
          HDA_Base_Path_current = HDA_Ledge_Forest_Path
        if ( current_PATH_set == "LEDGECAVESTALAG") :
          HDA_Base_Path_current = HDA_Ledge_CaveStalag_Path
        HDANODE_HDAparam_final = HDA_NODE_name + NODE_param_start + PYNODE_param_quotes + "inputfile" + PYNODE_param_quotes + NODE_param_mid + PYNODE_param_quotes + HDA_Base_Path_current + PYNODE_param_quotes + NODE_param_end
        print(HDANODE_HDAparam_final)
        textfile_output.write(HDANODE_HDAparam_final) #HDA FILE PATH
        textfile_output.write('\n') # newline
        #set num outputs
        HDANODE_NUMOutparam_final = HDA_NODE_name + NODE_param_start + PYNODE_param_quotes + "numberoutputs" + PYNODE_param_quotes + NODE_param_mid + PYNODE_param_quotes + "5" + PYNODE_param_quotes + NODE_param_end
        print(HDANODE_NUMOutparam_final)
        textfile_output.write(HDANODE_NUMOutparam_final) #NUMBER OF OUTPUTS
        textfile_output.write('\n') # newline

        # set direction ====================================================================================================
        current_dir_from_array = PATH_DIR_ARRAY_NUM[dir_top_count]
        HDANODE_DIRparam_final = HDA_NODE_name + HDANODE_DIRparam_start + PYNODE_param_quotes + str(current_dir_from_array) + PYNODE_param_quotes + NODE_param_end
        print(HDANODE_DIRparam_final)
        textfile_output.write(HDANODE_DIRparam_final) # TOP DIRECTION NUMBER
        textfile_output.write('\n') # newline
        HDANODE_DIRBparam_final = HDA_NODE_name + HDANODE_DIRBparam_start + PYNODE_param_quotes + str(current_dir_from_array) + PYNODE_param_quotes + NODE_param_end
        print(HDANODE_DIRBparam_final)
        textfile_output.write(HDANODE_DIRBparam_final) # BOT DIRECTION
        textfile_output.write('\n') # newline

        # set BASE direction  ====================================================================================================
        #if ( current_PATH_set == "BASE") :  # now moved into ledges as well
        HDANODE_BASEDirparamX = HDA_NODE_name + HDANODE_BASEDIRXparam_start + PYNODE_param_quotes + str(30) + PYNODE_param_quotes + NODE_param_end
        textfile_output.write(HDANODE_BASEDirparamX) #X
        textfile_output.write('\n') # newline
        HDANODE_BASEDirparamZ = HDA_NODE_name + HDANODE_BASEDIRZparam_start + PYNODE_param_quotes + str(30) + PYNODE_param_quotes + NODE_param_end
        textfile_output.write(HDANODE_BASEDirparamZ) #X
        textfile_output.write('\n') # newline

        # set ledgedir TOP BOT vectors  ====================================================================================================
        if ( "U" in PATH_ledgedir) :
          current_LEDGEDIR_NUM = PATH_LEDGEDIRU_ARRAY
        if ( "D" in PATH_ledgedir) :
          current_LEDGEDIR_NUM = PATH_LEDGEDIRD_ARRAY
        if ( "R" in PATH_ledgedir) :
          current_LEDGEDIR_NUM = PATH_LEDGEDIRR_ARRAY
        if ( "L" in PATH_ledgedir) :
          current_LEDGEDIR_NUM = PATH_LEDGEDIRL_ARRAY
        if ( current_PATH_set != "BASE") :
          HDANODE_LedgeDirparam_finalA = HDA_NODE_name + HDANODE_LEDGETOPDIRXparam_start + PYNODE_param_quotes + str(current_LEDGEDIR_NUM[0]) + PYNODE_param_quotes + NODE_param_end
          HDANODE_LedgeDirparam_finalB = HDA_NODE_name + HDANODE_LEDGETOPDIRZparam_start + PYNODE_param_quotes + str(current_LEDGEDIR_NUM[1]) + PYNODE_param_quotes + NODE_param_end
          HDANODE_LedgeDirparam_finalC = HDA_NODE_name + HDANODE_LEDGEBOTDIRXparam_start + PYNODE_param_quotes + str(current_LEDGEDIR_NUM[2]) + PYNODE_param_quotes + NODE_param_end
          HDANODE_LedgeDirparam_finalD = HDA_NODE_name + HDANODE_LEDGEBOTDIRZparam_start + PYNODE_param_quotes + str(current_LEDGEDIR_NUM[3]) + PYNODE_param_quotes + NODE_param_end
          #print(HDANODE_LedgeDirparam_final)
          textfile_output.write(HDANODE_LedgeDirparam_finalA) #X
          textfile_output.write('\n') # newline
          textfile_output.write(HDANODE_LedgeDirparam_finalB) #Z
          textfile_output.write('\n') # newline
          textfile_output.write(HDANODE_LedgeDirparam_finalC) #X
          textfile_output.write('\n') # newline
          textfile_output.write(HDANODE_LedgeDirparam_finalD) #Z
          textfile_output.write('\n') # newline

        # set starts ====================================================================================================
        if ( "START" in PATH_typedir) :
          HDANODE_STARTparam_final = HDA_NODE_name + HDANODE_STARTparam_start + PYNODE_param_quotes + "1" + PYNODE_param_quotes + NODE_param_end
          print(HDANODE_STARTparam_final)
          textfile_output.write(HDANODE_STARTparam_final) #START
          textfile_output.write('\n') # newline
          HDANODE_STARTBparam_final = HDA_NODE_name + HDANODE_STARTBparam_start + PYNODE_param_quotes + "1" + PYNODE_param_quotes + NODE_param_end
          print(HDANODE_STARTBparam_final)
          textfile_output.write(HDANODE_STARTBparam_final) #START B
          textfile_output.write('\n') # newline
        # set ends ====================================================================================================
        if ( "END" in PATH_typedir) :
          HDANODE_ENDparam_final = HDA_NODE_name + HDANODE_ENDparam_start + PYNODE_param_quotes + "1" + PYNODE_param_quotes + NODE_param_end
          print(HDANODE_ENDparam_final)
          textfile_output.write(HDANODE_ENDparam_final) #END
          textfile_output.write('\n') # newline
          HDANODE_STARTparam_final = HDA_NODE_name + HDANODE_STARTparam_start + PYNODE_param_quotes + "1" + PYNODE_param_quotes + NODE_param_end
          print(HDANODE_STARTparam_final)
          textfile_output.write(HDANODE_STARTparam_final) #START
          textfile_output.write('\n') # newline
          HDANODE_STARTBparam_final = HDA_NODE_name + HDANODE_STARTBparam_start + PYNODE_param_quotes + "1" + PYNODE_param_quotes + NODE_param_end
          print(HDANODE_STARTBparam_final)
          textfile_output.write(HDANODE_STARTBparam_final) #START B
          textfile_output.write('\n') # newline
        # set STRAIGHT ====================================================================================================
        if ( "STRAIGHT" in PATH_typedir) :
          HDANODE_STARTparam_final = HDA_NODE_name + HDANODE_STRAIGHTparam_start + PYNODE_param_quotes + "1" + PYNODE_param_quotes + NODE_param_end
          print(HDANODE_STARTparam_final)
          textfile_output.write(HDANODE_STARTparam_final) #START
          textfile_output.write('\n') # newline
          #if ( current_PATH_set == "BASE") :
          HDANODE_BASEDirparamX = HDA_NODE_name + HDANODE_BASEDIRXparam_start + PYNODE_param_quotes + str(0) + PYNODE_param_quotes + NODE_param_end
          textfile_output.write(HDANODE_BASEDirparamX) #X
          textfile_output.write('\n') # newline
          HDANODE_BASEDirparamZ = HDA_NODE_name + HDANODE_BASEDIRZparam_start + PYNODE_param_quotes + str(50) + PYNODE_param_quotes + NODE_param_end
          textfile_output.write(HDANODE_BASEDirparamZ) #Z
          textfile_output.write('\n') # newline
          # JITTER - STRAIGHT
          HDANODE_JITTERAparam = HDA_NODE_name + HDANODE_JITTERA_start + PYNODE_param_quotes + str(5) + PYNODE_param_quotes + NODE_param_end
          textfile_output.write(HDANODE_JITTERAparam) #Z
          textfile_output.write('\n') # newline
          HDANODE_JITTERBparam = HDA_NODE_name + HDANODE_JITTERB_start + PYNODE_param_quotes + str(4) + PYNODE_param_quotes + NODE_param_end
          textfile_output.write(HDANODE_JITTERBparam) #Z
          textfile_output.write('\n') # newline
          HDANODE_JITTERCparam = HDA_NODE_name + HDANODE_JITTERC_start + PYNODE_param_quotes + str(3.3) + PYNODE_param_quotes + NODE_param_end
          textfile_output.write(HDANODE_JITTERCparam) #Z
          textfile_output.write('\n') # newline


        #set input for ledge ====================================================================================================
        # // DISABLED now that base is in ledge nodes
        if ( current_PATH_set != "BASE") :
          HDANODE_FileInput_ON = HDA_NODE_name + '.setParms({\'hdap_FILE_INPUT_ONinput3\':' + PYNODE_param_quotes + "1" + PYNODE_param_quotes + NODE_param_end
          #print(HDANODE_FileInput_ON)
          #textfile_output.write(HDANODE_FileInput_ON) #FILE INPUT ON
          #textfile_output.write('\n') # newline
          HDANODE_INAparam_current = NODE_EXPORT_start + "BASE" + "_" + PATH_ledgedir+ "_" + PATH_typedir + "_" + "floor" + "`.bgeo.sc"
          HDANODE_INAparam_final = HDA_NODE_name + NODE_param_start + PYNODE_param_quotes + "hdap_INPUT_0file" + PYNODE_param_quotes + NODE_param_mid + PYNODE_param_quotes + HDANODE_INAparam_current + PYNODE_param_quotes + NODE_param_end
          #print(HDANODE_INAparam_final)
          #textfile_output.write(HDANODE_INAparam_final) #FILE INPUT 0 FLOOR
          #textfile_output.write('\n') # newline
          HDANODE_INBparam_current = NODE_EXPORT_start + "BASE" + "_" + PATH_ledgedir + "_" + PATH_typedir + "_" + "startend" + "`.bgeo.sc"
          HDANODE_INBparam_final = HDA_NODE_name + NODE_param_start + PYNODE_param_quotes + "hdap_INPUT_1file" + PYNODE_param_quotes + NODE_param_mid + PYNODE_param_quotes + HDANODE_INBparam_current + PYNODE_param_quotes + NODE_param_end
          #print(HDANODE_INBparam_final)
          #textfile_output.write(HDANODE_INBparam_final) #FILE INPUT 1 STARTEND
          #textfile_output.write('\n') # newline

        component_sub_count = 0
        # OUTPUT FILE PARAMETERS ====================================================================================================
        while component_sub_count < 6:

          if ( current_PATH_set == "BASE") :
            if component_sub_count >= len(PATH_BASE_component_ARRAY):
              break
            current_COMPONENT_overide = PATH_BASE_component_ARRAY[component_sub_count]
          if ( current_PATH_set != "BASE") :
            if component_sub_count >= len(PATH_LEDGE_component_ARRAY):
              break
            current_COMPONENT_overide = PATH_LEDGE_component_ARRAY[component_sub_count]

          HDANODE_OUTparam_current = NODE_EXPORT_start + current_PATH_set + "_" + PATH_ledgedir + "_"  + PATH_typedir + "_" + current_COMPONENT_overide + "`.bgeo.sc"
          HDANODE_OUTparam_final = HDA_NODE_name + NODE_param_start + PYNODE_param_quotes + "outputfile" + str(component_sub_count+1) + PYNODE_param_quotes + NODE_param_mid + PYNODE_param_quotes + HDANODE_OUTparam_current + PYNODE_param_quotes + NODE_param_end
          print(HDANODE_OUTparam_final)
          textfile_output.write(HDANODE_OUTparam_final) #START
          textfile_output.write('\n') # newline
          component_sub_count += 1

        if ( connectnodes == True ):
          current_wait_input = dir_top_count + set_top_count + ledgedir_top_count
          CONNECT_TOPWAITNODE_ROP = TOP_WaitNODE_name + ".setInput( " + str(current_wait_input) + " , "  + HDA_NODE_name + " )"
          print(CONNECT_TOPWAITNODE_ROP)
          textfile_output.write(CONNECT_TOPWAITNODE_ROP) #START
          textfile_output.write('\n') # newline
          CONNECT_WEDGENODE = HDA_NODE_name + ".setInput( " + "0" + " , "  + "WEDGE_start" + " )"
          print(CONNECT_WEDGENODE)
          textfile_output.write(CONNECT_WEDGENODE) #START
          textfile_output.write('\n') # newline
        dir_top_count += 1
      ledgedir_top_count += 1

    set_top_count+=1 # iterate the set number in tops


def delete_unused_nodes():

  PATH_BASE = ["BASE"]
  PATH_DIR_ARRAY = numpy.concatenate((PATH_LEDGE_SET_ARRAY , PATH_BASE ))

  for current_PATH_set in PATH_DIR_ARRAY:
    for current_MAINDIR in PATH_LEDGEDIR_ARRAY:
      current_ANTI_LEDGEDIR_NAMES = []
      if ( "U" in current_MAINDIR) :
        current_ANTI_LEDGEDIR_NAMES = PATH_LEDGEDIRU_ANTI_ARRAY
      if ( "D" in current_MAINDIR) :
        current_ANTI_LEDGEDIR_NAMES = PATH_LEDGEDIRD_ANTI_ARRAY
      if ( "R" in current_MAINDIR) :
        current_ANTI_LEDGEDIR_NAMES = PATH_LEDGEDIRR_ANTI_ARRAY
      if ( "L" in current_MAINDIR) :
        current_ANTI_LEDGEDIR_NAMES = PATH_LEDGEDIRL_ANTI_ARRAY

      for current_ANTItypedir in current_ANTI_LEDGEDIR_NAMES:
        ANTIHDA_NODE_name = current_PATH_set + "_" + current_MAINDIR + "_" + current_ANTItypedir + "_HDA"
        HDANODE_DELETE = ANTIHDA_NODE_name + ".destroy()"
        textfile_output.write(HDANODE_DELETE) #START
        textfile_output.write('\n') # newline



# MAIN 
# CREATE TOP HDA PROCESSORS FOR EACH DIR 
# 1. CREATE NODOES - if false then only UPDATE parameters on existing
# 2. CONNECT NODES
#create_tops_code_gen(True,True)  
create_tops_code_gen(False,False)  
delete_unused_nodes()
time.sleep(2.0)
textfile_output.close