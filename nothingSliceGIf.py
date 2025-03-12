"""
For the first h/v shift: python3 nothingSlice.py full_logo.png 50 {i} horizontal {i}.png
For the second h/v shift: python3 nothingSlice.py {i}.png 50 {i} vertical {i}.png

Setup: Change INPUT_FILE and OUTPUT_FILE
Usage: python3 nothingSliceGif.py 0

"""

import os
import sys

INPUT_FILE = "~/Downloads/temp13_w.png"
OUTPUT_FOLDER = "temp13/"

if __name__ == "__main__":
    os.system(f"cp {INPUT_FILE} {OUTPUT_FOLDER}0.png")

    try:
        first_or_second = int(sys.argv[1])
    except Exception as e:
        first_or_second = 0

    if first_or_second == 0:
        for i in range(101, 0, -1):
            os.system(f"python3 nothingSlice.py {INPUT_FILE} {i*10} {i} horizontal {OUTPUT_FOLDER}{i}.png")
        os.system(f"python3 center.py {OUTPUT_FOLDER}")
    else:
        for i in range(51, 0, -1):
            os.system(f"python3 nothingSlice.py {i}.png {i*10} {i} vertical /temp13/{i}.png")

