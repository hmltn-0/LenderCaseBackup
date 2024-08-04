from pdf2image import convert_from_path
import os

def pdf_to_images(pdf_path, output_dir):
    script_output_dir = os.path.join(output_dir, "convert_pdf_to_images_absolute_output")
    os.makedirs(script_output_dir, exist_ok=True)
    
    images = convert_from_path(pdf_path)
    for i, image in enumerate(images):
        image.save(f'{script_output_dir}/page_{i+1}.png')
        print(f'Saved {script_output_dir}/page_{i+1}.png')

pdf_path = '/Users/juliushamilton/Lender_Contract_Reversal_Case/Contracts/2019 Chevy Equinox.pdf'
output_dir = '/Users/juliushamilton/Lender_Contract_Reversal_Case/Contracts/output_images'

if __name__ == '__main__':
    pdf_to_images(pdf_path, output_dir)
