from PIL import Image
from simple_chalk import chalk


import argparse
import re
import os
import sys


def validate_path(path: str):
  if not os.path.isdir(path):
    print(chalk.red("Path doesn't exist!"))
    sys.exit(-1)


def validate_size(size: str):
  pattern = r'\d+(?:%|px)'
  if not re.match(pattern, size):
    print(chalk.red(f"Unknown size type {size}!\nPlease use px or %"))
    sys.exit(-1)


def validate_filetype(file_type: str):
  if file_type != 'png' and file_type != 'jpg':
    print(chalk.red(f"Unknow file type {file_type}! Please use 'png' or 'jpg'."))


def find_input_files(path: str, type: str) -> list:
  files_to_resize = []

  for file in os.listdir(path):
    if file.endswith(type) or file.endswith(type.upper()):
      files_to_resize.append(os.path.join(path, file))

  return files_to_resize


def calculate_new_size(input_size: str, original_size: tuple[int, int]) -> tuple[int, int]:
  if input_size.endswith("%"):
    new_size = input_size.replace("%", "")

    percantage = int(new_size)
    multiplier = percantage / 100

    width, height = original_size

    return (width * multiplier, height * multiplier)
    
  elif input_size.endswith("px"):
    pass


def resize_images(files: list, input_size: str, path: str, type: str):
  for file in files:
    full_file_name = os.path.basename(file)
    file_name = os.path.splitext(full_file_name)[0]

    image = Image.open(file)

    new_width, new_height = calculate_new_size(input_size, image.size)

    resized_image = image.resize((round(new_width), round(new_height)))

    output_path = os.path.join(path, file_name + f"_resized.{type}")

    resized_image.save(output_path)

    print(f"Resized: {output_path}")


def main():
  print(chalk.green("LT Bulk Image Resizer v0.1.0"))

  parser = argparse.ArgumentParser(description="Image Resizer")

  parser.add_argument("path")
  parser.add_argument("size")
  parser.add_argument("-t", "--type")

  args = parser.parse_args()

  validate_path(args.path)
  validate_size(args.size)
  validate_filetype(args.type)

  files_to_resize = find_input_files(args.path, args.type)

  resize_images(files_to_resize, args.size, args.path, args.type)

  print("Done!")


if __name__ == '__main__':
  main()

