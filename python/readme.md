# ZENV PYTHON SCRITPS

- HOUDINI_HDA_PLACE_ALL.py = for each hda in a folder creates hython script to place the nodes in houdini 
- HOUDINI_PATH_TOPs_CREATE_SET.py = creates hython script to place TOP nodes for each PATH mesh component
- UNREAL_PATH_CREATE_SNAPMAPS.py = for each set of PATH meshes creates unreal map for each corresponding variant
- ZENV_GITHUB_DOC_GEN.py = creates readme and docs from googlesheet and existing files 

## HOUDINI_HDA_PLACE_ALL.py
- for each .hda in a target folder creates hython script to place the nodes in houdini 
- creates a txt file with the hython code 
- copy paste into houdini's python shell ( Houdini > Windows > Python Shell )
- places all sop hda nodes into geometry node
- this is used to review and make updates to toolset , additionally used to create the ALL_HDA example

## HOUDINI_PATH_TOPs_CREATE_SET.py
- creates hython script to place TOP nodes for each PATH mesh component
- creates a txt file with the hython code 
- copy paste into houdini's python shell ( Houdini > Windows > Python Shell )
- all PATH variants of TURN , START / END , STRAIGHT , placed as TOP PDG nodes 
- this is used to generate all the meshes of a PATH type , for use in Unreal as SnapMap with DungeonArchitect 

![HOUDINI_PATH_TOPs_CREATE_SET](https://raw.githubusercontent.com/CorvaeOboro/zenv/master/python/HOUDINI_PATH_TOPs_CREATE_SET.png?raw=true "HOUDINI_PATH_TOPs_CREATE_SET")

## UNREAL_PATH_CREATE_SNAPMAPS.py
- for each set of PATH meshes creates unreal map for each corresponding variant .
- this is used to create/populated SnapMap levels for use with the DungeonArchitect plugin 
- enable unreal Python Editor Script Plugin , https://docs.unrealengine.com/5.1/en-US/scripting-the-unreal-editor-using-python/
- Unreal > Tools > Execute Python Script
- in Unreal given a set of templates map levels , corresponding to the TURN , START / END , STRAIGHT variants 
- duplicates the map template and places corresponding PATH meshs

## ZENV_GITHUB_DOC_GEN.py
- creates readme and docs from googlesheet and existing files 
- authorize access via google credentials.json
- googlesheet contains a list of the HDA tools , along side their category , order , notes , and status of example and images 

![ZENV_GITHUB_DOC_GSHEET](https://raw.githubusercontent.com/CorvaeOboro/zenv/master/python/ZENV_GITHUB_DOC_GSHEET.png?raw=true "ZENV_GITHUB_DOC_GSHEET")

- a copy of the repo is locally cloned to review 
- new hdas found are added to the googlesheet , and datemodified updated , if no notes exist the last git commit notes are used .
- main readme table list is generated , by category order , then ordered within category 
- all individual hip readmes are combined by same order for the VIEW_ALL.md , additional combined readmes created per category .
- readme.md for all hips are converted to html for docs , including the combined versions
- collapsable menu generated for the docs website as html 

![ZENV_GITHUB_DOCS_MENU](https://raw.githubusercontent.com/CorvaeOboro/zenv/master/python/ZENV_GITHUB_DOCS_MENU.png?raw=true "ZENV_GITHUB_DOCS_MENU")

