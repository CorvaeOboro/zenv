# z_COLOR_MASK_VERTEX

![z_COLOR_MASK_VERTEX](https://raw.githubusercontent.com/CorvaeOboro/zenv/master/hip/z_COLOR_MASK_VERTEX/z_COLOR_MASK_VERTEX.jpg?raw=true "z_COLOR_MASK_VERTEX")

- RGB mask vertex colors setups for various material / shaders .
- AO , Variation ( random per connected element ) , 
- localized gradients ( Z axis per connected element ) 
- proximity to secondary input meshes

## LAYERED VERTEX COLORS
RGB vertex color setup for material blending on environment meshes .
- 0 = occlusion
- R = base
- G = direction vector 
- B = secondary mesh proximity 

example :
dirt in crevices ( 0 ) of rock ( R ) ,  with moss on top ( G ) , near water ( B ) .

## VARIANTS VERTEX COLORS
RGB vertex color setup for variations , example stone brick structure .
- 0 = base 
- R = vertical gradient
- G = occlusion grunge
- B = random per element

example :
stone base material ( 0 ) darkened by vertical gradient ( R ) ,  blending dirt in crevices ( G ) , randomly altering the brightness per brick by ( B ) .