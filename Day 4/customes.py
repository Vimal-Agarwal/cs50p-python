import sys  # To access command-line arguments passed when running the script

from PIL import Image  # PIL (Pillow) library to work with images

images = []  # Empty list to store all opened image objects

# sys.argv[1:] skips the script name (sys.argv[0] = "costumes.py")
# Remaining args are the image filenames passed in terminal
for arg in sys.argv[1:]:
    image = Image.open(arg)   # Open each image file (e.g. costume1.gif)
    images.append(image)      # Add the image object to our list

# Save the first image as an animated GIF
images[0].save(
    "costumes.gif",            # Output filename
    save_all=True,             # Save all frames, not just the first
    append_images=[images[1]], # Append remaining images as extra frames
    duration=200,              # Time per frame in milliseconds (not visible here)
    loop=0                     # 0 = loop forever
)