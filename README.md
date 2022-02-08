## ZENV ##
- collection of houdini tools , hda's focused on procedural modelling environments .
- an open source work in progress , many thanks to the other libraries and tutorials .

## TOOLS ##

## LAYOUT ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK_icon.png" width = "40" height = "40"/> **[z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK](https://github.com/corvaeoboro/zenv/)** : copy variants by piecenum attribute with collision checks
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COPY_MESH_ALONG_CURVE_DEFORM_icon.png" width = "40" height = "40"/> **[z_COPY_MESH_ALONG_CURVE_DEFORM](https://github.com/corvaeoboro/zenv/)** : pipe / wire curvedeform for houdini engine . copies input mesh without stretching along a curve , options to add cuts for smoother bending , can project normals outward from curve ,
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COPY_TO_EVENLY_DISTRIBUTED_GRID_icon.png" width = "40" height = "40"/> **[z_COPY_TO_EVENLY_DISTRIBUTED_GRID](https://github.com/corvaeoboro/zenv/)** : copy by piecenum to dynamic evenly spaced grid - used for baking and reviewing generated piecenums 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TILE_4m_icon.png" width = "40" height = "40"/> **[z_TILE_4m](https://github.com/corvaeoboro/zenv/)** : copies input to each of the 9 quarants preview tiling for texture over specific distance ( 4m default )
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TRANSFORM_ITERATE_COLLISION_CHECK_icon.png" width = "40" height = "40"/> **[z_TRANSFORM_ITERATE_COLLISION_CHECK](https://github.com/corvaeoboro/zenv/)** : move pieces towards goal while avoid itersection and collision ( simple gravity but sop based )
## CREATE ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_HELIX_ROOTS_icon.png" width = "40" height = "40"/> **[z_GEN_HELIX_ROOTS](https://github.com/corvaeoboro/zenv/)** : fixed uv generation for 1x2 texture uv set and lightmap uv set

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_BRICKMAIN_01_icon.png" width = "40" height = "40"/> **[z_GEN_BRICKMAIN_01](https://github.com/corvaeoboro/zenv/)** : stone brick variation generator , for game ready stone bricks to be placed
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DIFFERENTIAL_REACTION_TUBES_icon.png" width = "40" height = "40"/> **[z_DIFFERENTIAL_REACTION_TUBES](https://github.com/corvaeoboro/zenv/)** : fill mesh with intestine brain like tubes based on simulated diffusion chemical reaction
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURL_LINES_LOOP_icon.png" width = "40" height = "40"/> **[z_CURL_LINES_LOOP](https://github.com/corvaeoboro/zenv/)** : create lines curling around the mesh using curlnoise deforming the mesh topology 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_PETAL_FORM_icon.png" width = "40" height = "40"/> **[z_GEN_PETAL_FORM](https://github.com/corvaeoboro/zenv/)** : generate petal from curve backbone and multiple warped elipse curves defining the shape changes over the length of the backbone 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DRIP_GRUNGE_icon.png" width = "40" height = "40"/> **[z_DRIP_GRUNGE](https://github.com/corvaeoboro/zenv/)** : drip grunge under overhangs , longer when near more drip neighboors
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_VINES_WITH_LEAVES_icon.png" width = "40" height = "40"/> **[z_GEN_VINES_WITH_LEAVES](https://github.com/corvaeoboro/zenv/)** : added point outputs leaves with transform parameter  for exporting the transfering to other projects ( game editor instancing )

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_REVOLVE_BASIC_icon.png" width = "40" height = "40"/> **[z_GEN_REVOLVE_BASIC](https://github.com/corvaeoboro/zenv/)** : create revolved mesh path deformed to backbone curve , input profile and backbone curves , first try at adaptive resample resolution based on bounds

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_STAIRWAY_icon.png" width = "40" height = "40"/> **[z_GEN_STAIRWAY](https://github.com/corvaeoboro/zenv/)** : generate stairway made of bricks 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURL_LINES_THEN_PLACE_SPIRALS_icon.png" width = "40" height = "40"/> **[z_CURL_LINES_THEN_PLACE_SPIRALS](https://github.com/corvaeoboro/zenv/)** : creates curllines on the surface of mesh then copies spirals to the geometry with collision detection
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_CIRCLES_RADIATE_PATTERN_icon.png" width = "40" height = "40"/> **[z_GEN_CIRCLES_RADIATE_PATTERN](https://github.com/corvaeoboro/zenv/)** : create circular patterns inspired by asian design . scatter circles , then radiate those circles outward while avoiding intersection by order or generation . 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_STONE_BRICK_CIRCLE_icon.png" width = "40" height = "40"/> **[z_GEN_STONE_BRICK_CIRCLE](https://github.com/corvaeoboro/zenv/)** : generate a circular shaped brick section by evenly voronoi fracturing and extruding toward center . applies additional noise and separation to resemble stone 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_MOSS_HANGING_icon.png" width = "40" height = "40"/> **[z_GEN_MOSS_HANGING](https://github.com/corvaeoboro/zenv/)** : fixed uv sets and vertex colors

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_HELIX_ALONG_CURVE_icon.png" width = "40" height = "40"/> **[z_HELIX_ALONG_CURVE](https://github.com/corvaeoboro/zenv/)** : creates environment mesh for isometric snapmap pieces , used with PATH_BASE as its inputs for PDG
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_PATH_LEDGE_icon.png" width = "40" height = "40"/> **[z_PATH_LEDGE](https://github.com/corvaeoboro/zenv/)** : input curve to get helix curve around / along it 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURVE_FROM_TUBE_icon.png" width = "40" height = "40"/> **[z_CURVE_FROM_TUBE](https://github.com/corvaeoboro/zenv/)** : centered curve from mesh ( even if mesh has nonuniform topo )
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURVES_FROM_UV_ISLANDS_icon.png" width = "40" height = "40"/> **[z_CURVES_FROM_UV_ISLANDS](https://github.com/corvaeoboro/zenv/)** : for each uv island create a line curve aligned by the longest angle or vertical\horizontal . useful for generating tree branch curves from existing low poly trees

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_VINES_GUIDED_icon.png" width = "40" height = "40"/> **[z_GEN_VINES_GUIDED](https://github.com/corvaeoboro/zenv/)** : generate a vine tube using a wandering path finder guided variably by a curve and other forces like a universal direction 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_PATH_BASE_icon.png" width = "40" height = "40"/> **[z_PATH_BASE](https://github.com/corvaeoboro/zenv/)** : create a path floor section and collision for gameplay , creates directional variants for snapmap . this is the basis for all other path generation 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_WIRE_OVERLAPING_OFFSET_icon.png" width = "40" height = "40"/> **[z_WIRE_OVERLAPING_OFFSET](https://github.com/corvaeoboro/zenv/)** : creates wires rayed to ground , properly overlapping . input curves and collision 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TUBE_MESH_BETWEEN_TO_CIRCLES_icon.png" width = "40" height = "40"/> **[z_TUBE_MESH_BETWEEN_TO_CIRCLES](https://github.com/corvaeoboro/zenv/)** : input 2 circles , create a cyllinder between them 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_PILLAR_icon.png" width = "40" height = "40"/> **[z_GEN_PILLAR](https://github.com/corvaeoboro/zenv/)** : generate pillar - holding multiple brick generators and circle brick generators assembled to create a full pillar .
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_ROCK_4m_icon.png" width = "40" height = "40"/> **[z_GEN_ROCK_4m](https://github.com/corvaeoboro/zenv/)** : generates simple rock , setup for pdg 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_TUBES_FINDPATHS_FROM_CURVE_icon.png" width = "40" height = "40"/> **[z_GEN_TUBES_FINDPATHS_FROM_CURVE](https://github.com/corvaeoboro/zenv/)** : generates tubes that procedurally find a path to not intersect other tubes following along the length of a guide curve
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_SWORD_FROM_IMAGE_icon.png" width = "40" height = "40"/> **[z_GEN_SWORD_FROM_IMAGE](https://github.com/corvaeoboro/zenv/)** : create a sword from image , traces png alpha  , orients vertically , and thickens from center internal line , sets uvs to match image and bakes colors to vertex colors

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_TREE_TUBE_PATHFIND_icon.png" width = "40" height = "40"/> **[z_GEN_TREE_TUBE_PATHFIND](https://github.com/corvaeoboro/zenv/)** : generate a tree using shortest path thru curves scattered and connected around collision objects and previous tree roots
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_CRACK_BRANCHING_icon.png" width = "40" height = "40"/> **[z_GEN_CRACK_BRANCHING](https://github.com/corvaeoboro/zenv/)** : creates branching crack mesh used for booleaning other meshes
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_GIZMO_icon.png" width = "40" height = "40"/> **[z_GEN_GIZMO](https://github.com/corvaeoboro/zenv/)** : axis gizmo for debug
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GLASS_BOOLEAN_icon.png" width = "40" height = "40"/> **[z_GLASS_BOOLEAN](https://github.com/corvaeoboro/zenv/)** : input mesh with irregular shaped hole , creates an intersection plane that conforms to the opening and adds inset with vertex colors for glass shader
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_LATTICE_GRIDMESH_icon.png" width = "40" height = "40"/> **[z_GEN_LATTICE_GRIDMESH](https://github.com/corvaeoboro/zenv/)** : generate a box of grids with interior points ideal for use as a lattice deformer 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UE4_PATH_2SPLINE_COLLISION_icon.png" width = "40" height = "40"/> **[z_UE4_PATH_2SPLINE_COLLISION](https://github.com/corvaeoboro/zenv/)** : input two curves defining the border of a path , creates geometry to match , useful for quickly applying collision to organic pathways in ue4
## MODIFY ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VORONI_FRACTURE_GRADIENT_OFFSET_icon.png" width = "40" height = "40"/> **[z_VORONI_FRACTURE_GRADIENT_OFFSET](https://github.com/corvaeoboro/zenv/)** : voronoi fractures then offsets by multiple world space gradients . common tool for rock like shapes
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DEFORM_BY_HELIX_icon.png" width = "40" height = "40"/> **[z_DEFORM_BY_HELIX](https://github.com/corvaeoboro/zenv/)** : added output for the curves , to use for secondary polywires or to atrtransfr

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_SUBTRACT_COLLAPSE_END_icon.png" width = "40" height = "40"/> **[z_MESH_SUBTRACT_COLLAPSE_END](https://github.com/corvaeoboro/zenv/)** : simple boolean subtract with option to collapse . useful for quick edits in ue4 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DEFORM_BY_AXIS_icon.png" width = "40" height = "40"/> **[z_DEFORM_BY_AXIS](https://github.com/corvaeoboro/zenv/)** : bounding box ramp deformation , using multi axes \ multiple ramps
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_NOISE_DISPLACE_MASKED_icon.png" width = "40" height = "40"/> **[z_NOISE_DISPLACE_MASKED](https://github.com/corvaeoboro/zenv/)** : using vex attribute noise with presets apply noise to hi poly mesh surface 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_WRAP_DEFORM_BY_UV_icon.png" width = "40" height = "40"/> **[z_MESH_WRAP_DEFORM_BY_UV](https://github.com/corvaeoboro/zenv/)** : deform mesh to another mesh by using the flattened UVs , useful to wrap a pattern around another
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_SURFACE_SIMPLE_REMESH_icon.png" width = "40" height = "40"/> **[z_MESH_SURFACE_SIMPLE_REMESH](https://github.com/corvaeoboro/zenv/)** : mesh surface simple remesh ray projects a grid unto the input geo and remeshes then reduces , helpful for fixing chaotic geo and non manifold errors , voxelization is ideal for closed geo this method is helpful for surface shell geo

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_PLANARIZE_MULTIPLE_SURFACES_icon.png" width = "40" height = "40"/> **[z_PLANARIZE_MULTIPLE_SURFACES](https://github.com/corvaeoboro/zenv/)** : added second example for rock gen using planarize , increased max piece size

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_CHIP_CRACKED_icon.png" width = "40" height = "40"/> **[z_MESH_CHIP_CRACKED](https://github.com/corvaeoboro/zenv/)** : boolean subtract chipping and crack meshes onto the surface based on curvature and fit projecting the crack meshes .
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CONFORM_INTERSECTING_LERP_icon.png" width = "40" height = "40"/> **[z_CONFORM_INTERSECTING_LERP](https://github.com/corvaeoboro/zenv/)** : added paramters , now focused on conforming around a given colllision object based on it intersection

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_SLICER_SAVE_icon.png" width = "40" height = "40"/> **[z_MESH_SLICER_SAVE](https://github.com/corvaeoboro/zenv/)** : separates large meshes into grided sections and exports them to fbx , options for specific area exports , and compatible with houdini engine .  
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MASK_TO_LINE_icon.png" width = "40" height = "40"/> **[z_MASK_TO_LINE](https://github.com/corvaeoboro/zenv/)** : input blured mask of color channel from an image , output a single polypath line , useful for converting guide lines from annotated images such as before proportional adjustments or realignment of input images based on the mask

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_STAMP_FOREACH_PIECE_icon.png" width = "40" height = "40"/> **[z_STAMP_FOREACH_PIECE](https://github.com/corvaeoboro/zenv/)** : randomized boolean of one mesh on to the surface of variants . useful for cutting designs into bricks
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SMOOTHING_FROM_UVs_icon.png" width = "40" height = "40"/> **[z_SMOOTHING_FROM_UVs](https://github.com/corvaeoboro/zenv/)** : hard edges by uv island  for baking 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VARIATION_DIRECTIONS_icon.png" width = "40" height = "40"/> **[z_VARIATION_DIRECTIONS](https://github.com/corvaeoboro/zenv/)** : cycle thru 90 degree rotations and mirrored variantions  . for use with path tool
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SPLIT_CLIP_CREVISE_icon.png" width = "40" height = "40"/> **[z_SPLIT_CLIP_CREVISE](https://github.com/corvaeoboro/zenv/)** : separate the input into two outputs with an indent along the separation , useful separating environment shell into terraced layers
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CUT_INTERSECT_DARKEN_icon.png" width = "40" height = "40"/> **[z_CUT_INTERSECT_DARKEN](https://github.com/corvaeoboro/zenv/)** : darken a surface from the intersections of other objects , with option to boolean those cuts in
## REMOVAL ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REMOVE_PIECES_BY_VOLUME_icon.png" width = "40" height = "40"/> **[z_REMOVE_PIECES_BY_VOLUME](https://github.com/corvaeoboro/zenv/)** : for each connected element , remove if doesnt match min or max measured volume , also has options of perimeter or other measurements
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_KEEP_ONLY_LARGEST_CONNECTED_ELEMENT_icon.png" width = "40" height = "40"/> **[z_KEEP_ONLY_LARGEST_CONNECTED_ELEMENT](https://github.com/corvaeoboro/zenv/)** : removes smaller detached objects 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_KEEP_BIGGER_OF_TWO_icon.png" width = "40" height = "40"/> **[z_KEEP_BIGGER_OF_TWO](https://github.com/corvaeoboro/zenv/)** : takes two inputs and ouputs only one ( bigger or smaller ) 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_KEEP_ONLY_FIRST_LAST_PRIMS_icon.png" width = "40" height = "40"/> **[z_KEEP_ONLY_FIRST_LAST_PRIMS](https://github.com/corvaeoboro/zenv/)** : carve for prim lines after segments split 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REMOVE_THIN_MESH_icon.png" width = "40" height = "40"/> **[z_REMOVE_THIN_MESH](https://github.com/corvaeoboro/zenv/)** : removes prims based on thickness measurement , then can fill in holes , useful for removing thin slivers 
## UV ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_AXIS_ALIGN_SNAP_icon.png" width = "40" height = "40"/> **[z_UV_AXIS_ALIGN_SNAP](https://github.com/corvaeoboro/zenv/)** : optimize uv location , moves uvs to zero to one space for precision in games
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_ALIGN_WORLD_icon.png" width = "40" height = "40"/> **[z_UV_ALIGN_WORLD](https://github.com/corvaeoboro/zenv/)** : align uvs to world axis , 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_OVERLAP_CHECK_icon.png" width = "40" height = "40"/> **[z_UV_OVERLAP_CHECK](https://github.com/corvaeoboro/zenv/)** : brute force uv overlap intersection check , separates all prims  for re packing
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_TEXEL_DENSITY_CHECK_icon.png" width = "40" height = "40"/> **[z_UV_TEXEL_DENSITY_CHECK](https://github.com/corvaeoboro/zenv/)** : check texel density with colorized debug , handles multiple materials with different texture resolutions by specifiying the corresponding materials name string and their rez
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_POLYWIRE_icon.png" width = "40" height = "40"/> **[z_UV_POLYWIRE](https://github.com/corvaeoboro/zenv/)** : creates polywire with specific UVs , useful when sweep is not producing desired bends
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_TRIM_icon.png" width = "40" height = "40"/> **[z_UV_TRIM](https://github.com/corvaeoboro/zenv/)** : fits uvs into specific trim sheet area while scaling the pieces along an axis relative to their world space

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_LIGHTMAP_UV_GEN_icon.png" width = "40" height = "40"/> **[z_LIGHTMAP_UV_GEN](https://github.com/corvaeoboro/zenv/)** : UVs creation for lightmaps , stored to uv1 with higher merge threshold 
## QA ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COLLISION_INTERSECT_CHECK_icon.png" width = "40" height = "40"/> **[z_COLLISION_INTERSECT_CHECK](https://github.com/corvaeoboro/zenv/)** : detect and show intersections with provided collision geometry . useful to avoid clipping into level geometry beyond a specific distance threshold 
## CHARACTER ##
## TEXTURE ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TEX_SEAM_BLENDER_icon.png" width = "40" height = "40"/> **[z_TEX_SEAM_BLENDER](https://github.com/corvaeoboro/zenv/)** : blend and blur a texture across uv seams to fix small bake errors and make seamless , additionally blending intersections of the meshes when surface details do not share a uvseam edge .. this is WIP bruteforce approach dividing the mesh by texel density and transfering the colors to vertexcolor bluring in worldspace proximity lastly adding in some noise counteract the blur .

## VFX ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VFX_SLASH_from_ANIM_icon.png" width = "40" height = "40"/> **[z_VFX_SLASH_from_ANIM](https://github.com/corvaeoboro/zenv/)** : create a smoothed  swipe mesh for vfx , sword slashing

## CAM ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CAM_ISOMETRIC_icon.png" width = "40" height = "40"/> **[z_CAM_ISOMETRIC](https://github.com/corvaeoboro/zenv/)** : camera with crane\boom arm setup matching isometric game settings

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CAM_PROJECTION_fspy_icon.png" width = "40" height = "40"/> **[z_CAM_PROJECTION_fspy](https://github.com/corvaeoboro/zenv/)** : a wrapper for fspy hda created  by floodini , input fspy json creating camera matching ref image perspective then project that image to floor plane

## GROUP ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_EDGEGROUP_BY_UV_AXIS_icon.png" width = "40" height = "40"/> **[z_EDGEGROUP_BY_UV_AXIS](https://github.com/corvaeoboro/zenv/)** : edgegroup based on axis of uvs , useful for polybeveling specific edges procedurally
## SORT ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SORT_BY_LINEAXIS_icon.png" width = "40" height = "40"/> **[z_SORT_BY_LINEAXIS](https://github.com/corvaeoboro/zenv/)** : sorts a line contigously linearly along axis , useful when must enforce a point order on a curved line when normal sort by axis would skip around

## CLEAN ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REVERSE_BY_N_UP_icon.png" width = "40" height = "40"/> **[z_REVERSE_BY_N_UP](https://github.com/corvaeoboro/zenv/)** : attempts to fix reversed facing ( backfacing )  normals on subobjects for an overhead camera , useful for fixing exports from some levels that mirrored assets with negative scaling

## OPTIMIZE ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_POLYREDUCE_GRADIENT_QUADS_icon.png" width = "40" height = "40"/> **[z_POLYREDUCE_GRADIENT_QUADS](https://github.com/corvaeoboro/zenv/)** : polyreduce setup with gradient retention to keep mostly quads , with secondary reduction

- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REMESH_RAY_SPHERE_icon.png" width = "40" height = "40"/> **[z_REMESH_RAY_SPHERE](https://github.com/corvaeoboro/zenv/)** : remesh from a sphere centered inside mesh , then raycast to the surface iteratively smoothing and raying

## MESH ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VDB_INTERNAL_FILL_icon.png" width = "40" height = "40"/> **[z_VDB_INTERNAL_FILL](https://github.com/corvaeoboro/zenv/)** : vdb to mesh , combines multiple lower res vdb's that are eroded to fill in the internal spaces
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SHRINKWRAP_VORONOI_CLUSTERS_icon.png" width = "40" height = "40"/> **[z_SHRINKWRAP_VORONOI_CLUSTERS](https://github.com/corvaeoboro/zenv/)** : similar to convex decomposition , cuts mesh into pieces via voronoi , then shrinkwraps those pieces . useful for rocky shapes
## COLOR ##
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COLOR_MASK_VERTEX_icon.png" width = "40" height = "40"/> **[z_COLOR_MASK_VERTEX](https://github.com/corvaeoboro/zenv/)** : creates vertex colors for game masking . AO , Variation ( random per connected element ) , and localized gradients ( Z axis per connected element ) 
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COLOR_NOISE_HI_icon.png" width = "40" height = "40"/> **[z_COLOR_NOISE_HI](https://github.com/corvaeoboro/zenv/)** : assigns colors based on curvature ramps , useful for hi poly stones and bricks
- <img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COLOR_LINES_SCRATCH_VTX_icon.png" width = "40" height = "40"/> **[z_COLOR_LINES_SCRATCH_VTX](https://github.com/corvaeoboro/zenv/)** : cuts in elipses and applys vertex colors  for stratches along an axis


## RECOMMENDED LIBRARIES ##
- SideFXLabs	**[https://github.com/sideeffects/SideFXLabs](https://github.com/sideeffects/SideFXLabs)** 
- qLib	**[https://github.com/qLab/qLib](https://github.com/qLab/qLib)** 
- AeLib	**[https://github.com/Aeoll/Aelib](https://github.com/Aeoll/Aelib)** 
- nLib	**[https://github.com/Njordy/nLib](https://github.com/Njordy/nLib)** 
- mifthtools	**[https://github.com/mifth/mifthtools](https://github.com/mifth/mifthtools)** 

## CC0 ##
free to all , creative commons cc0 