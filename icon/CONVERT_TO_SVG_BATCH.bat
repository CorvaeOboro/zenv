rem // REQUIRES IMAGE MAGICK 7.0.10 https://imagemagick.org/script/download.php
SETLOCAL ENABLEDELAYEDEXPANSION
for /r %%f in (*.jpg*) do (
set  _nametif=%%f
set  _nametga=!_nametif:.jpg=.svg!
set  _finalname=!_nametga:.jpg=.svg!
echo !_finalname!
magick convert "%%f" "!_finalname!"
)