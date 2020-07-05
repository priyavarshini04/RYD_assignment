import os 
import pdf2image
import PyPDF2
from pdf2image import convert_from_path


from pdf2image.exceptions import (
 PDFInfoNotInstalledError,
 PDFPageCountError,
 PDFSyntaxError
)

def image_converter(book,books_dir):
    os.mkdir(book)
    reader = PyPDF2.PdfFileReader(open(f'{books_dir}/{book}','rb'))
    max_pages = reader.getNumPages()
    for page in range(1,max_pages,10):
        images = convert_from_path(f'{books_dir}/{book}',dpi = 200,first_page = page, last_page = min(page+10,max_pages))
        for i, image in zip(range(page,page+len(images)),images):
            fname = "image" + str(i) + ".png"
            image.save(f"{book}/{fname}", "PNG")

books_dir = os.path.join(os.getcwd(),'book/Hindi')
books_list = os.listdir(books_dir)

for book in books_list:
        print(f"converting {book}...")
        image_converter(book,books_dir)
    
