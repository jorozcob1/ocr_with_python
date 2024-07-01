# Text Extractor using Tesseract OCR

Este script de Python automatiza la extracción de texto de imágenes utilizando la herramienta Tesseract OCR. Es útil para convertir el contenido visualizado en imágenes en texto editable, almacenándolo posteriormente en un archivo de texto para su posterior análisis o almacenamiento.

## Requisitos

Antes de ejecutar el script, asegúrate de tener instalados:

- Python 3.x
- Tesseract OCR
- Bibliotecas Python: `PIL`, `pytesseract`, `glob`, `os`

## Configuración

### Windows

Si estás utilizando Windows, es necesario configurar la ruta al ejecutable de Tesseract-OCR. Asegúrate de que Tesseract está instalado y que la ruta especificada en el script apunta correctamente al ejecutable:

```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
```
