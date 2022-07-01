#//=======================================================================================
#// UNREAL PYTHON - CREATE MAPS from templates for each TYPEDIR place meshes from SET matching
#// places Collision meshes from BASE set then meshes from SET
#//=======================================================================================
# duplicate a map template based on typedir
START_ARRAY = ["START_R","START_L","START_U","START_D"]
END_ARRAY = ["END_R","END_L","END_U","END_D"]
DIR_ARRAY = ["TURN_RU","TURN_UL","TURN_LD","TURN_DR","TURN_RD","TURN_UR","TURN_LU","TURN_DL"]
#DIR_ARRAY = ["TURN_RU","TURN_DR","TURN_RD","TURN_UR"]
TYPEDIR_ARRAY = START_ARRAY + DIR_ARRAY + END_ARRAY 
SET_ARRAY = ["LEDGE_CAVE_STALAG","LEDGE_FOREST","LEDGE_CLIFF","DIFF_REACTION"]
LEDGE_component_ARRAY = ["floor","bot","top","distant"]
wedge_max = 2

import unreal
import time
actor_location = unreal.Vector(0.0,0.0,0.0)
actor_rotation = unreal.Rotator(0.0,0.0,0.0)

editor_file_utils = unreal.EditorLoadingAndSavingUtils()

def spawnActor(meshpath,levelname):
  obj = unreal.load_asset(meshpath)
  unreal.EditorLevelLibrary.spawn_actor_from_object(obj, actor_location, actor_rotation)

  level = unreal.find_asset(levelname)
  static_meshes = unreal.GameplayStatics.get_all_actors_of_class(level, unreal.StaticMeshActor)

  for mesh in static_meshes :
    print (mesh.get_name() )
    #print(dir(mesh))
    if ( 'area_gen' in mesh.get_name() ):
      mesh.set_editor_property("bRelevantForLevelBounds", False)
      if ( 'COL' in mesh.get_name() ):
        mesh.set_editor_property("bHidden", True) 

wedge_count = 0
while (wedge_count < wedge_max) : # FOR EACH WEDGE
  current_SET = "LEDGE_CAVE_STALAG"
  for current_DIR in TYPEDIR_ARRAY : # FOR EACH TYPE DIRECTION
    level_to_load = '/Game/00_MAPS/ARPG/00_TEMPLATE/' + current_DIR
    loaded_level = editor_file_utils.load_map(level_to_load)

    level_to_save = '/Game/00_MAPS/ARPG/' + "ARPG_" + current_SET + "/" + current_SET + "_" + current_DIR + "_" + str(wedge_count)
    level_saved = editor_file_utils.save_map(loaded_level, level_to_save)
    load_new_level = editor_file_utils.load_map(level_to_save)
    #time.sleep(10)

    # PLACE CORRESPONDING MESHES
    # BASE 
    currrent_BASEComp = "env_area_gen_A_" + str(wedge_count) + "_" + "BASE" + "_" + current_DIR + "_" 
    currrent_BASEComp_sides = currrent_BASEComp + "COL_side"
    currrent_BASEComp_floor = currrent_BASEComp + "COL_floor"
    BASEMeshComp_final = '/Game/00_MAPS/ARPG/' + "ARPG_" + "BASE" + "/env/"
    BASE_COL_sides_final  = BASEMeshComp_final + currrent_BASEComp_sides + "." + currrent_BASEComp_sides
    BASE_COL_floor_final  = BASEMeshComp_final + currrent_BASEComp_floor + "." + currrent_BASEComp_floor
    spawnActor(BASE_COL_sides_final,level_to_save)
    print(BASE_COL_sides_final)
    spawnActor(BASE_COL_floor_final,level_to_save)
    print(BASE_COL_floor_final)
    # TYPE DIRECTIONS 
    for current_COMPONENT in LEDGE_component_ARRAY :
      currrent_MeshComp = "env_area_gen_A_" + str(wedge_count) + "_" + current_SET + "_" + current_DIR + "_" + current_COMPONENT
      MeshComp_final = '/Game/00_MAPS/ARPG/' + "ARPG_" + current_SET + "/env/" + currrent_MeshComp + "." + currrent_MeshComp
      spawnActor(MeshComp_final,level_to_save)
      print(MeshComp_final)
    editor_file_utils.save_current_level()

  wedge_count +=1
