from PIL import Image
import os
import sys

# Check if the folder path is provided as a command line argument
if len(sys.argv) != 2:
    print("Usage: python center.py <folder_path>")
    sys.exit(1)

# Get the folder path from the command line argument
folder_path = sys.argv[1]

# Function to find the bounds of the non-transparent region
def find_non_transparent_bounds(image):
    width, height = image.size
    left_bound = width
    right_bound = 0

    # Convert image to RGBA if it isn't already
    if image.mode != "RGBA":
        image = image.convert("RGBA")

    # Get pixel data
    pixels = image.load()

    # Scan each row to find the leftmost and rightmost non-transparent pixels
    for y in range(height):
        for x in range(width):
            r, g, b, a = pixels[x, y]
            # Check if the pixel is non-transparent (alpha > 0)
            if a > 0:
                left_bound = min(left_bound, x)
                right_bound = max(right_bound, x)

    return left_bound, right_bound

# Function to center the non-transparent region
def center_non_transparent_region(image):
    width, height = image.size

    # Find the bounds of the non-transparent region
    left_bound, right_bound = find_non_transparent_bounds(image)

    # If no non-transparent region is found, return the original image
    if left_bound >= right_bound:
        return image

    # Calculate the width of the non-transparent region
    region_width = right_bound - left_bound + 1

    # Calculate the current center of the non-transparent region
    current_center = left_bound + (region_width // 2)

    # Calculate the target center (middle of the image)
    target_center = width // 2

    # Calculate the shift needed to center the region
    shift = target_center - current_center

    # Create a new blank image with the same size and transparent background
    new_image = Image.new("RGBA", (width, height), (0, 0, 0, 0))

    # Crop the non-transparent region
    region = image.crop((left_bound, 0, right_bound + 1, height))

    # Calculate the new left position after shifting
    new_left = left_bound + shift

    # Paste the region into the new image at the centered position
    new_image.paste(region, (new_left, 0))

    return new_image

# Process all images in the folder
for filename in os.listdir(folder_path):
    if filename.lower().endswith((".png", ".jpg", ".jpeg", ".bmp", ".gif")):
        # Load the image
        image_path = os.path.join(folder_path, filename)
        image = Image.open(image_path)

        # Center the non-transparent region
        centered_image = center_non_transparent_region(image)

        # Save the centered image to the same folder
        output_path = os.path.join(folder_path, f"{filename}")
        centered_image.save(output_path)

        print(f"Processed: {filename} -> {output_path}")

print("All images have been processed!")