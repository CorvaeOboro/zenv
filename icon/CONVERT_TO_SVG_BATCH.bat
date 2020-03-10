rem // REQUIRES IMAGE MAGICK 7.0.10 https://imagemagick.org/script/download.php
SETLOCAL ENABLEDELAYEDEXPANSION
for /r %%f in (*.png*) do (
set  _nametif=%%f
set  _nametga=!_nametif:.png=.svg!
set  _finalname=!_nametga:.png=.svg!
echo !_finalname!
magick convert "%%f" "!_finalname!"
)