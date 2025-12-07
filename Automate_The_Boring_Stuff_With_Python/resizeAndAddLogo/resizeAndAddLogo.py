# Resizes images to fit in a 300x300 square with a logo in the corner
from math import log
import os
from PIL import Image

SQUARE_FIT_SIZE = 300
LOGO_FILENAME = 'catlogo.png'

logo_im = Image.open(LOGO_FILENAME)
logo_im = logo_im.resize((50, 50))
logo_width, logo_height = logo_im.size

# Convert logo to RGBA to support transparency
if logo_im.mode != 'RGBA':
    logo_im = logo_im.convert('RGBA')


os.makedirs('withLogo', exist_ok=True)
for filename in os.listdir('.'):
    if not (filename.endswith('.png') or filename.endswith('.jpg')) or filename == LOGO_FILENAME:
        continue
    im = Image.open(filename)
    width, height = im.size

    if width > SQUARE_FIT_SIZE and height > SQUARE_FIT_SIZE:
        if width > height:
            height = int((SQUARE_FIT_SIZE / width) * height)
            width = SQUARE_FIT_SIZE
        else:
            width = int((SQUARE_FIT_SIZE / height) * width)
            height = SQUARE_FIT_SIZE
        print(f'Resizing {filename}...')
        im = im.resize((width, height))

    print(f'Adding logo to {filename}...')
    im.paste(logo_im, (width - logo_width, height - logo_height), logo_im)

    im.save(os.path.join('withLogo', filename))