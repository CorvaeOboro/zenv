rem // REQUIRES IMAGE MAGICK 7.0.10 https://imagemagick.org/script/download.php
SETLOCAL ENABLEDELAYEDEXPANSION
for /r %%f in (*.psd) do (
set  _nametif=%%f
set  _nametga=!_nametif:.psd=.png!
set  _finalname=!_nametga:.psd=.png!
echo !_finalname!
magick convert "%%f[0]" "!_finalname!"
)