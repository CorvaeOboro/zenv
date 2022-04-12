# z_TEX_SEAM_BLENDER

blend and blur a texture across uv seams to fix small bake errors and make seamless , additionally blending intersections of the meshes when surface details do not share a uvseam edge .. this is WIP bruteforce approach dividing the mesh by texel density and transfering the colors to vertexcolor bluring in worldspace proximity lastly adding in some noise counteract the blur .

