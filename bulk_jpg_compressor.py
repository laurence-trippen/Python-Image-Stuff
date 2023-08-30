from PIL import Image

import os
import sys
import argparse
import re


def validate_path(path: str):
  if path is None:
    print("No path specified!")
    sys.exit(-1)

  if not os.path.isdir(path):
    print("Path doesn't exist!")
    sys.exit(-1)


def validate_quality(quality: str):
  if quality is None:
    print("No quality specified!")
    sys.exit(-1)

  pattern = r'^(?:[1-9][0-9]?|100)%$'
  if re.match(pattern, quality) is None:
    print(f"Invalid quality (1-100%)")
    sys.exit(-1)


def extract_quality(quality: str):
  number_str = quality.replace("%", "")
  return int(number_str)


def find_jpg_files(path: str) -> list:
  jpg_extensions = ["jpg", "jpeg"]

  files_to_compress = []

  for file in os.listdir(path):
    for ext in jpg_extensions:
      if file.endswith(f".{ext}") or file.endswith(f".{ext.upper()}"):
        files_to_compress.append(file)
  
  return files_to_compress


def compress_jpgs(path: str, jpegs: list, quality: int):
  for jpeg in jpegs:
    file_path = os.path.join(path, jpeg)
    
    image = Image.open(file_path)

    only_file_name = os.path.splitext(jpeg)[0]
    output_path = os.path.join(path, only_file_name + f"_q{quality}.jpg")

    image.save(output_path, "JPEG", optimize=True, quality=quality)

    print(f"Optimized {output_path}")



def main():
  parser = argparse.ArgumentParser(description="Bulk JPG compressor")
  parser.add_argument("-p", "--path", help="Path")
  parser.add_argument("-q", "--quality", help="Quality 1-100%")

  args = parser.parse_args()

  print(args)

  validate_path(args.path)
  validate_quality(args.quality)

  quality = extract_quality(args.quality)
  jpegs = find_jpg_files(args.path)

  compress_jpgs(args.path, jpegs, quality)

  print("Done!")


if __name__ == '__main__':
  main()
