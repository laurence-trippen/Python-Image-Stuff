from PIL import Image
from pillow_heif import register_heif_opener

import os
import sys
import argparse


def validate_file_type(file_type):
  if file_type != 'jpg' and file_type != 'png':
    sys.exit(f"Unknown file type '{file_type}'!")


def find_heic_files(path):
  files_to_convert = []

  for file in os.listdir(path):
    if file.endswith(".HEIC") or file.endswith(".heic"):
      files_to_convert.append(os.path.join(path, file))

  return files_to_convert


def main():
  register_heif_opener()

  arg_parser = argparse.ArgumentParser(description="Converts HEIC to JPG or PNG images.")
  arg_parser.add_argument("-p", "--path", help="Path")
  arg_parser.add_argument("-t", "--file-type", help="jpg | png")

  args = arg_parser.parse_args()

  validate_file_type(args.file_type)

  heic_files = find_heic_files(args.path) 

  for heic in heic_files:
    full_file_name = os.path.basename(heic)

    file_name = os.path.splitext(full_file_name)[0]

    output_path = os.path.join(args.path, file_name + f'.{args.file_type}')

    image = Image.open(heic)
    image.convert('RGB').save(output_path)

    print(f'Generated {output_path}')

  print('Done!')


if __name__ == '__main__':
  main()
