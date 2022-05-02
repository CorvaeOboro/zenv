# ALL HDA TOOL EXAMPLES

<h1>z_HELIX_ALONG_CURVE</h1>
<ul>
<li>creates a helix curves along input curve  </li>
</ul>
<p><img alt="z_HELIX_ALONG_CURVE" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_HELIX_ALONG_CURVE/z_HELIX_ALONG_CURVE.jpg?raw=true" title="z_HELIX_ALONG_CURVE" /></p>
<h1>z_EXPORT_TO_UNREAL</h1>
<p>common settings used before exporting fbx to unreal , material parameter conversion , point color to vtx conversion
. scale and rotation</p>
<h1>z_VERTEXCOLOR_CONVERT</h1>
<p>converts standard rgb vertex color blending to multilayer vertex blending with alpha</p>
<h1>z_GEN_CIRCLES_RADIATE_PATTERN</h1>
<p>creates circular patterns inspired by asian design . scatter circles , then radiate those circles outward while avoiding intersection by order or generation . </p>
<p><img alt="z_GEN_CIRCLES_RADIATE_PATTERN" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_CIRCLES_RADIATE_PATTERN/z_GEN_CIRCLES_RADIATE_PATTERN_thumb.jpg?raw=true" title="z_GEN_CIRCLES_RADIATE_PATTERN" /></p>
<h1>z_GEN_GIZMO</h1>
<p>axis gizmo for debug</p>
<p><img alt="z_GEN_GIZMO" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_GIZMO/z_GEN_GIZMO.jpg?raw=true" title="z_GEN_GIZMO" /></p>
<h1>z_DEFORM_BY_HELIX</h1>
<p>deform the input mesh by a helix fit to the object bounds</p>
<h1>z_GEN_HELIX_ROOTS</h1>
<ul>
<li>creates winding intertwined roots from an input guide line .</li>
</ul>
<p><img alt="z_GEN_HELIX_ROOTS" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_HELIX_ROOTS/z_GEN_HELIX_ROOTS.jpg?raw=true" title="z_GEN_HELIX_ROOTS" /></p>
<h1>z_PATH_BASE</h1>
<p>create a path floor section and collision for gameplay , creates directional variants for snapmap . this is the basis for all other path generation </p>
<h1>z_GEN_PILLAR</h1>
<p>generate pillar - holding multiple brick generators and circle brick generators assembled to create a full pillar .</p>
<h1>z_SHRINKWRAP_VORONOI_CLUSTERS</h1>
<p>similar to convex decomposition , cuts mesh into pieces via voronoi , shrinkwraps those pieces . useful for rocky shapes</p>
<h1>z_UV_TRIM</h1>
<p>fits uvs into specific trim sheet area while scaling the pieces along an axis relative to their world space</p>
<h1>z_MESH_CONNECT_BORDERS</h1>
<p>mesh connect borders , simplified circular connect from input curves with different number of divisions, ideally a basic poly bridge with unified circular outward normals</p>
<h1>z_COLOR_NOISE_HI</h1>
<ul>
<li>vertex colors based on multiple ramps driven by curvature , occlusion , and noise </li>
<li>default stone preset</li>
</ul>
<p><img alt="z_COLOR_NOISE_HI" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_COLOR_NOISE_HI/z_COLOR_NOISE_HI.jpg?raw=true" title="z_COLOR_NOISE_HI" /></p>
<h1>z_TUBE_BOOLEAN_PANELS</h1>
<p>cut instanced panels from cyllinder surface</p>
<h1>z_CAM_ISOMETRIC</h1>
<ul>
<li>camera with crane\boom arm setup matching isometric game settings</li>
</ul>
<p><img alt="z_CAM_ISOMETRIC" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_CAM_ISOMETRIC/z_CAM_ISOMETRIC.jpg?raw=true" title="z_CAM_ISOMETRIC" /></p>
<h1>z_CONFORM_INTERSECTING_LERP</h1>
<p>conform around a given colllision object if has intersection</p>
<p><img alt="z_CONFORM_INTERSECTING_LERP" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_CONFORM_INTERSECTING_LERP/z_CONFORM_INTERSECTING_LERP.jpg?raw=true" title="z_CONFORM_INTERSECTING_LERP" /></p>
<h1>z_GEN_VINES_GUIDED</h1>
<p>generate a vine tube using a wandering path finder guided variably by a curve or direction vector</p>
<h1>z_GEN_REVOLVE_BASIC</h1>
<p>creates revolved mesh , path deformed by backbone curve , input profile and backbone curves </p>
<p><img alt="z_GEN_REVOLVE_BASIC" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_REVOLVE_BASIC/z_GEN_REVOLVE_BASIC.jpg?raw=true" title="z_GEN_REVOLVE_BASIC" /></p>
<h1>z_TRANSFORM_ITERATE_COLLISION_CHECK</h1>
<p>iteratively move pieces towards nearest goal while avoid itersection with collision ( an iterative simplified gravity / attraction sop based )</p>
<h1>z_GEN_BRICKMAIN_01</h1>
<ul>
<li>creates stone brick variations , fractured , cracks , chipped </li>
<li>outputs lowpoly and hipoly meshes with piecenum , and a distributed grid for texture baking highs to low </li>
</ul>
<p><img alt="z_GEN_BRICKMAIN_01" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_BRICKMAIN_01/z_GEN_BRICKMAIN_01.jpg?raw=true" title="z_GEN_BRICKMAIN_01" /></p>
<h1>z_DEFORM_BY_AXIS</h1>
<ul>
<li>bounding box ramp deformation , setup to allow multiple axis ramps </li>
<li>useful for procedural relative deformations </li>
</ul>
<p><img alt="z_DEFORM_BY_AXIS" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_DEFORM_BY_AXIS/z_DEFORM_BY_AXIS.jpg?raw=true" title="z_DEFORM_BY_AXIS" /></p>
<h1>z_MESH_SUBTRACT_COLLAPSE_END</h1>
<p>simple boolean subtract with option to collapse . useful for quick edits in ue4 </p>
<h1>z_MESH_CHIP_CRACKED</h1>
<p>boolean subtract chipping and crack meshes onto the surface based on curvature and fit projecting the crack meshes .</p>
<p><img alt="z_MESH_CHIP_CRACKED" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_MESH_CHIP_CRACKED/z_MESH_CHIP_CRACKED.jpg?raw=true" title="z_MESH_CHIP_CRACKED" /></p>
<h1>z_KEEP_BIGGER_OF_TWO</h1>
<p>takes two inputs and ouputs only one ( bigger or smaller ) </p>
<p><img alt="z_KEEP_BIGGER_OF_TWO" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_KEEP_BIGGER_OF_TWO/z_KEEP_BIGGER_OF_TWO.jpg?raw=true" title="z_KEEP_BIGGER_OF_TWO" /></p>
<h1>z_REMOVE_THIN_MESH</h1>
<p>removes prims based on thickness measurement , then can fill in holes , useful for removing thin slivers </p>
<p><img alt="z_REMOVE_THIN_MESH" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_REMOVE_THIN_MESH/z_REMOVE_THIN_MESH.jpg?raw=true" title="z_REMOVE_THIN_MESH" /></p>
<h1>z_COPY_TO_EVENLY_DISTRIBUTED_GRID</h1>
<p>copy by piecenum to dynamic evenly spaced grid - useful when baking and review</p>
<h1>z_VFX_SLASH_from_ANIM</h1>
<p>create a smoothed  swipe mesh for vfx , sword slashing</p>
<h1>z_GEN_MOSS_HANGING</h1>
<p>creates hanging placements of moss mesh , leaves , spirals . placed onto input mesh .</p>
<p><img alt="z_GEN_MOSS_HANGING" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_MOSS_HANGING/z_GEN_MOSS_HANGING.jpg?raw=true" title="z_GEN_MOSS_HANGING" /></p>
<h1>z_DRIP_GRUNGE</h1>
<ul>
<li>drips grunge under overhangs of input mesh . longer when near drip neighboors .</li>
<li>output mesh or bake vertex color</li>
</ul>
<p><img alt="z_DRIP_GRUNGE" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_DRIP_GRUNGE/z_DRIP_GRUNGE.jpg?raw=true" title="z_DRIP_GRUNGE" /></p>
<h1>z_TRIM_BORDER</h1>
<p>create trim matching input square curve , maps specific textures \ UV to sides and top bot</p>
<h1>z_UV_AXIS_ALIGN_SNAP</h1>
<p>optimize uv location , moves uvs to zero to one space for precision in games</p>
<h1>z_MESH_SLICER_SAVE</h1>
<p>separates large meshes into grided sections and exports them to fbx , options for specific area exports , and compatible with houdini engine .  </p>
<p><img alt="z_MESH_SLICER_SAVE" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_MESH_SLICER_SAVE/z_MESH_SLICER_SAVE.jpg?raw=true" title="z_MESH_SLICER_SAVE" /></p>
<h1>z_MESH_SURFACE_SIMPLE_REMESH</h1>
<p>mesh surface simple remesh ray projects a grid unto the input geo and remeshes then reduces , helpful for fixing chaotic geo and non manifold errors .</p>
<p><img alt="z_MESH_SURFACE_SIMPLE_REMESH" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_MESH_SURFACE_SIMPLE_REMESH/z_MESH_SURFACE_SIMPLE_REMESH.jpg?raw=true" title="z_MESH_SURFACE_SIMPLE_REMESH" /></p>
<h1>z_TEX_SEAM_BLENDER</h1>
<p>blend and blur a texture across uv seams to fix small bake errors and make seamless , additionally blending intersections of the meshes when surface details do not share a uvseam edge .. this is WIP bruteforce approach dividing the mesh by texel density and transfering the colors to vertexcolor bluring in worldspace proximity lastly adding in some noise counteract the blur .</p>
<h1>z_GEN_ROCK_4m</h1>
<p>generates rock surface , fractures input mesh and applies randomized offsets , setup for pdg randomness</p>
<p><img alt="z_GEN_ROCK_4m" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_ROCK_4m/z_GEN_ROCK_4m.jpg?raw=true" title="z_GEN_ROCK_4m" /></p>
<h1>z_SMOOTHING_FROM_UVs</h1>
<p>hard edges by uv island  for baking </p>
<h1>z_GEN_LATTICE_GRIDMESH</h1>
<ul>
<li>creates a box of grids with interior points automatically around the bounds of input object </li>
<li>ideal for use with lattice deformer </li>
</ul>
<p><img alt="z_GEN_LATTICE_GRIDMESH" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_LATTICE_GRIDMESH/z_GEN_LATTICE_GRIDMESH.jpg?raw=true" title="z_GEN_LATTICE_GRIDMESH" /></p>
<h1>z_REF_PROJECT_ISO</h1>
<p>project a reference image onto a floor plane , attempts to handle varied isometric settings .</p>
<h1>z_UV_TEXEL_DENSITY_CHECK</h1>
<p>check texel density with colorized debug , handles multiple materials with different texture resolutions by specifiying the materials name string and their rez</p>
<h1>z_GEN_STONE_BRICK_CIRCLE</h1>
<ul>
<li>generates a circular shaped brick section by evenly voronoi fracturing and extruding toward center .</li>
<li>applies additional noise and separation to resemble stone surface</li>
</ul>
<p><img alt="z_GEN_STONE_BRICK_CIRCLE" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_STONE_BRICK_CIRCLE/z_GEN_STONE_BRICK_CIRCLE.jpg?raw=true" title="z_GEN_STONE_BRICK_CIRCLE" /></p>
<h1>z_LIGHTMAP_UV_GEN</h1>
<p>UVs creation for lightmaps , stored to uv1 with higher merge threshold </p>
<h1>z_CURVES_FROM_UV_ISLANDS</h1>
<p>for each uv island create a line curve aligned by the longest angle or vertical\horizontal . useful for generating tree branch curves from existing low poly trees</p>
<h1>z_COLOR_MASK_VERTEX</h1>
<p><img alt="z_COLOR_MASK_VERTEX" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_COLOR_MASK_VERTEX/z_COLOR_MASK_VERTEX.jpg?raw=true" title="z_COLOR_MASK_VERTEX" /></p>
<ul>
<li>RGB mask vertex colors setups for various material / shaders .</li>
<li>AO , Variation ( random per connected element ) , </li>
<li>localized gradients ( Z axis per connected element ) </li>
<li>proximity to secondary input meshes</li>
</ul>
<h2>LAYERED VERTEX COLORS</h2>
<p>RGB vertex color setup for material blending on environment meshes .
- 0 = occlusion
- R = base
- G = direction vector 
- B = secondary mesh proximity </p>
<p>example :
dirt in crevices ( 0 ) of rock ( R ) ,  with moss on top ( G ) , near water ( B ) .</p>
<h2>VARIANTS VERTEX COLORS</h2>
<p>RGB vertex color setup for variations , example stone brick structure .
- 0 = base 
- R = vertical gradient
- G = occlusion grunge
- B = random per element</p>
<p>example :
stone base material ( 0 ) darkened by vertical gradient ( R ) ,  blending dirt in crevices ( G ) , randomly altering the brightness per brick by ( B ) .</p>
<h1>z_REVERSE_BY_N_UP</h1>
<ul>
<li>attempts to fix reversed facing ( backfacing )  normals on subobjects for an overhead camera </li>
<li>useful for fixing exports from some levels that mirrored assets with negative scaling</li>
</ul>
<p><img alt="z_REVERSE_BY_N_UP" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_REVERSE_BY_N_UP/z_REVERSE_BY_N_UP.jpg?raw=true" title="z_REVERSE_BY_N_UP" /></p>
<h1>z_MATERIAL_AUTO_ASSIGN</h1>
<p>shop materialpath auto assignment from an existing material path to the houdini scene files specific . uses regex to parse the name </p>
<h1>z_REMESH_RAY_SPHERE</h1>
<p>remesh using sphere around object , iteratively raycast and smooth to approximate shape</p>
<h1>z_UV_OVERLAP_CHECK</h1>
<p>a slow tho absolute uv overlap check , by intersection checks , separates all overlaping prims, then repacks</p>
<h1>z_MESH_WRAP_DEFORM_BY_UV</h1>
<p>deform mesh to another mesh by using the flattened UVs , useful to wrap a pattern around another</p>
<h1>z_GEN_CRACK_BRANCHING</h1>
<p>creates branching crack mesh used for booleaning other meshes</p>
<p><img alt="z_GEN_CRACK_BRANCHING" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_CRACK_BRANCHING/z_GEN_CRACK_BRANCHING.jpg?raw=true" title="z_GEN_CRACK_BRANCHING" /></p>
<h1>z_SORT_BY_LINEAXIS</h1>
<p>sorts a line contigously linearly along axis , enforcing a point order on a curved line when sort by axis may skip around</p>
<h1>z_PLANARIZE_MULTIPLE_SURFACES</h1>
<p>input mesh surface is segmented by avg n and flattened from multiple directions . useful to randomly planarize from different angles for rock meshes</p>
<p><img alt="z_PLANARIZE_MULTIPLE_SURFACES" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_PLANARIZE_MULTIPLE_SURFACES/z_PLANARIZE_MULTIPLE_SURFACES.jpg?raw=true" title="z_PLANARIZE_MULTIPLE_SURFACES" /></p>
<h1>z_GEN_TREE_TUBE_PATHFIND</h1>
<p>generate a tree using shortest path thru curves scattered and connected around collision objects and previous tree roots</p>
<h1>z_GEN_STAIRWAY</h1>
<p>generate stairway made of bricks </p>
<p><img alt="z_GEN_STAIRWAY" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_STAIRWAY/z_GEN_STAIRWAY_B.jpg?raw=true" title="z_GEN_STAIRWAY" /></p>
<p><img alt="z_GEN_STAIRWAY" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_STAIRWAY/z_GEN_STAIRWAY.jpg?raw=true" title="z_GEN_STAIRWAY" /></p>
<p><img alt="z_GEN_STAIRWAY" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_STAIRWAY/z_GEN_STAIRWAY_nodes.jpg?raw=true" title="z_GEN_STAIRWAY" /></p>
<h1>z_STAMP_FOREACH_PIECE</h1>
<ul>
<li>randomized boolean of one mesh on to the surface of variants .</li>
<li>useful for cutting runes , designs , cracks into bricks</li>
</ul>
<p><img alt="z_STAMP_FOREACH_PIECE" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_STAMP_FOREACH_PIECE/z_STAMP_FOREACH_PIECE.jpg?raw=true" title="z_STAMP_FOREACH_PIECE" /></p>
<h1>z_NORMAL_AREA_WEIGHTED</h1>
<p>normals smoothed face area weighted alternative</p>
<h1>z_COLOR_LINES_SCRATCH_VTX</h1>
<p>cuts in elipses to geo and applys vertex colors for stratches along an axis</p>
<p><img alt="z_COLOR_LINES_SCRATCH_VTX" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_COLOR_LINES_SCRATCH_VTX/z_COLOR_LINES_SCRATCH_VTX.jpg?raw=true" title="z_COLOR_MASK_VERTEX" /></p>
<h1>z_TILEABLE</h1>
<ul>
<li>copies input to each of the nearby quadrants preview tiling ( 4m default )</li>
</ul>
<p><img alt="z_TILEABLE" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_TILEABLES/z_TILEABLE.jpg?raw=true" title="z_TILEABLE" /></p>
<h1>z_TRIM_CIRCLE</h1>
<p>circular trim piece</p>
<h1>z_GEN_PETAL_FORM</h1>
<p>generates petal from curve backbone and multiple warped elipse curves defining the shape changes over the length of the backbone </p>
<p><img alt="z_GEN_PETAL_FORM" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_GEN_PETAL_FORM/z_GEN_PETAL_FORM.jpg?raw=true" title="z_GEN_PETAL_FORM" /></p>
<h1>z_KEEP_ONLY_LARGEST_CONNECTED_ELEMENT</h1>
<p>removes smaller detached objects </p>
<h1>z_NOISE_DISPLACE_MASKED</h1>
<p>using vex attribute noise with presets apply noise to hi poly mesh surface </p>
<h1>z_CURVE_FROM_TUBE</h1>
<ul>
<li>input a mesh , outputs a centered curve within the mesh , even if the topology is highly irregular</li>
<li>similar to the sidefx labs tool = Labs Straight Skeleton 3d  </li>
</ul>
<p><img alt="z_CURVE_FROM_TUBE" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_CURVE_FROM_TUBE/z_CURVE_FROM_TUBE.jpg?raw=true" title="z_CAM_ISOMETRIC" /></p>
<h1>z_COLLISION_INTERSECT_CHECK</h1>
<p>detect and show intersections with provided collision geometry . useful to avoid clipping into level geometry beyond a specific distance threshold </p>
<h1>z_REMOVE_PIECES_BY_VOLUME</h1>
<p>for each connected element , remove if doesnt match min or max measured volume , also has options of perimeter or other measurements</p>
<p><img alt="z_REMOVE_PIECES_BY_VOLUME" src="https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_REMOVE_PIECES_BY_VOLUME/z_REMOVE_PIECES_BY_VOLUME.jpg?raw=true" title="z_REMOVE_PIECES_BY_VOLUME" /></p>