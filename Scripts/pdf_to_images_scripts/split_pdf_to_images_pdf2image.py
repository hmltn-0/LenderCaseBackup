from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_dir):
    # Convert PDF to list of images
    images = convert_from_path(pdf_path)
    
    # Ensure output directory exists
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Save images
    for idx, image in enumerate(images):
        img_path = os.path.join(output_dir, f'page_{idx + 1}.png')
        image.save(img_path, 'PNG')
        print(f'Saved {img_path}')

if __name__ == '__main__':
    pdf_path = '../Contracts/2019 Chevy Equinox.pdf'  # actual PDF file path
    output_dir = '../Contracts/output_images'
    pdf_to_images(pdf_path, output_dir)
