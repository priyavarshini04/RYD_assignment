import os

book_images = os.path.join(os.getcwd(),'images')

for book in os.listdir(book_images):
    for image in os.listdir(os.path.join(book_images,book)):
        cmd = f"tesseract -l hin images/{book}/{image} out/{book}/{image[:-4]}"
        os.system(cmd)
