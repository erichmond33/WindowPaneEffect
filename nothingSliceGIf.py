"""
For the first h/v shift: python3 nothingSlice.py full_logo.png 50 {i} horizontal {i}.png
For the second h/v shift: python3 nothingSlice.py {i}.png 50 {i} vertical {i}.png

"""

import os
import sys

if __name__ == "__main__":

    try:
        first_or_second = int(sys.argv[1])
    except Exception as e:
        first_or_second = 0

    if first_or_second == 0:
        for i in range(51, 0, -1):
            os.system(f"python3 nothingSlice.py full_logo.png {i*10} {i} horizontal {i}.png")
    else:
        for i in range(51, 0, -1):
            os.system(f"python3 nothingSlice.py {i}.png {i*10} {i} vertical {i}.png")

