# Python Image Scripts

### Bulk HEIC Converter

Converts HEIC/HEIF files to PNG or JPGs.

**Depedencies**

* pillow_heif

**Usage**

`python3 bulk_heic_converter.py -p /path/to/folder -t png`

-t = png|jpg


### Bulk Image Resizer

Resizes PNG and JPGs.

Right now only % scaling is possible.

**Depedencies**

* simple_chalk

**Usage**

`python3 bulk_image_resizer.py /path/to/folder 90% -t png`

-t = png|jpg


### Bulk JPG Compressor

Compresses JPGs.

**Depedencies**

* No 3rd party packages

**Usage**

`python3 bulk_jpg_compressor.py -p /path/to/folder -q 70%`

-q = 1 - 100%







