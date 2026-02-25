import cv2
from matplotlib import pyplot as plt
import pytesseract
from PIL import Image

# Ruta de Tesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\Ale\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Cargar la imagen
ruta_imagen = "OCR/OCR/2.png"
img = cv2.imread(ruta_imagen)

# Verificar si la imagen se cargó correctamente
if img is None:
    print(f"Error: no se pudo cargar la imagen en la ruta: {ruta_imagen}")
else:
    print("Imagen cargada correctamente.")

    # Convertir a escala de grises
    imagen_procesada = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Recortar la imagen si es necesario
    # imagen_procesada = imagen_procesada[60:220, 280:480]
 
    
    # Mostrar la imagen (opcional)
    plt.imshow(imagen_procesada, cmap='gray')
    plt.title("Imagen preprocesada (limpia)")
    plt.axis("off")
    plt.show()

    # Convertir a formato PIL
    pil_img = Image.fromarray(imagen_procesada)

    # Extraer texto con OCR
    texto = pytesseract.image_to_string(pil_img, lang='spa')  # puedes usar 'eng' para inglés

    print("📜 Texto extraído:")
    print("----------------------")
    print(texto)
    print("----------------------")
