import os
import glob
import pyheif
from PIL import Image
# pip install pyheif Pillow

def convert_heic_to_jpg():
    for filename in glob.glob("*.heic"):
        heic_image = pyheif.read(filename)
        image = Image.frombytes(
            heic_image.mode,
            heic_image.size,
            heic_image.data,
            "raw",
            heic_image.mode,
            heic_image.stride,
        )
        jpg_filename = os.path.splitext(filename)[0] + ".jpg"
        image.save(jpg_filename, "JPEG")
        print(f"Converted {filename} to {jpg_filename}")

if __name__ == "__main__":
    convert_heic_to_jpg()
