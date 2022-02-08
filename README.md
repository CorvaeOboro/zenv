## ZENV ##
- houdini hda tools focused on procedural modelling environments .
- an open source work in progress , many thanks to sidefx and other libraries and tutorials .

## EXAMPLES ##


<img src="/hip/z_GEN_VINES_WITH_LEAVES/z_GEN_VINES_WITH_LEAVES_01.jpg?raw=true" height="250" />
<img src="/hip/z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK/z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK.jpg?raw=true" height="250" />
<img src="/hip/z_GEN_HELIX_ROOTS/z_GEN_HELIX_ROOTS.jpg?raw=true" height="250" />
<img src="/hip/z_DRIP_GRUNGE/z_DRIP_GRUNGE.jpg?raw=true" height="250" />
<img src="/hip/z_TILEABLE/z_TILEABLE.jpg?raw=true" height="250" />

## TOOLS LIST ##

<img src="/hip/00_ALL_HDA/00_ALL_HDA.jpg?raw=true" height="250" />

## TYPE ##
|      |      |      |
| :--- | :--- | :--- |
## LAYOUT ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK_icon.png" width = "40" height = "40"/>| **[z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK](https://github.com/corvaeoboro/zenv/z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK)**| copy variants by piecenum attribute with collision checks|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COPY_MESH_ALONG_CURVE_DEFORM_icon.png" width = "40" height = "40"/>| **[z_COPY_MESH_ALONG_CURVE_DEFORM](https://github.com/corvaeoboro/zenv/z_COPY_MESH_ALONG_CURVE_DEFORM)**| pipe / wire curvedeform for houdini engine . copies input mesh without stretching along a curve , options to add cuts for smoother bending , can project normals outward from curve ,|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COPY_TO_EVENLY_DISTRIBUTED_GRID_icon.png" width = "40" height = "40"/>| **[z_COPY_TO_EVENLY_DISTRIBUTED_GRID](https://github.com/corvaeoboro/zenv/z_COPY_TO_EVENLY_DISTRIBUTED_GRID)**| copy by piecenum to dynamic evenly spaced grid - useful when baking and review|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TILE_4m_icon.png" width = "40" height = "40"/>| **[z_TILE_4m](https://github.com/corvaeoboro/zenv/z_TILE_4m)**| copies input to each of the 9 quadrants preview tiling for texture over specific distance ( 4m default )|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TRANSFORM_ITERATE_COLLISION_CHECK_icon.png" width = "40" height = "40"/>| **[z_TRANSFORM_ITERATE_COLLISION_CHECK](https://github.com/corvaeoboro/zenv/z_TRANSFORM_ITERATE_COLLISION_CHECK)**| move pieces towards goal while avoid itersection with collision ( simplied gravity + attraction sop based )|
## CREATE ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_HELIX_ROOTS_icon.png" width = "40" height = "40"/>| **[z_GEN_HELIX_ROOTS](https://github.com/corvaeoboro/zenv/z_GEN_HELIX_ROOTS)**| create winding intertwined roots from a guide line .|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_BRICKMAIN_01_icon.png" width = "40" height = "40"/>| **[z_GEN_BRICKMAIN_01](https://github.com/corvaeoboro/zenv/z_GEN_BRICKMAIN_01)**| stone brick variation generator , for midpoly stone bricks to be placed|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DIFFUSION_REACTION_TUBES_icon.png" width = "40" height = "40"/>| **[z_DIFFUSION_REACTION_TUBES](https://github.com/corvaeoboro/zenv/z_DIFFUSION_REACTION_TUBES)**| fill mesh with intestine brain like tubes based on simulated diffusion chemical reaction|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURL_LINES_LOOP_icon.png" width = "40" height = "40"/>| **[z_CURL_LINES_LOOP](https://github.com/corvaeoboro/zenv/z_CURL_LINES_LOOP)**| create lines curling on mesh surface using curlnoise loop|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_PETAL_FORM_icon.png" width = "40" height = "40"/>| **[z_GEN_PETAL_FORM](https://github.com/corvaeoboro/zenv/z_GEN_PETAL_FORM)**| generate petal from curve backbone and multiple warped elipse curves defining the shape changes over the length of the backbone |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DRIP_GRUNGE_icon.png" width = "40" height = "40"/>| **[z_DRIP_GRUNGE](https://github.com/corvaeoboro/zenv/z_DRIP_GRUNGE)**| drip grunge under overhangs , longer when near more drip neighboors|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_VINES_WITH_LEAVES_icon.png" width = "40" height = "40"/>| **[z_GEN_VINES_WITH_LEAVES](https://github.com/corvaeoboro/zenv/z_GEN_VINES_WITH_LEAVES)**| creates vines conforming to surface of mesh guided by line . iterative collision checks slow tho precise , leaves also collision avoid |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_REVOLVE_BASIC_icon.png" width = "40" height = "40"/>| **[z_GEN_REVOLVE_BASIC](https://github.com/corvaeoboro/zenv/z_GEN_REVOLVE_BASIC)**| create revolved mesh path deformed to backbone curve , input profile and backbone curves , first try at adaptive resample resolution based on bounds
|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_STAIRWAY_icon.png" width = "40" height = "40"/>| **[z_GEN_STAIRWAY](https://github.com/corvaeoboro/zenv/z_GEN_STAIRWAY)**| generate stairway made of bricks |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURL_LINES_THEN_PLACE_SPIRALS_icon.png" width = "40" height = "40"/>| **[z_CURL_LINES_THEN_PLACE_SPIRALS](https://github.com/corvaeoboro/zenv/z_CURL_LINES_THEN_PLACE_SPIRALS)**| creates curllines on the surface of mesh then copies spirals to the geometry with collision detection|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_CIRCLES_RADIATE_PATTERN_icon.png" width = "40" height = "40"/>| **[z_GEN_CIRCLES_RADIATE_PATTERN](https://github.com/corvaeoboro/zenv/z_GEN_CIRCLES_RADIATE_PATTERN)**| create circular patterns inspired by asian design . scatter circles , then radiate those circles outward while avoiding intersection by order or generation . |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_STONE_BRICK_CIRCLE_icon.png" width = "40" height = "40"/>| **[z_GEN_STONE_BRICK_CIRCLE](https://github.com/corvaeoboro/zenv/z_GEN_STONE_BRICK_CIRCLE)**| generate a circular shaped brick section by evenly voronoi fracturing and extruding toward center . applies additional noise and separation to resemble stone |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_MOSS_HANGING_icon.png" width = "40" height = "40"/>| **[z_GEN_MOSS_HANGING](https://github.com/corvaeoboro/zenv/z_GEN_MOSS_HANGING)**| creates hanging placements of moss mesh|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_HELIX_ALONG_CURVE_icon.png" width = "40" height = "40"/>| **[z_HELIX_ALONG_CURVE](https://github.com/corvaeoboro/zenv/z_HELIX_ALONG_CURVE)**| creates environment mesh for isometric snapmap pieces , used with PATH_BASE as its inputs for PDG|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_PATH_LEDGE_icon.png" width = "40" height = "40"/>| **[z_PATH_LEDGE](https://github.com/corvaeoboro/zenv/z_PATH_LEDGE)**| input curve to get helix curve around / along it |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURVE_FROM_TUBE_icon.png" width = "40" height = "40"/>| **[z_CURVE_FROM_TUBE](https://github.com/corvaeoboro/zenv/z_CURVE_FROM_TUBE)**| centered curve from mesh ( even if mesh has nonuniform topology )|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CURVES_FROM_UV_ISLANDS_icon.png" width = "40" height = "40"/>| **[z_CURVES_FROM_UV_ISLANDS](https://github.com/corvaeoboro/zenv/z_CURVES_FROM_UV_ISLANDS)**| for each uv island create a line curve aligned by the longest angle or vertical\horizontal . useful for generating tree branch curves from existing low poly trees
|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_VINES_GUIDED_icon.png" width = "40" height = "40"/>| **[z_GEN_VINES_GUIDED](https://github.com/corvaeoboro/zenv/z_GEN_VINES_GUIDED)**| generate a vine tube using a wandering path finder guided variably by a curve and other forces like a universal direction |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_PATH_BASE_icon.png" width = "40" height = "40"/>| **[z_PATH_BASE](https://github.com/corvaeoboro/zenv/z_PATH_BASE)**| create a path floor section and collision for gameplay , creates directional variants for snapmap . this is the basis for all other path generation |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_WIRE_OVERLAPING_OFFSET_icon.png" width = "40" height = "40"/>| **[z_WIRE_OVERLAPING_OFFSET](https://github.com/corvaeoboro/zenv/z_WIRE_OVERLAPING_OFFSET)**| creates wires rayed to ground , properly overlapping . input curves and collision |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TUBE_MESH_BETWEEN_TO_CIRCLES_icon.png" width = "40" height = "40"/>| **[z_TUBE_MESH_BETWEEN_TO_CIRCLES](https://github.com/corvaeoboro/zenv/z_TUBE_MESH_BETWEEN_TO_CIRCLES)**| input 2 circles , create a cyllinder between them |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_PILLAR_icon.png" width = "40" height = "40"/>| **[z_GEN_PILLAR](https://github.com/corvaeoboro/zenv/z_GEN_PILLAR)**| generate pillar - holding multiple brick generators and circle brick generators assembled to create a full pillar .|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_ROCK_4m_icon.png" width = "40" height = "40"/>| **[z_GEN_ROCK_4m](https://github.com/corvaeoboro/zenv/z_GEN_ROCK_4m)**| generates simple rock , setup for pdg |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_TUBES_FINDPATHS_FROM_CURVE_icon.png" width = "40" height = "40"/>| **[z_GEN_TUBES_FINDPATHS_FROM_CURVE](https://github.com/corvaeoboro/zenv/z_GEN_TUBES_FINDPATHS_FROM_CURVE)**| generates tubes that procedurally find a path to not intersect other tubes following along the length of a guide curve|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_SWORD_FROM_IMAGE_icon.png" width = "40" height = "40"/>| **[z_GEN_SWORD_FROM_IMAGE](https://github.com/corvaeoboro/zenv/z_GEN_SWORD_FROM_IMAGE)**| create a sword from image , traces png alpha  , orients vertically , and thickens from center internal line , sets uvs to match image and bakes colors to vertex colors
|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_TREE_TUBE_PATHFIND_icon.png" width = "40" height = "40"/>| **[z_GEN_TREE_TUBE_PATHFIND](https://github.com/corvaeoboro/zenv/z_GEN_TREE_TUBE_PATHFIND)**| generate a tree using shortest path thru curves scattered and connected around collision objects and previous tree roots|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_CRACK_BRANCHING_icon.png" width = "40" height = "40"/>| **[z_GEN_CRACK_BRANCHING](https://github.com/corvaeoboro/zenv/z_GEN_CRACK_BRANCHING)**| creates branching crack mesh used for booleaning other meshes|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_GIZMO_icon.png" width = "40" height = "40"/>| **[z_GEN_GIZMO](https://github.com/corvaeoboro/zenv/z_GEN_GIZMO)**| axis gizmo for debug|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GLASS_BOOLEAN_icon.png" width = "40" height = "40"/>| **[z_GLASS_BOOLEAN](https://github.com/corvaeoboro/zenv/z_GLASS_BOOLEAN)**| input mesh with irregular shaped hole , creates an intersection plane that conforms to the opening and adds inset with vertex colors for glass shader|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_GEN_LATTICE_GRIDMESH_icon.png" width = "40" height = "40"/>| **[z_GEN_LATTICE_GRIDMESH](https://github.com/corvaeoboro/zenv/z_GEN_LATTICE_GRIDMESH)**| creates a box of grids with interior points ideal for use as a lattice deformer |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UE4_PATH_2SPLINE_COLLISION_icon.png" width = "40" height = "40"/>| **[z_UE4_PATH_2SPLINE_COLLISION](https://github.com/corvaeoboro/zenv/z_UE4_PATH_2SPLINE_COLLISION)**| input two curves defining the border of a path , creates geometry to match , useful for quickly applying collision to organic pathways in ue4|
## MODIFY ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VORONI_FRACTURE_GRADIENT_OFFSET_icon.png" width = "40" height = "40"/>| **[z_VORONI_FRACTURE_GRADIENT_OFFSET](https://github.com/corvaeoboro/zenv/z_VORONI_FRACTURE_GRADIENT_OFFSET)**| voronoi fractures then offsets by multiple world space gradients . common tool for rock like shapes|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DEFORM_BY_HELIX_icon.png" width = "40" height = "40"/>| **[z_DEFORM_BY_HELIX](https://github.com/corvaeoboro/zenv/z_DEFORM_BY_HELIX)**| added output for the curves , to use for secondary polywires or to atrtransfr
|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_SUBTRACT_COLLAPSE_END_icon.png" width = "40" height = "40"/>| **[z_MESH_SUBTRACT_COLLAPSE_END](https://github.com/corvaeoboro/zenv/z_MESH_SUBTRACT_COLLAPSE_END)**| simple boolean subtract with option to collapse . useful for quick edits in ue4 |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_DEFORM_BY_AXIS_icon.png" width = "40" height = "40"/>| **[z_DEFORM_BY_AXIS](https://github.com/corvaeoboro/zenv/z_DEFORM_BY_AXIS)**| bounding box ramp deformation , using multi axes \ multiple ramps|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_NOISE_DISPLACE_MASKED_icon.png" width = "40" height = "40"/>| **[z_NOISE_DISPLACE_MASKED](https://github.com/corvaeoboro/zenv/z_NOISE_DISPLACE_MASKED)**| using vex attribute noise with presets apply noise to hi poly mesh surface |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_WRAP_DEFORM_BY_UV_icon.png" width = "40" height = "40"/>| **[z_MESH_WRAP_DEFORM_BY_UV](https://github.com/corvaeoboro/zenv/z_MESH_WRAP_DEFORM_BY_UV)**| deform mesh to another mesh by using the flattened UVs , useful to wrap a pattern around another|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_SURFACE_SIMPLE_REMESH_icon.png" width = "40" height = "40"/>| **[z_MESH_SURFACE_SIMPLE_REMESH](https://github.com/corvaeoboro/zenv/z_MESH_SURFACE_SIMPLE_REMESH)**| mesh surface simple remesh ray projects a grid unto the input geo and remeshes then reduces , helpful for fixing chaotic geo and non manifold errors , voxelization is ideal for closed geo this method is helpful for surface shell geo
|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_PLANARIZE_MULTIPLE_SURFACES_icon.png" width = "40" height = "40"/>| **[z_PLANARIZE_MULTIPLE_SURFACES](https://github.com/corvaeoboro/zenv/z_PLANARIZE_MULTIPLE_SURFACES)**| added second example for rock gen using planarize , increased max piece size
|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_CHIP_CRACKED_icon.png" width = "40" height = "40"/>| **[z_MESH_CHIP_CRACKED](https://github.com/corvaeoboro/zenv/z_MESH_CHIP_CRACKED)**| boolean subtract chipping and crack meshes onto the surface based on curvature and fit projecting the crack meshes .|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CONFORM_INTERSECTING_LERP_icon.png" width = "40" height = "40"/>| **[z_CONFORM_INTERSECTING_LERP](https://github.com/corvaeoboro/zenv/z_CONFORM_INTERSECTING_LERP)**| added paramters , now focused on conforming around a given colllision object based on it intersection
|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MESH_SLICER_SAVE_icon.png" width = "40" height = "40"/>| **[z_MESH_SLICER_SAVE](https://github.com/corvaeoboro/zenv/z_MESH_SLICER_SAVE)**| separates large meshes into grided sections and exports them to fbx , options for specific area exports , and compatible with houdini engine .  |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_MASK_TO_LINE_icon.png" width = "40" height = "40"/>| **[z_MASK_TO_LINE](https://github.com/corvaeoboro/zenv/z_MASK_TO_LINE)**| input blured mask of color channel from an image , output a single polypath line , useful for converting guide lines from annotated images such as before proportional adjustments or realignment of input images based on the mask
|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_STAMP_FOREACH_PIECE_icon.png" width = "40" height = "40"/>| **[z_STAMP_FOREACH_PIECE](https://github.com/corvaeoboro/zenv/z_STAMP_FOREACH_PIECE)**| randomized boolean of one mesh on to the surface of variants . useful for cutting designs into bricks|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SMOOTHING_FROM_UVs_icon.png" width = "40" height = "40"/>| **[z_SMOOTHING_FROM_UVs](https://github.com/corvaeoboro/zenv/z_SMOOTHING_FROM_UVs)**| hard edges by uv island  for baking |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VARIATION_DIRECTIONS_icon.png" width = "40" height = "40"/>| **[z_VARIATION_DIRECTIONS](https://github.com/corvaeoboro/zenv/z_VARIATION_DIRECTIONS)**| cycle thru 90 degree rotations and mirrored variantions  . for use with path tool|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SPLIT_CLIP_CREVISE_icon.png" width = "40" height = "40"/>| **[z_SPLIT_CLIP_CREVISE](https://github.com/corvaeoboro/zenv/z_SPLIT_CLIP_CREVISE)**| separate the input into two outputs with an indent along the separation , useful separating environment shell into terraced layers|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CUT_INTERSECT_DARKEN_icon.png" width = "40" height = "40"/>| **[z_CUT_INTERSECT_DARKEN](https://github.com/corvaeoboro/zenv/z_CUT_INTERSECT_DARKEN)**| darken a surface from the intersections of other objects , with option to boolean those cuts in|
## REMOVAL ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REMOVE_PIECES_BY_VOLUME_icon.png" width = "40" height = "40"/>| **[z_REMOVE_PIECES_BY_VOLUME](https://github.com/corvaeoboro/zenv/z_REMOVE_PIECES_BY_VOLUME)**| for each connected element , remove if doesnt match min or max measured volume , also has options of perimeter or other measurements|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_KEEP_ONLY_LARGEST_CONNECTED_ELEMENT_icon.png" width = "40" height = "40"/>| **[z_KEEP_ONLY_LARGEST_CONNECTED_ELEMENT](https://github.com/corvaeoboro/zenv/z_KEEP_ONLY_LARGEST_CONNECTED_ELEMENT)**| removes smaller detached objects |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_KEEP_BIGGER_OF_TWO_icon.png" width = "40" height = "40"/>| **[z_KEEP_BIGGER_OF_TWO](https://github.com/corvaeoboro/zenv/z_KEEP_BIGGER_OF_TWO)**| takes two inputs and ouputs only one ( bigger or smaller ) |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_KEEP_ONLY_FIRST_LAST_PRIMS_icon.png" width = "40" height = "40"/>| **[z_KEEP_ONLY_FIRST_LAST_PRIMS](https://github.com/corvaeoboro/zenv/z_KEEP_ONLY_FIRST_LAST_PRIMS)**| carve for prim lines after segments split |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REMOVE_THIN_MESH_icon.png" width = "40" height = "40"/>| **[z_REMOVE_THIN_MESH](https://github.com/corvaeoboro/zenv/z_REMOVE_THIN_MESH)**| removes prims based on thickness measurement , then can fill in holes , useful for removing thin slivers |
## UV ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_AXIS_ALIGN_SNAP_icon.png" width = "40" height = "40"/>| **[z_UV_AXIS_ALIGN_SNAP](https://github.com/corvaeoboro/zenv/z_UV_AXIS_ALIGN_SNAP)**| optimize uv location , moves uvs to zero to one space for precision in games|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_ALIGN_WORLD_icon.png" width = "40" height = "40"/>| **[z_UV_ALIGN_WORLD](https://github.com/corvaeoboro/zenv/z_UV_ALIGN_WORLD)**| align uv islands to world axis |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_OVERLAP_CHECK_icon.png" width = "40" height = "40"/>| **[z_UV_OVERLAP_CHECK](https://github.com/corvaeoboro/zenv/z_UV_OVERLAP_CHECK)**| brute force uv overlap intersection check , separates all prims  for re packing|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_TEXEL_DENSITY_CHECK_icon.png" width = "40" height = "40"/>| **[z_UV_TEXEL_DENSITY_CHECK](https://github.com/corvaeoboro/zenv/z_UV_TEXEL_DENSITY_CHECK)**| check texel density with colorized debug , handles multiple materials with different texture resolutions by specifiying the materials name string and their rez|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_POLYWIRE_icon.png" width = "40" height = "40"/>| **[z_UV_POLYWIRE](https://github.com/corvaeoboro/zenv/z_UV_POLYWIRE)**| creates polywire with specific UVs , useful when sweep is not producing desired bends|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_UV_TRIM_icon.png" width = "40" height = "40"/>| **[z_UV_TRIM](https://github.com/corvaeoboro/zenv/z_UV_TRIM)**| fits uvs into specific trim sheet area while scaling the pieces along an axis relative to their world space
|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_LIGHTMAP_UV_GEN_icon.png" width = "40" height = "40"/>| **[z_LIGHTMAP_UV_GEN](https://github.com/corvaeoboro/zenv/z_LIGHTMAP_UV_GEN)**| UVs creation for lightmaps , stored to uv1 with higher merge threshold |
## QA ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_COLLISION_INTERSECT_CHECK_icon.png" width = "40" height = "40"/>| **[z_COLLISION_INTERSECT_CHECK](https://github.com/corvaeoboro/zenv/z_COLLISION_INTERSECT_CHECK)**| detect and show intersections with provided collision geometry . useful to avoid clipping into level geometry beyond a specific distance threshold |
## CHARACTER ##
|      |      |      |
| :--- | :--- | :--- |
## TEXTURE ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_TEX_SEAM_BLENDER_icon.png" width = "40" height = "40"/>| **[z_TEX_SEAM_BLENDER](https://github.com/corvaeoboro/zenv/z_TEX_SEAM_BLENDER)**| blend and blur a texture across uv seams to fix small bake errors and make seamless , additionally blending intersections of the meshes when surface details do not share a uvseam edge .. this is WIP bruteforce approach dividing the mesh by texel density and transfering the colors to vertexcolor bluring in worldspace proximity lastly adding in some noise counteract the blur .
|
## VFX ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_VFX_SLASH_from_ANIM_icon.png" width = "40" height = "40"/>| **[z_VFX_SLASH_from_ANIM](https://github.com/corvaeoboro/zenv/z_VFX_SLASH_from_ANIM)**| create a smoothed  swipe mesh for vfx , sword slashing
|
## CAM ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CAM_ISOMETRIC_icon.png" width = "40" height = "40"/>| **[z_CAM_ISOMETRIC](https://github.com/corvaeoboro/zenv/z_CAM_ISOMETRIC)**| camera with crane\boom arm setup matching isometric game settings
|
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_CAM_PROJECTION_fspy_icon.png" width = "40" height = "40"/>| **[z_CAM_PROJECTION_fspy](https://github.com/corvaeoboro/zenv/z_CAM_PROJECTION_fspy)**| a wrapper for fspy hda created  by floodini , input fspy json creating camera matching ref image perspective then project that image to floor plane
|
## GROUP ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_EDGEGROUP_BY_UV_AXIS_icon.png" width = "40" height = "40"/>| **[z_EDGEGROUP_BY_UV_AXIS](https://github.com/corvaeoboro/zenv/z_EDGEGROUP_BY_UV_AXIS)**| edgegroup based on axis of uvs , useful for polybeveling specific edges procedurally|
## SORT ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_SORT_BY_LINEAXIS_icon.png" width = "40" height = "40"/>| **[z_SORT_BY_LINEAXIS](https://github.com/corvaeoboro/zenv/z_SORT_BY_LINEAXIS)**| sorts a line contigously linearly along axis , useful when must enforce a point order on a curved line when normal sort by axis would skip around
|
## CLEAN ##
|      |      |      |
| :--- | :--- | :--- |
|<img src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/icon/z_REVERSE_BY_N_UP_icon.png" width = "40" height = "40"/>| **[z_REVERSE_BY_N_UP](https://github.com/corvaeoboro/zenv/z_REVERSE_BY_N_UP)**| attempts to fix reversed facing ( backfacing )  normals on subobjects for an overhead camera , useful for fixing exports from some levels that mirrored assets with negative scaling
|

## RECOMMENDED LIBRARIES ##
- SideFXLabs	**[https://github.com/sideeffects/SideFXLabs](https://github.com/sideeffects/SideFXLabs)** 
- qLib	**[https://github.com/qLab/qLib](https://github.com/qLab/qLib)** 
- AeLib	**[https://github.com/Aeoll/Aelib](https://github.com/Aeoll/Aelib)** 
- nLib	**[https://github.com/Njordy/nLib](https://github.com/Njordy/nLib)** 
- mifthtools	**[https://github.com/mifth/mifthtools](https://github.com/mifth/mifthtools)** 

## CC0 ##
free to all , creative commons cc0 