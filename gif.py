'''
Usage: python3 gif.py temp13 output.gif --duration 50 --pause_duration 3000

'''

import os
import imageio.v2 as imageio
from PIL import Image
import argparse

def create_looping_gif(folder: str, output_gif: str, duration: int = 200, pause_duration: int = 1000):
    # Get list of image files sorted numerically
    files = sorted([f for f in os.listdir(folder) if f.endswith('.png')], key=lambda x: int(x.split('.')[0]))
    
    if not files:
        print("No PNG files found in the folder.")
        return
    
    # Construct the loop sequence: 0,1,2,...,x-1,x,x-1,...,1,0
    images = [Image.open(os.path.join(folder, f)) for f in files]
    images += images[-2:0:-1]  # Append reversed sequence excluding first and last
    
    # Add pause duration to the last frame
    durations = [duration] * len(images)
    durations[-1] = pause_duration
    
    # Save as GIF
    images[0].save(output_gif, save_all=True, append_images=images[1:], duration=durations, loop=0)
    print(f"GIF saved as {output_gif}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a looping GIF from a folder of PNG images.')
    parser.add_argument('folder', type=str, help='Path to the folder containing PNG images')
    parser.add_argument('output_gif', type=str, help='Output GIF file path')
    parser.add_argument('--duration', type=int, default=200, help='Duration of each frame in milliseconds (default: 200)')
    parser.add_argument('--pause_duration', type=int, default=0, help='Duration of the pause before looping again in milliseconds (default: 1000)')
    
    args = parser.parse_args()
    
    create_looping_gif(args.folder, args.output_gif, args.duration, args.pause_duration)
