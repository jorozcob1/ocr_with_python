from PIL import Image
import pytesseract
import glob
import os
# Specify the path to the Tesseract-OCR executable (only for Windows)
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_ext = ['*.jpeg', '*.jpg', '*.png', '*.gif', '*.bmp', '*.tiff', '*.tif', '*.webp']
directory = 'images/'
image_files = []
for ext in image_ext:
  if glob.glob(os.path.join(directory, ext)):
    image_files.extend(glob.glob(os.path.join(directory, ext)))

if not image_files:
    print('No se encontraron imágenes en el directorio especificado.')
    exit()
else:
  for img in image_files:
    print(img)
    # Open an image file
    image = Image.open(img)
    # Use pytesseract to do OCR on the image
    extracted_text = pytesseract.image_to_string(image)
    output_file_name = 'extracted_text.txt'
    # Print the extracted text
    with open(output_file_name, 'a') as file:
        file.write('-'*50 + '\n')
        file.write(extracted_text)
        #file.write('\n')
    print(f'Texto extraído guardado en {output_file_name}.')
    print(extracted_text)