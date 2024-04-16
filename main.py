import os
from PIL import Image
from pillow_heif import register_heif_opener
from multiprocessing import Pool

register_heif_opener()

def convert_file(args):
    src_path, dst_path = args
    with Image.open(src_path) as img:
        img.save(dst_path, "WEBP")

def convert_heic_to_webp(src_dir, dst_dir):
    tasks = []
    for root, dirs, files in os.walk(src_dir):
        for file in files:
            if file.lower().endswith(".heic"):
                src_path = os.path.join(root, file)
                rel_path = os.path.relpath(src_path, src_dir)
                dst_path = os.path.join(dst_dir, os.path.splitext(rel_path)[0] + ".webp")
                os.makedirs(os.path.dirname(dst_path), exist_ok=True)
                tasks.append((src_path, dst_path))

    with Pool() as pool:
        pool.map(convert_file, tasks)

src_directory = "src"
dst_directory = "dst"
convert_heic_to_webp(src_directory, dst_directory)
