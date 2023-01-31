# CREATES A MODULE LIST FOR SNAPMAP in DungeonArchitect 
import numpy
import os
import time

METADIR_ARRAY = ["U","D","R","L"]

START_ARRAY = ["START_R","START_L","START_U","START_D"]
END_ARRAY = ["END_R","END_L","END_U","END_D"]
STRAGHT_ARRAY = ["STRAIGHT_R","STRAIGHT_L","STRAIGHT_U","STRAIGHT_D"]
DIR_ARRAY = ["TURN_RU","TURN_UL","TURN_LD","TURN_DR","TURN_RD","TURN_UR","TURN_LU","TURN_DL"]
#DIR_ARRAY = ["TURN_RU","TURN_DR","TURN_RD","TURN_UR"]
TYPEDIR_ARRAY = START_ARRAY + DIR_ARRAY + END_ARRAY + STRAGHT_ARRAY
TYPEROOMDIR_ARRAY =  DIR_ARRAY + STRAGHT_ARRAY
#SET_ARRAY = ["LEDGE_CAVE_STALAG","LEDGE_FOREST","LEDGE_CLIFF","DIFF_REACTION"]
LEDGE_component_ARRAY = ["floor","bot","top","distant","collision"]
WEDGE_LIST = ["0"]

# ANTI LIST 
PATH_LEDGEDIRU_ANTI_ARRAY = ["TURN_LD","TURN_DR","TURN_DL","TURN_RD","START_D","END_U","STRAIGHT_D"] # NO DOWN
PATH_LEDGEDIRD_ANTI_ARRAY = ["TURN_RU","TURN_UL","TURN_LU","TURN_UR","START_U","END_D","STRAIGHT_U"] # NO UP
PATH_LEDGEDIRR_ANTI_ARRAY = ["TURN_UL","TURN_LD","TURN_LU","TURN_DL","START_L","END_R","STRAIGHT_L"] # NO LEFT
PATH_LEDGEDIRL_ANTI_ARRAY = ["TURN_RU","TURN_DR","TURN_RD","TURN_UR","START_R","END_L","STRAIGHT_R"] # NO RIGHT

# EXAMPLE LIST
#((Level="/Game/00_MAPS/ARPG/ARPG_POOLS/POOLS_TURN_RD_0.POOLS_TURN_RD_0",Category="TURN"),(Level="/Game/00_MAPS/ARPG/ARPG_POOLS/POOLS_TURN_RD_0.POOLS_TURN_RD_0",Category="TURN"))

current_SET = "LEDGEFOREST"
for current_METADIR in METADIR_ARRAY:
    output_file = 'SNAPMAP_MODULE_LIST_' + current_METADIR + '.txt'
    textfile_output = open(output_file, 'w')
    time.sleep(1.0)
    if current_METADIR == "U":
        ANTILIST = PATH_LEDGEDIRU_ANTI_ARRAY
    if current_METADIR == "D":
        ANTILIST = PATH_LEDGEDIRD_ANTI_ARRAY
    if current_METADIR == "R":
        ANTILIST = PATH_LEDGEDIRR_ANTI_ARRAY
    if current_METADIR == "L":
        ANTILIST = PATH_LEDGEDIRL_ANTI_ARRAY

    text_start = "("
    textfile_output.write(text_start) #START

    #//=============================================================
    #// TYPE ROOMS BY CATEGORY
    counter = 0
    for current_WEDGE in WEDGE_LIST:
        for current_DIR in TYPEDIR_ARRAY:
            if current_DIR not in ANTILIST:
                if counter > 0 :
                    textfile_output.write(",") # COMMA 

                leveltext_start = '''(Level="/Game/00_MAPS/ARPG/'''
                textfile_output.write(leveltext_start) #LEVEL START

                levelfolder = "ARPG_" + current_SET + "/"
                textfile_output.write(levelfolder) #LEVEL FOLDER

                level_to_save = current_SET + "_" + current_METADIR + "_" + current_DIR + "_" + str(current_WEDGE)
                textfile_output.write(level_to_save) #LEVEL NAME
                dot = '''.'''
                textfile_output.write(dot) #dot
                textfile_output.write(level_to_save) #LEVEL NAME

                doublequotes = '''",Category="'''
                textfile_output.write(doublequotes) #doublequotes
                
                category_name = "FAILED"
                if "TURN" in current_DIR :
                    category_name = "TURN"
                if "START" in current_DIR :
                    category_name = "START"
                if "END" in current_DIR:
                    category_name = "END"
                if "STRAIGHT" in current_DIR:
                    category_name = "STRAIGHT"

                textfile_output.write(category_name) #CATEGORY

                text_end = '''")'''
                textfile_output.write(text_end) #END
                counter += 1

    #//=============================================================
    #// TYPE ROOMS BY CATEGORY
    counter = 0
    for current_WEDGE in WEDGE_LIST:
        for current_DIR in TYPEROOMDIR_ARRAY:
            if current_DIR not in ANTILIST:
                #if counter > 0 :
                textfile_output.write(",") # COMMA 

                leveltext_start = '''(Level="/Game/00_MAPS/ARPG/'''
                textfile_output.write(leveltext_start) #LEVEL START

                levelfolder = "ARPG_" + current_SET + "/"
                textfile_output.write(levelfolder) #LEVEL FOLDER

                level_to_save = current_SET + "_" + current_METADIR + "_" + current_DIR + "_" + str(current_WEDGE)
                textfile_output.write(level_to_save) #LEVEL NAME
                dot = '''.'''
                textfile_output.write(dot) #dot
                textfile_output.write(level_to_save) #LEVEL NAME

                doublequotes = '''",Category="'''
                textfile_output.write(doublequotes) #doublequotes
                
                category_name = "FAILED"
                if "TURN" in current_DIR :
                    category_name = "ROOM"
                if "STRAIGHT" in current_DIR:
                    category_name = "ROOM"

                textfile_output.write(category_name) #CATEGORY

                text_end = '''")'''
                textfile_output.write(text_end) #END
                counter += 1

    finaltext_end = ''')'''
    textfile_output.write(finaltext_end) #END
    time.sleep(2.0)
    textfile_output.close
            




