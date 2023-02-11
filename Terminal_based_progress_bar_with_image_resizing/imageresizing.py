'''
    # Terminal Progress bar with image Resizing
    Here I just take example of image resizing for displaying progress bar.
    when we convert lots of images at time we can use progress bar to
    show how many images are resized.
    ### For this purpose I am using tqdm librabry
    ` pip install tqdm `
    This Library is for showing progress bar
    ### For Resizing images
    ` pip install Pillow `
'''

from tqdm import tqdm
from PIL import Image
import os
from time import sleep


def resize_image(size, image):
    if os.path.isfile(image):
        try:
            im = Image.open(image)
            im.thumbnail(size, Image.ANTIALIAS)
            # im.save("resize/" + str(image) + "jpg")
            im.save("resize/" + str(image))
        except Exception as ex:
            print(f"Error: {str(ex)} to {image}")

path = input("Enter Path to images:")
size = input("Size Height, Width:")
size = tuple(map(int, size.split(",")))

os.chdir(path)

list_images = os.listdir(path)
if "resize" not in list_images:
    os.mkdir("resize")

for image in tqdm(list_images, desc="Resizing Images"):
    resize_image(size, image)
    sleep(0.1)

print("Resizing Completed")