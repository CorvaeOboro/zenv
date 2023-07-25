#//=======================================================================================
#// UNREAL PYTHON - CREATE MAPS from templates
#// run in unreal python scripts
#// for each TYPEDIR place meshes from SET matching
#// places Collision meshes from BASE set then meshes from SET
#//=======================================================================================
import unreal
import time
# duplicate a map template based on typedir
METADIR_ARRAY = ["U","D","R","L"]
#METADIR_ARRAY = ["U"] # only one dir for testing
START_ARRAY = ["START_R","START_L","START_U","START_D"]
END_ARRAY = ["END_R","END_L","END_U","END_D"]
DIR_ARRAY = ["TURN_RU","TURN_UL","TURN_LD","TURN_DR","TURN_RD","TURN_UR","TURN_LU","TURN_DL"]
STRAIGHT_ARRAY = ["STRAIGHT_R","STRAIGHT_L","STRAIGHT_U","STRAIGHT_D"]
#DIR_ARRAY = ["TURN_RU","TURN_DR","TURN_RD","TURN_UR"]
TYPEDIR_ARRAY = START_ARRAY + DIR_ARRAY + END_ARRAY + STRAIGHT_ARRAY
#SET_ARRAY = ["LEDGE_CAVE_STALAG","LEDGE_FOREST","LEDGE_CLIFF","DIFF_REACTION"]
LEDGE_component_ARRAY = ["floor","bot","top","distant","collision"]
wedge_max = 1
ATMOSPHERE_TEMPLATE = "00_ATMOSPHERE"
current_SET = "FRACTUREMEMORY"

# a list of the nodes that should be excluded from directinal groups , end piece directions are reversed
PATH_LEDGEDIRU_ANTI_ARRAY = ["TURN_LD","TURN_DR","TURN_DL","TURN_RD","START_D","END_U","STRAIGHT_D"]
PATH_LEDGEDIRD_ANTI_ARRAY = ["TURN_RU","TURN_UL","TURN_LU","TURN_UR","START_U","END_D","STRAIGHT_U"]
PATH_LEDGEDIRR_ANTI_ARRAY = ["TURN_UL","TURN_LD","TURN_LU","TURN_DL","START_L","END_R","STRAIGHT_L"]
PATH_LEDGEDIRL_ANTI_ARRAY = ["TURN_RU","TURN_DR","TURN_RD","TURN_UR","START_R","END_L","STRAIGHT_R"]

print("RUNNING UNREAL CREATE PATH SNAPMAPS")
actor_location = unreal.Vector(0.0,0.0,0.0)
actor_rotation = unreal.Rotator(0.0,0.0,0.0)

editor_file_utils = unreal.EditorLoadingAndSavingUtils()

# SPAWN ACTOR FUNCTION , SETS PARAMETERS
def spawnActor(meshpath,levelname,meshname):
  obj = unreal.load_asset(meshpath)
  temp_actor = unreal.EditorLevelLibrary.spawn_actor_from_object(obj, actor_location, actor_rotation)
  if temp_actor:
    temp_actor.rename(meshname)

  level = unreal.find_asset(levelname)
  static_meshes = unreal.GameplayStatics.get_all_actors_of_class(level, unreal.StaticMeshActor)

  for mesh in static_meshes :
    print ("current mesh = " + mesh.get_name() )
    #print(dir(mesh))
    if ( 'PATH' in mesh.get_name() ):
      print("setting not relevant for bounds")
      mesh.set_editor_property("bRelevantForLevelBounds", False)
      if ( 'collision' in mesh.get_name() ):
        print("hidden in game")
        mesh.set_editor_property("bHidden", True) 
        #mesh.SetActorHiddenInGame(True)

# CREATE ATMOPSHERE LEVEL FROM TEMPLATE IF DOESNT EXIST
atmosphere_level_to_save = '/Game/00_MAPS/ARPG/' + "ARPG_" + current_SET + "/" + "ARPG_" + current_SET + "_" + "ATMOSPHERE" 
print("ATMOSPHERE LEVEL = " + atmosphere_level_to_save)
if not unreal.EditorAssetLibrary.does_asset_exist(atmosphere_level_to_save):
  #atmosphere_template_level = unreal.EditorLevelLibrary.load_level('/Game/00_MAPS/ARPG/00_TEMPLATE/00_ATMOSPHERE')
  #atmosphere_template_level_loaded = editor_file_utils.load_map(atmosphere_template_level)
  atmosphere_template_level_loaded = editor_file_utils.load_map('/Game/00_MAPS/ARPG/00_TEMPLATE/00_ATMOSPHERE')
  level_saved = editor_file_utils.save_map(atmosphere_template_level_loaded, atmosphere_level_to_save)
#atmosphere_level_loaded = unreal.EditorLevelLibrary.load_level(atmosphere_level_to_save)
#atmosphere_level_final = unreal.EditorLevelLibrary.get_EditorWorld()



wedge_count = 0
while (wedge_count < wedge_max) : # FOR EACH WEDGE
  for current_METADIR  in METADIR_ARRAY:
    current_ANTI_LEDGEDIR_NAMES = []
    if ( "U" in current_METADIR) :
      current_ANTI_LEDGEDIR_NAMES = PATH_LEDGEDIRU_ANTI_ARRAY
    if ( "D" in current_METADIR) :
      current_ANTI_LEDGEDIR_NAMES = PATH_LEDGEDIRD_ANTI_ARRAY
    if ( "R" in current_METADIR) :
      current_ANTI_LEDGEDIR_NAMES = PATH_LEDGEDIRR_ANTI_ARRAY
    if ( "L" in current_METADIR) :
      current_ANTI_LEDGEDIR_NAMES = PATH_LEDGEDIRL_ANTI_ARRAY

    for current_DIR in TYPEDIR_ARRAY : # FOR EACH TYPE DIRECTION
      print("CURRENT_DIR = "  + str(current_DIR))
      if current_DIR not in current_ANTI_LEDGEDIR_NAMES:
        level_to_save = '/Game/00_MAPS/ARPG/' + "ARPG_" + current_SET + "/" + current_SET + "_" + current_METADIR + "_" + current_DIR + "_" + str(wedge_count)
        if not unreal.EditorAssetLibrary.does_asset_exist(level_to_save):

          level_to_load = '/Game/00_MAPS/ARPG/00_TEMPLATE/' + current_DIR
          loaded_level = editor_file_utils.load_map(level_to_load)

          level_saved = editor_file_utils.save_map(loaded_level, level_to_save)
          load_new_level = editor_file_utils.load_map(level_to_save)
          #time.sleep(10)

          # PLACE CORRESPONDING MESHES
          # BASE - no longer used
          currrent_BASEComp = "env_area_gen_A_" + str(wedge_count) + "_" + "BASE" + "_" + current_DIR + "_" 
          currrent_BASEComp_sides = currrent_BASEComp + "COL_side"
          currrent_BASEComp_floor = currrent_BASEComp + "COL_floor"
          BASEMeshComp_final = '/Game/00_MAPS/ARPG/' + "ARPG_" + "BASE" + "/env/"
          BASE_COL_sides_final  = BASEMeshComp_final + currrent_BASEComp_sides + "." + currrent_BASEComp_sides
          BASE_COL_floor_final  = BASEMeshComp_final + currrent_BASEComp_floor + "." + currrent_BASEComp_floor
          #spawnActor(BASE_COL_sides_final,level_to_save)
          #print(BASE_COL_sides_final)
          #spawnActor(BASE_COL_floor_final,level_to_save)
          #print(BASE_COL_floor_final)
          # TYPE DIRECTIONS 
          for current_COMPONENT in LEDGE_component_ARRAY :
            currrent_MeshComp = "PATH_" + str(wedge_count) + "_" + current_SET + "_" + current_METADIR + "_" + current_DIR + "_" + current_COMPONENT
            MeshComp_final = '/Game/00_MAPS/ARPG/' + "ARPG_" + current_SET + "/env/" + currrent_MeshComp + "." + currrent_MeshComp
            spawnActor(MeshComp_final,level_to_save,currrent_MeshComp)
            print(MeshComp_final)

          # Add atmosphere level 
          editor_file_utils.save_current_level()
          current_level = unreal.EditorLevelLibrary.get_editor_world()
          #level = unreal.EditorLevelLibrary.load_level('/Game/Maps/MyLevel')
          #atmosphere_level_to_save = '/Game/00_MAPS/ARPG/' + "ARPG_" + current_SET + "/" + "ARPG_" + current_SET + "_" + "ATMOSPHERE" 
          #atmosphere_level = unreal.EditorLevelLibrary.load_level(atmosphere_level_to_save)
          level_streaming_class = unreal.LevelStreamingAlwaysLoaded.static_class() # 'LevelStreamingAlwaysLoaded'
          unreal.EditorLevelUtils.add_level_to_world(current_level, atmosphere_level_to_save,level_streaming_class)
          #unreal.EditorLevelLibrary.add_level_to_world(unreal.EditorLevelUtils.get_level_world(), atmosphere_level)

          editor_file_utils.save_current_level()

  wedge_count +=1
