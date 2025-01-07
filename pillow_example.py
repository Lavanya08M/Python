import sys
from PIL import Image

image1 = Image.open("images/smily.png")

try:
    with Image.open("images/smily.png") as img:
        rgb_img = img.convert("RGB")
        rgb_img.save("images/smily.jpg", "JPEG")
except FileNotFoundError:
    print(f"File not found: {input_file}")
except OSError as e:
    print(f"Error processing {input_file}: {e}")
