""" Create a act file from a given color list. """
import os


def save_act_palette(rgb_colors, act_file_path):
    """ Save a list of RGB colors to an .ACT file. """
    with open(act_file_path, 'wb') as f:
        # Ensure there are exactly 256 colors in the palette
        num_colors = len(rgb_colors)
        if num_colors > 256:
            raise ValueError("The palette cannot contain more than 256 colors.")

        # Write the palette to the file
        for color in rgb_colors:
            r, g, b = color
            f.write(bytes([r, g, b]))

        # Pad the palette with black (0, 0, 0) to ensure it has 256 colors
        if num_colors < 256:
            f.write(bytes([0, 0, 0] * (256 - num_colors)))


# Example usage
example_rgb_colors = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    # Add more colors as needed
    ]

project_dir = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(project_dir, "custom_palette.act")

save_act_palette(example_rgb_colors, output_file_path)
