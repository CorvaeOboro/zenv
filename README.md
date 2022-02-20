## ZENV ##
- houdini hda tools focused on procedural modelling environments .
- an open source work in progress , many thanks to sidefx and other [libraries]( https://github.com/CorvaeOboro/zenv#recommended-libraries ) and tutorials .

|      |      |      |      |
| :---: | :---: | :---: | :---: |
| <img src="/hip/z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK/z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK_thumb.jpg?raw=true" width="170" height="170" /> |  <img src="/hip/z_GEN_BRICKMAIN_01/z_GEN_BRICKMAIN_01_thumb.jpg?raw=true" width="170" height="170" />    |   <img src="/hip/z_GEN_STONE_BRICK_CIRCLE/z_GEN_STONE_BRICK_CIRCLE_thumb.jpg?raw=true" width="170" height="170" />    |  <img src="/hip/z_DIFFUSION_REACTION_TUBES/z_DIFFUSION_REACTION_TUBES_thumb.jpg?raw=true" width="170" height="170" />    |
| <img src="/hip/z_GEN_VINES_WITH_LEAVES/z_GEN_VINES_WITH_LEAVES.jpg?raw=true" width="170" height="170" /> |  <img src="/hip/z_GEN_HELIX_ROOTS/z_GEN_HELIX_ROOTS.jpg?raw=true" width="170" height="170" /> |  <img src="/hip/z_COLOR_NOISE_HI/z_COLOR_NOISE_HI_thumb.jpg?raw=true" width="170" height="170" />    |  <img src="/hip/z_GEN_MOSS_HANGING/z_GEN_MOSS_HANGING_thumb.jpg?raw=true" width="170" height="170" />    |
| <img src="/hip/z_COLOR_MASK_VERTEX/z_COLOR_MASK_VERTEX_thumb.jpg?raw=true" width="170" height="170" /> | <img src="/hip/z_DRIP_GRUNGE/z_DRIP_GRUNGE_thumb.jpg?raw=true" width="170" height="170" /> |  <img src="/hip/z_TILEABLE/z_TILEABLE.jpg?raw=true" width="170" height="170" />     |  <img src="/hip/z_HELIX_ALONG_CURVE/z_HELIX_ALONG_CURVE_thumb.jpg?raw=true" width="170" height="170" />    |
| <img src="/hip/z_GEN_REVOLVE_BASIC/z_GEN_REVOLVE_BASIC_thumb.jpg?raw=true" width="170" height="170" /> | <img src="/hip/z_DRIP_GRUNGE/z_DRIP_GRUNGE_thumb.jpg?raw=true" width="170" height="170" /> |  <img src="/hip/z_TILEABLE/z_TILEABLE.jpg?raw=true" width="170" height="170" />     |  <img src="/hip/z_HELIX_ALONG_CURVE/z_HELIX_ALONG_CURVE_thumb.jpg?raw=true" width="170" height="170" />    |

## TOOLS LIST ##

jump to category :

|       |___|      |___|       |___|       |___|       |
| :---: | :---:  | :---: |  :---: | :---: | :---: | :---: | :---: | :---: |
|[ LAYOUT ]( https://github.com/CorvaeOboro/zenv#layout )| |[ CREATE ]( https://github.com/CorvaeOboro/zenv#create )| |[ MODIFY ]( https://github.com/CorvaeOboro/zenv#modify )| |[ REMOVAL ]( https://github.com/CorvaeOboro/zenv#removal )||
|[ UV ]( https://github.com/CorvaeOboro/zenv#uv )| |[ QA ]( https://github.com/CorvaeOboro/zenv#qa )| |[ TEXTURE ]( https://github.com/CorvaeOboro/zenv#texture )| |[ VFX ]( https://github.com/CorvaeOboro/zenv#vfx )| |[ CAM ]( https://github.com/CorvaeOboro/zenv#cam )|
|[ GROUP ]( https://github.com/CorvaeOboro/zenv#group )| |[ SORT ]( https://github.com/CorvaeOboro/zenv#sort )| |[ CLEAN ]( https://github.com/CorvaeOboro/zenv#clean )| |[ OPTIMIZE ]( https://github.com/CorvaeOboro/zenv#optimize )| |[ MESH ]( https://github.com/CorvaeOboro/zenv#mesh )|
|[ COLOR ]( https://github.com/CorvaeOboro/zenv#color )| | [ MATERIAL ]( https://github.com/CorvaeOboro/zenv#material ) | | [ NORMALS ]( https://github.com/CorvaeOboro/zenv#normals )| |  | |

<img src="/hip/00_ALL_HDA/00_ALL_HDA.jpg?raw=true" height="250" />

**[hip/00_ALL_HDA/00_ALL_HDA.hip](https://github.com/corvaeoboro/zenv/tree/master/hip/00_ALL_HDA)**

click names below for tool example :

## LAYOUT ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK_icon.png" width = "40" height = "40"/>| **[z_COPY_TO_POINT S_BY_PIECENUM_INTERSECTIONCHECK](https://github.com/corvaeoboro/zenv/tree/master/hip/z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK)**|copy variants by piecenum attribute with collision checks|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COPY_MESH_ALONG_CURVE_DEFORM_icon.png" width = "40" height = "40"/>| **[z_COPY_MESH_ALO NG_CURVE_DEFORM](https://github.com/corvaeoboro/zenv/tree/master/hip/z_COPY_MESH_ALONG_CURVE_DEFORM)**|pipe / wire curvedeform for houdini engine . copies input mesh without stretching along a curve , options to add cuts for smoother bending , can project normals outward from curve ,|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COPY_TO_EVENLY_DISTRIBUTED_GRID_icon.png" width = "40" height = "40"/>| **[z_COPY_TO_EVENL Y_DISTRIBUTED_GRID](https://github.com/corvaeoboro/zenv/tree/master/hip/z_COPY_TO_EVENLY_DISTRIBUTED_GRID)**|copy by piecenum to dynamic evenly spaced grid - useful when baking and review|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TILE_4m_icon.png" width = "40" height = "40"/>| **[z_TILE_4m ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_TILE_4m)**|copies input to each of the nearby quadrants preview tiling ( 4m default )|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TRANSFORM_ITERATE_COLLISION_CHECK_icon.png" width = "40" height = "40"/>| **[z_TRANSFORM_ITE RATE_COLLISION_CHECK](https://github.com/corvaeoboro/zenv/tree/master/hip/z_TRANSFORM_ITERATE_COLLISION_CHECK)**|iteratively move pieces towards nearest goal while avoid itersection with collision ( an iterative simplified gravity / attraction sop based )|
## CREATE ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_HELIX_ROOTS_icon.png" width = "40" height = "40"/>| **[z_GEN_HELIX_ROO TS](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_HELIX_ROOTS)**|create winding intertwined roots from a guide line .|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_BRICKMAIN_01_icon.png" width = "40" height = "40"/>| **[z_GEN_BRICKMAIN _01](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_BRICKMAIN_01)**|stone brick variation generator , for midpoly stone bricks to be placed|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DIFFUSION_REACTION_TUBES_icon.png" width = "40" height = "40"/>| **[z_DIFFUSION_REA CTION_TUBES](https://github.com/corvaeoboro/zenv/tree/master/hip/z_DIFFUSION_REACTION_TUBES)**|fill mesh with intestine brain like tubes based on simulated diffusion chemical reaction|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURL_LINES_LOOP_icon.png" width = "40" height = "40"/>| **[z_CURL_LINES_LO OP](https://github.com/corvaeoboro/zenv/tree/master/hip/z_CURL_LINES_LOOP)**|create lines curling on mesh surface using curlnoise loop|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_PETAL_FORM_icon.png" width = "40" height = "40"/>| **[z_GEN_PETAL_FOR M](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_PETAL_FORM)**|generate petal from curve backbone and multiple warped elipse curves defining the shape changes over the length of the backbone|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DRIP_GRUNGE_icon.png" width = "40" height = "40"/>| **[z_DRIP_GRUNGE ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_DRIP_GRUNGE)**|drip grunge under overhangs , longer when near more drip neighboors|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_VINES_WITH_LEAVES_icon.png" width = "40" height = "40"/>| **[z_GEN_VINES_WIT H_LEAVES](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_VINES_WITH_LEAVES)**|creates vines conforming to surface of mesh guided by line . iterative collision checks slow tho precise , leaves also collision avoid|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_REVOLVE_BASIC_icon.png" width = "40" height = "40"/>| **[z_GEN_REVOLVE_B ASIC](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_REVOLVE_BASIC)**|create revolved mesh path deformed to backbone curve , input profile and backbone curves|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_STAIRWAY_icon.png" width = "40" height = "40"/>| **[z_GEN_STAIRWAY ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_STAIRWAY)**|generate stairway made of bricks|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURL_LINES_THEN_PLACE_SPIRALS_icon.png" width = "40" height = "40"/>| **[z_CURL_LINES_TH EN_PLACE_SPIRALS](https://github.com/corvaeoboro/zenv/tree/master/hip/z_CURL_LINES_THEN_PLACE_SPIRALS)**|creates curllines on the surface of mesh then copies spirals to the geometry with collision detection|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_CIRCLES_RADIATE_PATTERN_icon.png" width = "40" height = "40"/>| **[z_GEN_CIRCLES_R ADIATE_PATTERN](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_CIRCLES_RADIATE_PATTERN)**|create circular patterns inspired by asian design . scatter circles , then radiate those circles outward while avoiding intersection by order or generation .|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_STONE_BRICK_CIRCLE_icon.png" width = "40" height = "40"/>| **[z_GEN_STONE_BRI CK_CIRCLE](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_STONE_BRICK_CIRCLE)**|generate a circular shaped brick section by evenly voronoi fracturing and extruding toward center . applies additional noise and separation to resemble stone|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_MOSS_HANGING_icon.png" width = "40" height = "40"/>| **[z_GEN_MOSS_HANG ING](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_MOSS_HANGING)**|creates hanging placements of moss mesh|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_HELIX_ALONG_CURVE_icon.png" width = "40" height = "40"/>| **[z_HELIX_ALONG_C URVE](https://github.com/corvaeoboro/zenv/tree/master/hip/z_HELIX_ALONG_CURVE)**|creates environment mesh for isometric snapmap pieces , used with PATH_BASE as its inputs for PDG|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_PATH_LEDGE_icon.png" width = "40" height = "40"/>| **[z_PATH_LEDGE ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_PATH_LEDGE)**|input curve to get helix curve around / along it|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURVE_FROM_TUBE_icon.png" width = "40" height = "40"/>| **[z_CURVE_FROM_TU BE](https://github.com/corvaeoboro/zenv/tree/master/hip/z_CURVE_FROM_TUBE)**|centered curve from mesh ( even if mesh has nonuniform topology )|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_VINES_GUIDED_icon.png" width = "40" height = "40"/>| **[z_GEN_VINES_GUI DED](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_VINES_GUIDED)**|generate a vine tube using a wandering path finder guided variably by a curve or direction vector|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURVES_FROM_UV_ISLANDS_icon.png" width = "40" height = "40"/>| **[z_CURVES_FROM_U V_ISLANDS](https://github.com/corvaeoboro/zenv/tree/master/hip/z_CURVES_FROM_UV_ISLANDS)**|for each uv island create a line curve aligned by the longest angle or vertical\horizontal . useful for generating tree branch curves from existing low poly trees|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_PATH_BASE_icon.png" width = "40" height = "40"/>| **[z_PATH_BASE ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_PATH_BASE)**|create a path floor section and collision for gameplay , creates directional variants for snapmap . this is the basis for all other path generation|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_WIRE_OVERLAPING_OFFSET_icon.png" width = "40" height = "40"/>| **[z_WIRE_OVERLAPI NG_OFFSET](https://github.com/corvaeoboro/zenv/tree/master/hip/z_WIRE_OVERLAPING_OFFSET)**|creates wires rayed to ground , properly overlapping . input curves and collision|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TUBE_MESH_BETWEEN_TO_CIRCLES_icon.png" width = "40" height = "40"/>| **[z_TUBE_MESH_BET WEEN_TO_CIRCLES](https://github.com/corvaeoboro/zenv/tree/master/hip/z_TUBE_MESH_BETWEEN_TO_CIRCLES)**|input 2 circles , create a cyllinder between them|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_PILLAR_icon.png" width = "40" height = "40"/>| **[z_GEN_PILLAR ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_PILLAR)**|generate pillar - holding multiple brick generators and circle brick generators assembled to create a full pillar .|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_ROCK_4m_icon.png" width = "40" height = "40"/>| **[z_GEN_ROCK_4m ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_ROCK_4m)**|generates simple rock , setup for pdg|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_TUBES_FINDPATHS_FROM_CURVE_icon.png" width = "40" height = "40"/>| **[z_GEN_TUBES_FIN DPATHS_FROM_CURVE](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_TUBES_FINDPATHS_FROM_CURVE)**|generates tubes that procedurally find a path to not intersect other tubes following along the length of a guide curve|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_SWORD_FROM_IMAGE_icon.png" width = "40" height = "40"/>| **[z_GEN_SWORD_FRO M_IMAGE](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_SWORD_FROM_IMAGE)**|creates a sword mesh from image , traces png alpha  , orients vertically , thickens from center skeleton line , sets uvs to match image , bakes colors to vertex colors|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_TREE_TUBE_PATHFIND_icon.png" width = "40" height = "40"/>| **[z_GEN_TREE_TUBE _PATHFIND](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_TREE_TUBE_PATHFIND)**|generate a tree using shortest path thru curves scattered and connected around collision objects and previous tree roots|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_CRACK_BRANCHING_icon.png" width = "40" height = "40"/>| **[z_GEN_CRACK_BRA NCHING](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_CRACK_BRANCHING)**|creates branching crack mesh used for booleaning other meshes|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_GIZMO_icon.png" width = "40" height = "40"/>| **[z_GEN_GIZMO ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_GIZMO)**|axis gizmo for debug|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GLASS_BOOLEAN_icon.png" width = "40" height = "40"/>| **[z_GLASS_BOOLEAN ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GLASS_BOOLEAN)**|input mesh with irregular shaped hole , creates an intersection plane that conforms to the opening and adds inset with vertex colors for glass shader|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_LATTICE_GRIDMESH_icon.png" width = "40" height = "40"/>| **[z_GEN_LATTICE_G RIDMESH](https://github.com/corvaeoboro/zenv/tree/master/hip/z_GEN_LATTICE_GRIDMESH)**|creates a box of grids with interior points ideal for use as a lattice deformer|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UE4_PATH_2SPLINE_COLLISION_icon.png" width = "40" height = "40"/>| **[z_UE4_PATH_2SPL INE_COLLISION](https://github.com/corvaeoboro/zenv/tree/master/hip/z_UE4_PATH_2SPLINE_COLLISION)**|input two curves defining the border of a path , creates geometry to match , useful for quickly applying collision to organic pathways in ue4|
## MODIFY ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VORONI_FRACTURE_GRADIENT_OFFSET_icon.png" width = "40" height = "40"/>| **[z_VORONI_FRACTU RE_GRADIENT_OFFSET](https://github.com/corvaeoboro/zenv/tree/master/hip/z_VORONI_FRACTURE_GRADIENT_OFFSET)**|voronoi fractures then offsets by multiple world space gradients . common tool for rock like shapes|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DEFORM_BY_HELIX_icon.png" width = "40" height = "40"/>| **[z_DEFORM_BY_HEL IX](https://github.com/corvaeoboro/zenv/tree/master/hip/z_DEFORM_BY_HELIX)**|deform the input mesh by a helix fit to the object bounds|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_SUBTRACT_COLLAPSE_END_icon.png" width = "40" height = "40"/>| **[z_MESH_SUBTRACT _COLLAPSE_END](https://github.com/corvaeoboro/zenv/tree/master/hip/z_MESH_SUBTRACT_COLLAPSE_END)**|simple boolean subtract with option to collapse . useful for quick edits in ue4|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DEFORM_BY_AXIS_icon.png" width = "40" height = "40"/>| **[z_DEFORM_BY_AXI S](https://github.com/corvaeoboro/zenv/tree/master/hip/z_DEFORM_BY_AXIS)**|bounding box ramp deformation , using multi axes \ multiple ramps|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_NOISE_DISPLACE_MASKED_icon.png" width = "40" height = "40"/>| **[z_NOISE_DISPLAC E_MASKED](https://github.com/corvaeoboro/zenv/tree/master/hip/z_NOISE_DISPLACE_MASKED)**|using vex attribute noise with presets apply noise to hi poly mesh surface|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_WRAP_DEFORM_BY_UV_icon.png" width = "40" height = "40"/>| **[z_MESH_WRAP_DEF ORM_BY_UV](https://github.com/corvaeoboro/zenv/tree/master/hip/z_MESH_WRAP_DEFORM_BY_UV)**|deform mesh to another mesh by using the flattened UVs , useful to wrap a pattern around another|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_SURFACE_SIMPLE_REMESH_icon.png" width = "40" height = "40"/>| **[z_MESH_SURFACE_ SIMPLE_REMESH](https://github.com/corvaeoboro/zenv/tree/master/hip/z_MESH_SURFACE_SIMPLE_REMESH)**|mesh surface simple remesh ray projects a grid unto the input geo and remeshes then reduces , helpful for fixing chaotic geo and non manifold errors , voxelization is ideal for closed geo this method is helpful for surface shell geo|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_PLANARIZE_MULTIPLE_SURFACES_icon.png" width = "40" height = "40"/>| **[z_PLANARIZE_MUL TIPLE_SURFACES](https://github.com/corvaeoboro/zenv/tree/master/hip/z_PLANARIZE_MULTIPLE_SURFACES)**|input mesh surface is segmented by avg n and flattened from multiple directions . useful to randomly planarize from different angles for rock meshes|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_CHIP_CRACKED_icon.png" width = "40" height = "40"/>| **[z_MESH_CHIP_CRA CKED](https://github.com/corvaeoboro/zenv/tree/master/hip/z_MESH_CHIP_CRACKED)**|boolean subtract chipping and crack meshes onto the surface based on curvature and fit projecting the crack meshes .|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CONFORM_INTERSECTING_LERP_icon.png" width = "40" height = "40"/>| **[z_CONFORM_INTER SECTING_LERP](https://github.com/corvaeoboro/zenv/tree/master/hip/z_CONFORM_INTERSECTING_LERP)**|conform around a given colllision object if has intersection|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_SLICER_SAVE_icon.png" width = "40" height = "40"/>| **[z_MESH_SLICER_S AVE](https://github.com/corvaeoboro/zenv/tree/master/hip/z_MESH_SLICER_SAVE)**|separates large meshes into grided sections and exports them to fbx , options for specific area exports , and compatible with houdini engine .|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MASK_TO_LINE_icon.png" width = "40" height = "40"/>| **[z_MASK_TO_LINE ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_MASK_TO_LINE)**|input blured mask of color channel from an image , output a single polypath line , useful for converting guide lines from annotated images such as before proportional adjustments or realignment of input images based on the mask|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_STAMP_FOREACH_PIECE_icon.png" width = "40" height = "40"/>| **[z_STAMP_FOREACH _PIECE](https://github.com/corvaeoboro/zenv/tree/master/hip/z_STAMP_FOREACH_PIECE)**|randomized boolean of one mesh on to the surface of variants . useful for cutting designs into bricks|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SMOOTHING_FROM_UVs_icon.png" width = "40" height = "40"/>| **[z_SMOOTHING_FRO M_UVs](https://github.com/corvaeoboro/zenv/tree/master/hip/z_SMOOTHING_FROM_UVs)**|hard edges by uv island  for baking|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VARIATION_DIRECTIONS_icon.png" width = "40" height = "40"/>| **[z_VARIATION_DIR ECTIONS](https://github.com/corvaeoboro/zenv/tree/master/hip/z_VARIATION_DIRECTIONS)**|cycle thru 90 degree rotations and mirrored variantions  . for use with path tool|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SPLIT_CLIP_CREVISE_icon.png" width = "40" height = "40"/>| **[z_SPLIT_CLIP_CR EVISE](https://github.com/corvaeoboro/zenv/tree/master/hip/z_SPLIT_CLIP_CREVISE)**|separate the input into two outputs with an indent along the separation , useful separating environment shell into terraced layers|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CUT_INTERSECT_DARKEN_icon.png" width = "40" height = "40"/>| **[z_CUT_INTERSECT _DARKEN](https://github.com/corvaeoboro/zenv/tree/master/hip/z_CUT_INTERSECT_DARKEN)**|darken a surface from the intersections of other objects , with option to boolean those cuts in|
## REMOVAL ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REMOVE_PIECES_BY_VOLUME_icon.png" width = "40" height = "40"/>| **[z_REMOVE_PIECES _BY_VOLUME](https://github.com/corvaeoboro/zenv/tree/master/hip/z_REMOVE_PIECES_BY_VOLUME)**|for each connected element , remove if doesnt match min or max measured volume , also has options of perimeter or other measurements|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_KEEP_ONLY_LARGEST_CONNECTED_ELEMENT_icon.png" width = "40" height = "40"/>| **[z_KEEP_ONLY_LAR GEST_CONNECTED_ELEMENT](https://github.com/corvaeoboro/zenv/tree/master/hip/z_KEEP_ONLY_LARGEST_CONNECTED_ELEMENT)**|removes smaller detached objects|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_KEEP_BIGGER_OF_TWO_icon.png" width = "40" height = "40"/>| **[z_KEEP_BIGGER_O F_TWO](https://github.com/corvaeoboro/zenv/tree/master/hip/z_KEEP_BIGGER_OF_TWO)**|takes two inputs and ouputs only one ( bigger or smaller )|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_KEEP_ONLY_FIRST_LAST_PRIMS_icon.png" width = "40" height = "40"/>| **[z_KEEP_ONLY_FIR ST_LAST_PRIMS](https://github.com/corvaeoboro/zenv/tree/master/hip/z_KEEP_ONLY_FIRST_LAST_PRIMS)**|carve for prim lines after segments split|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REMOVE_THIN_MESH_icon.png" width = "40" height = "40"/>| **[z_REMOVE_THIN_M ESH](https://github.com/corvaeoboro/zenv/tree/master/hip/z_REMOVE_THIN_MESH)**|removes prims based on thickness measurement , then can fill in holes , useful for removing thin slivers|
## UV ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_AXIS_ALIGN_SNAP_icon.png" width = "40" height = "40"/>| **[z_UV_AXIS_ALIGN _SNAP](https://github.com/corvaeoboro/zenv/tree/master/hip/z_UV_AXIS_ALIGN_SNAP)**|optimize uv location , moves uvs to zero to one space for precision in games|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_ALIGN_WORLD_icon.png" width = "40" height = "40"/>| **[z_UV_ALIGN_WORL D](https://github.com/corvaeoboro/zenv/tree/master/hip/z_UV_ALIGN_WORLD)**|align uv islands to world axis|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_OVERLAP_CHECK_icon.png" width = "40" height = "40"/>| **[z_UV_OVERLAP_CH ECK](https://github.com/corvaeoboro/zenv/tree/master/hip/z_UV_OVERLAP_CHECK)**|brute force uv overlap intersection check , separates all prims  for re packing|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_TEXEL_DENSITY_CHECK_icon.png" width = "40" height = "40"/>| **[z_UV_TEXEL_DENS ITY_CHECK](https://github.com/corvaeoboro/zenv/tree/master/hip/z_UV_TEXEL_DENSITY_CHECK)**|check texel density with colorized debug , handles multiple materials with different texture resolutions by specifiying the materials name string and their rez|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_POLYWIRE_icon.png" width = "40" height = "40"/>| **[z_UV_POLYWIRE ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_UV_POLYWIRE)**|creates polywire with specific UVs , useful when sweep is not producing desired bends|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_TRIM_icon.png" width = "40" height = "40"/>| **[z_UV_TRIM ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_UV_TRIM)**|fits uvs into specific trim sheet area while scaling the pieces along an axis relative to their world space|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_LIGHTMAP_UV_GEN_icon.png" width = "40" height = "40"/>| **[z_LIGHTMAP_UV_G EN](https://github.com/corvaeoboro/zenv/tree/master/hip/z_LIGHTMAP_UV_GEN)**|UVs creation for lightmaps , stored to uv1 with higher merge threshold|
## QA ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COLLISION_INTERSECT_CHECK_icon.png" width = "40" height = "40"/>| **[z_COLLISION_INT ERSECT_CHECK](https://github.com/corvaeoboro/zenv/tree/master/hip/z_COLLISION_INTERSECT_CHECK)**|detect and show intersections with provided collision geometry . useful to avoid clipping into level geometry beyond a specific distance threshold|

## TEXTURE ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TEX_SEAM_BLENDER_icon.png" width = "40" height = "40"/>| **[z_TEX_SEAM_BLEN DER](https://github.com/corvaeoboro/zenv/tree/master/hip/z_TEX_SEAM_BLENDER)**|blend and blur a texture across uv seams to fix small bake errors and make seamless , additionally blending intersections of the meshes when surface details do not share a uvseam edge .. this is WIP bruteforce approach dividing the mesh by texel density and transfering the colors to vertexcolor bluring in worldspace proximity lastly adding in some noise counteract the blur .|
## VFX ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VFX_SLASH_from_ANIM_icon.png" width = "40" height = "40"/>| **[z_VFX_SLASH_fro m_ANIM](https://github.com/corvaeoboro/zenv/tree/master/hip/z_VFX_SLASH_from_ANIM)**|create a smoothed  swipe mesh for vfx , sword slashing|
## CAM ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CAM_ISOMETRIC_icon.png" width = "40" height = "40"/>| **[z_CAM_ISOMETRIC ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_CAM_ISOMETRIC)**|camera with crane\boom arm setup matching isometric game settings|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CAM_PROJECTION_fspy_icon.png" width = "40" height = "40"/>| **[z_CAM_PROJECTIO N_fspy](https://github.com/corvaeoboro/zenv/tree/master/hip/z_CAM_PROJECTION_fspy)**|a wrapper for fspy hda created  by floodini , input fspy json creating camera matching ref image perspective then project that image to floor plane|
## GROUP ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_EDGEGROUP_BY_UV_AXIS_icon.png" width = "40" height = "40"/>| **[z_EDGEGROUP_BY_ UV_AXIS](https://github.com/corvaeoboro/zenv/tree/master/hip/z_EDGEGROUP_BY_UV_AXIS)**|edgegroup based on axis of uvs , useful for polybeveling specific edges procedurally|
## SORT ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SORT_BY_LINEAXIS_icon.png" width = "40" height = "40"/>| **[z_SORT_BY_LINEA XIS](https://github.com/corvaeoboro/zenv/tree/master/hip/z_SORT_BY_LINEAXIS)**|sorts a line contigously linearly along axis , enforcing a point order on a curved line when sort by axis may skip around|
## CLEAN ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REVERSE_BY_N_UP_icon.png" width = "40" height = "40"/>| **[z_REVERSE_BY_N_ UP](https://github.com/corvaeoboro/zenv/tree/master/hip/z_REVERSE_BY_N_UP)**|attempts to fix reversed backfacing normals on multiple sub meshes, useful for fixing exported levels with mirrored ( negative scaled ) objects|
## OPTIMIZE ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_POLYREDUCE_GRADIENT_QUADS_icon.png" width = "40" height = "40"/>| **[z_POLYREDUCE_GR ADIENT_QUADS](https://github.com/corvaeoboro/zenv/tree/master/hip/z_POLYREDUCE_GRADIENT_QUADS)**|polyreduce setup with gradient retention to keep mostly quads , with secondary reduction|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REMESH_RAY_SPHERE_icon.png" width = "40" height = "40"/>| **[z_REMESH_RAY_SP HERE](https://github.com/corvaeoboro/zenv/tree/master/hip/z_REMESH_RAY_SPHERE)**|remesh using sphere around object , iteratively raycast and smooth to approximate shape|
## MESH ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VDB_INTERNAL_FILL_icon.png" width = "40" height = "40"/>| **[z_VDB_INTERNAL_ FILL](https://github.com/corvaeoboro/zenv/tree/master/hip/z_VDB_INTERNAL_FILL)**|mesh to vdb to mesh , combines multiple lower res vdb's that are eroded to fill in the internal spaces|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SHRINKWRAP_VORONOI_CLUSTERS_icon.png" width = "40" height = "40"/>| **[z_SHRINKWRAP_VO RONOI_CLUSTERS](https://github.com/corvaeoboro/zenv/tree/master/hip/z_SHRINKWRAP_VORONOI_CLUSTERS)**|similar to convex decomposition , cuts mesh into pieces via voronoi , shrinkwraps those pieces . useful for rocky shapes|
## COLOR ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COLOR_MASK_VERTEX_icon.png" width = "40" height = "40"/>| **[z_COLOR_MASK_VE RTEX](https://github.com/corvaeoboro/zenv/tree/master/hip/z_COLOR_MASK_VERTEX)**|creates vertex colors for game masking . AO , Variation ( random per connected element ) , and localized gradients ( Z axis per connected element )|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COLOR_NOISE_HI_icon.png" width = "40" height = "40"/>| **[z_COLOR_NOISE_H I](https://github.com/corvaeoboro/zenv/tree/master/hip/z_COLOR_NOISE_HI)**|assigns colors based on curvature ramps , useful for hi poly stones and bricks|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COLOR_LINES_SCRATCH_VTX_icon.png" width = "40" height = "40"/>| **[z_COLOR_LINES_S CRATCH_VTX](https://github.com/corvaeoboro/zenv/tree/master/hip/z_COLOR_LINES_SCRATCH_VTX)**|cuts in elipses and applys vertex colors  for stratches along an axis|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VERTEXCOLOR_CONVERT_icon.png" width = "40" height = "40"/>| **[z_VERTEXCOLOR_C ONVERT](https://github.com/corvaeoboro/zenv/tree/master/hip/z_VERTEXCOLOR_CONVERT)**|converts standard rgb vertex color blending to multilayer vertex blending with alpha|
## MATERIAL ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UDIM_CONVERT_icon.png" width = "40" height = "40"/>| **[z_UDIM_CONVERT ](https://github.com/corvaeoboro/zenv/tree/master/hip/z_UDIM_CONVERT)**|convert single material UDIM to multiple materials , and reposition the uvs into zero to one|
## NORMALS ##
|  ______    |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_NORMAL_AREA_WEIGHTED_icon.png" width = "40" height = "40"/>| **[z_NORMAL_AREA_W EIGHTED](https://github.com/corvaeoboro/zenv/tree/master/hip/z_NORMAL_AREA_WEIGHTED)**|normals smoothed face area weighted alternative|

## RECOMMENDED LIBRARIES ##
- SideFXLabs	**[https://github.com/sideeffects/SideFXLabs](https://github.com/sideeffects/SideFXLabs)** 
- qLib	**[https://github.com/qLab/qLib](https://github.com/qLab/qLib)** 
- AeLib	**[https://github.com/Aeoll/Aelib](https://github.com/Aeoll/Aelib)** 
- nLib	**[https://github.com/Njordy/nLib](https://github.com/Njordy/nLib)** 
- mifthtools	**[https://github.com/mifth/mifthtools](https://github.com/mifth/mifthtools)** 
- jhorikawa https://github.com/jhorikawa/HoudiniHowtos

## CC0 ##
free to all , creative commons cc0 