import os
import sys
import glob
import pyheif
from PIL import Image

def convert_heic_to_jpg(image_dir):
    for filename in glob.glob(os.path.join(image_dir, "*.heic")):
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
    if len(sys.argv) < 2:
        print("Please provide the image directory as a command-line argument.")
        sys.exit(1)
    
    image_dir = sys.argv[1]
    convert_heic_to_jpg(image_dir)
