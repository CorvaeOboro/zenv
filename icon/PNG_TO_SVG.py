from pathlib import Path
from svgtrace import trace
import glob
import os

rootdir = os.path.dirname(os.path.abspath(__file__))
png_images = glob.glob(os.path.join(rootdir, "*.png"))
print(png_images)
for current_png_image in png_images:
    print(current_png_image)
    output_name = Path(current_png_image).stem + ".svg"
    output_filepath = str(rootdir) +"/" + str(output_name)
    #current_svg_image = current_png_image.write_text(trace(f"{logoFile}.png"), encoding="utf-8")
    Path(output_filepath).write_text(trace(current_png_image), encoding="utf-8")
    print(output_name)