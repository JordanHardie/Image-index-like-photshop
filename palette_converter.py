""" Convert a JPG image to a given color palette. """
import os
from PIL import Image

def load_act_palette(act_file_path):
    """ Load a color palette from an .ACT file and pad it to 256 colors if necessary. """
    with open(act_file_path, 'rb') as f:
        # Read the file in chunks of 3 bytes (RGB).
        raw_palette = f.read(768)  # 256 * 3
        num_colors = len(raw_palette) // 3

        palette = []
        for i in range(num_colors):
            r = raw_palette[3*i]
            g = raw_palette[3*i + 1]
            b = raw_palette[3*i + 2]
            palette.extend([r, g, b])

        # Pad the palette with black (0, 0, 0) to ensure it's 256 colors long
        if num_colors < 256:
            palette.extend([0, 0, 0] * (256 - num_colors))

        return palette

def convert_to_indexed_color(image_path, act_palette_path, output_path, dither=False):
    """ Convert an image to use a color palette from an .ACT file. """
    # Load the image.
    image = Image.open(image_path)

    # Load the .ACT palette.
    palette = load_act_palette(act_palette_path)

    # Convert the image to "P" mode (palette mode) using the loaded palette.
    palette_image = Image.new("P", (1, 1))
    palette_image.putpalette(palette)

    # Convert the image using the palette.
    if dither:
        converted_image = image.convert("RGB").quantize(palette=palette_image)
    else:
        converted_image = image.convert("RGB").quantize(palette=palette_image, dither=None)

    # Save the resulting image.
    converted_image.save(output_path, format="PNG")

project_dir = os.path.dirname(os.path.abspath(__file__))

def get_paths():
    """ Get the paths to the image and the ACT file. """
    input_image_path = os.path.join(project_dir, "image.jpg")
    act_file_path = os.path.join(project_dir, "custom_palette.act")
    output_image_path = os.path.join(project_dir, "output_image.png")
    return input_image_path, act_file_path, output_image_path

iip, afp, oip = get_paths()

convert_to_indexed_color(iip, afp, oip, dither=True)
