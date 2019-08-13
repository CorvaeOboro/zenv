## Z_HOUDINI ##
collection of houdini hda's focused on procedural modelling and game dev

## PLACEMENT ##
- **[z_COPY_TO_POINTS_BY_PIECENUM_INTERSECTIONCHECK](https://github.com/corvaeoboro/zhoudini/)** : Place an array of pieces using collision checks to avoid intersection
- **[z_TRANSFORM_ITERATE_COLLISION_CHECK](https://github.com/corvaeoboro/zhoudini/)** : move pieces towards goal while avoid itersection and collision ( simple gravity but sop based ) 
- **[Z_WIRE_OVERLAP_OFFSET](https://github.com/corvaeoboro/zhoudini/)** : sop base polywire tubes ray onto floor/collision and crossover each other 

## GENERATIVE ##
- **[z_curlnoise_lines_loop](https://github.com/corvaeoboro/zhoudini/)** : additive curlnoise deformation of the wireframe to produce smooth abstract curveson given mesh
- **[z_GEN_BRICKMAIN_01](https://github.com/corvaeoboro/zhoudini/)** : generate set of stone bricks given mesh from input ( produces pieces with piecenum ) percentage of them fractured 
- **[z_gen_chipped_cracked](https://github.com/corvaeoboro/zhoudini/)** : apply edge wear and boolean crack shapes onto mesh from input 
- **[z_GEN_CIRCLES_RADIATE_PATTERN](https://github.com/corvaeoboro/zhoudini/)** : points ripple circles outward , older circles can not be overlaped by younger ( booleaned ) 
- **[z_gen_crack](https://github.com/corvaeoboro/zhoudini/)** : generate crack shape mesh , for cutting or other
- **[z_GEN_STAIRWAY](https://github.com/corvaeoboro/zhoudini/)** : generate a stone stairway following a curve and avoiding collision given brick like shapes from other generators .

## MODIFY ##
- **[Z_MESH_WRAP_BY_UV](https://github.com/corvaeoboro/zhoudini/)** : deform a mesh by uvs of another mesh ( wrapping flat pattern to a cyllinderical object ) 
- **[z_SHRINKWRAP_VORONOI_CLUSTERS](https://github.com/corvaeoboro/zhoudini/)** : voronoi fracture input , then for each piece shrinkwrap . creates a fast convex version , useful for rock shapes
- **[z_STAMP_FOREACH_PIECE](https://github.com/corvaeoboro/zhoudini/)** : given a set of pieces ( bricks ) and a set of stamps ( runes ) this will boolean the stamp on the pieces with randomized range of transforms .
- **[z_VDB_INTERNAL_FILL](https://github.com/corvaeoboro/zhoudini/)** : vdb from polygons as multiple levels of resolution and erode the lower resolutions then combine . this is helpful for the low poly  or to fill small internal crevases ( shallow cracks ) 
- **[z_VORONI_FRACTURE_GRADIENT_OFFSET](https://github.com/corvaeoboro/zhoudini/)** : fracture with voronoi then for each piece move based on bounding box gradient . useful for cliff and rock faces  

## CLEANUP ##
- z_KEEP_ONLY_LARGEST_CONNECTED_ELEMENT
- z_REMOVE_PIECES_BY_VOLUME
- z_UV_OVERLAP_CHECK

## UE4 HDAS (WIP) ##
- HAPI_Test_Curves_ObjectMergeInput
- ue4_SAVE_INPUTS
- z_mesh_subtract_collapse

