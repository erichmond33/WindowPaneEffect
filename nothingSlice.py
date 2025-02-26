# '''
# This program takes an image and splits it into segments, then recombines the segments into a new image.
# The segments look really cool if the shift is about half of the segment width i.e. width=100px shift=50px.
# The split direction can be "horizontal" or "vertical".
# Run the script twice swiching the split direction to get both horizontal and vertical slices.

# Example script usage:
# python3 nothingSlice.py input_image.png 100 50 horizontal output_image.png
# '''

from PIL import Image
import sys

def split_and_recombine_image(input_image_path, output_image_path, segment_width, segment_shift, split_direction="horizontal"):
    try:
        # Open the input image
        image = Image.open(input_image_path)

        # Get the image dimensions
        width, height = image.size

        # Initialize variables for tracking segments and output image
        segments = []
        current_x, current_y = 0, 0

        if split_direction == "horizontal":
            # Split the image horizontally
            while current_x <= width:
                right_boundary = min(current_x + segment_width, width)
                segment = image.crop((current_x, 0, right_boundary, height))
                segments.append(segment)
                current_x += segment_shift

            total_width = len(segments) * segment_width
            output_image = Image.new('RGBA', (total_width, height))
            current_x = 0
            for segment in segments:
                output_image.paste(segment, (current_x, 0))
                current_x += segment_width

        elif split_direction == "vertical":
            # Split the image vertically
            while current_y <= height:
                bottom_boundary = min(current_y + segment_width, height)
                segment = image.crop((0, current_y, width, bottom_boundary))
                segments.append(segment)
                current_y += segment_shift

            total_height = len(segments) * segment_width
            output_image = Image.new('RGBA', (width, total_height))
            current_y = 0
            for segment in segments:
                output_image.paste(segment, (0, current_y))
                current_y += segment_width

        else:
            print("Invalid split_direction. Please use 'horizontal' or 'vertical'.")
            return

        # Resize the output image to match the size of the original
        output_image = output_image.resize((width, height), Image.Resampling.LANCZOS)

        # Save the recombined image
        output_image.save(output_image_path)

        print(f"Image split into {len(segments)} segments and recombined successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")



if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python script.py input_image.png segment_width segment_shift split_direction output_image.png")
        sys.exit(1)

    input_image_path = sys.argv[1]
    segment_width = int(sys.argv[2])
    segment_shift = int(sys.argv[3])
    split_direction = sys.argv[4]
    output_image_path = sys.argv[5]

    split_and_recombine_image(input_image_path, output_image_path, segment_width, segment_shift, split_direction)