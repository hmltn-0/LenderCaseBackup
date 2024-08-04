import fitz
import os

def pdf_to_images(pdf_path, output_dir):
    # Open the PDF file
    pdf_document = fitz.open(pdf_path)
    
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Iterate over each page and save as image
    for page_num in range(len(pdf_document)):
        page = pdf_document[page_num]
        pix = page.get_pixmap()
        img_path = os.path.join(output_dir, f'page_{page_num + 1}.png')
        pix.save(img_path)
        print(f'Saved {img_path}')

if __name__ == '__main__':
    pdf_path = '../Contracts/2019 Chevy Equinox.pdf'  # replace with your PDF file name
    output_dir = 'output_images'
    pdf_to_images(pdf_path, output_dir)
