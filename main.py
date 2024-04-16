import os
from PIL import Image
from pathlib import Path

def convert_heic_to_webp(src_dir, dst_dir):
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(".heic"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, src_dir)
                dst_path = os.path.join(dst_dir, os.path.splitext(rel_path)[0] + ".webp")
                
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                
                with Image.open(src_path) as img:
                    img.save(dst_path, "WEBP")

src_directory = "src"
dst_directory = "dst"
convert_heic_to_webp(src_directory, dst_directory)
