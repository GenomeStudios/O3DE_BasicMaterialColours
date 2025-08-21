# Created by Chat GPT Free. 2025-08-20
# Created to serve as a free utility for expanding the purpose of this O3DE Gem.
# Apache-2.0 License, as stated in the repository.

import json
import os

# Path to input file and output folder
INPUT_FILE = "materials.txt"
OUTPUT_FOLDER = "GeneratedMaterials"

# Ensure output folder exists
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

def hex_to_linear_rgb(hex_color):
    """Convert hex (#RRGGBB) to linear RGB [0-1 floats]."""
    hex_color = hex_color.lstrip("#")
    r, g, b = tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))
    return [r, g, b]

def make_material_json(color_rgb):
    """Generate O3DE material JSON structure."""
    return {
        "materialType": "@gemroot:Atom_Feature_Common@/Assets/Materials/Types/StandardPBR.materialtype",
        "materialTypeVersion": 5,
        "propertyValues": {
            "baseColor.color": color_rgb
        }
    }

with open(INPUT_FILE, "r") as f:
    index = 0
    for line in f:
        line = line.strip()
        if not line or line.startswith("#"):  # skip comments/empty lines
            continue
        hex_color, name = [x.strip() for x in line.split(",")]
        rgb = hex_to_linear_rgb(hex_color)

        material_data = make_material_json(rgb)
        prefix = f"{index:03d}"  # zero-padded counter (000, 001, 002...)
        filename = f"{prefix} {name}.material"
        output_path = os.path.join(OUTPUT_FOLDER, filename)

        with open(output_path, "w") as out_file:
            json.dump(material_data, out_file, indent=4)

        print(f"Generated: {output_path}")
        index += 1
