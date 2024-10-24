from PIL import Image
import os
import glob

# Tell the script where your downloads directory is
download_dir = os.path.expanduser('~/Downloads')

# Find all .webp files in the downloads directory
webp_files = glob.glob(os.path.join(download_dir, '*.webp'))

for webp_file in webp_files:
    # Open the .webp file
    with Image.open(webp_file) as img:
        # Define the new file name
        png_file = webp_file.rsplit('.', 1)[0] + '.png'
        # Save the image as .png
        img.save(png_file, 'PNG')
        # Remove the original .webp file
        os.remove(webp_file)
        # Done
