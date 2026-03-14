import cv2
import matplotlib.pyplot as plt
import os
import numpy as np
from PIL import Image

def convertir_a_hsv(imagen_bgr):
    """
    Convierte una imagen de espacio de color BGR a HSV.
    """
    if imagen_bgr is None:
        return None
    
    # OpenCV usa la constante COLOR_BGR2HSV
    imagen_hsv = cv2.cvtColor(imagen_bgr, cv2.COLOR_BGR2HSV)
    return imagen_hsv

'''
# ---ruta hacia la carpeta data ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "lenna.jpg"))

img = cv2.imread(ruta_imagen)

if img is not None:
    hsv_img = convertir_a_hsv(img)

    # Para visualizar los canales individuales (opcional pero muy útil en talleres)
    h, s, v = cv2.split(hsv_img)

    cv2.imshow('Original BGR', img)
    cv2.imshow('Espacio HSV (Visualización directa)', hsv_img)
    cv2.imshow('Canal Hue (Tono)', h)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"No se pudo encontrar la imagen en: {ruta_imagen}")
'''    

def graficar_histograma(image):
    """
    Calcula y grafica el histograma para los canales B, G y R.
    """
    if image is None:
        print("Error: La imagen no es válida.")
        return

    # Definimos los colores para el gráfico (OpenCV usa orden BGR)
    colores = ('b', 'g', 'r')
    
    plt.figure(figsize=(10, 5))
    plt.title('Histograma de Colores (BGR)')
    plt.xlabel('Intensidad de Píxel (0-255)')
    plt.ylabel('Número de Píxeles')

    # Iteramos sobre cada canal
    for i, col in enumerate(colores):
        # cv2.calcHist(imágenes, canales, máscara, tamañoHist, rangos)
        hist = cv2.calcHist([image], [i], None, [256], [0, 256])
        plt.plot(hist, color=col, label=f'Canal {col.upper()}')
        plt.xlim([0, 256])

    plt.legend()
    plt.grid(alpha=0.3)
    plt.show()

''''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "lenna.jpg"))

img = cv2.imread(ruta_imagen)

if img is not None:
    # Mostramos la imagen para referencia
    cv2.imshow('Imagen de referencia', img)
    
    # Llamamos a nuestra función de histograma
    graficar_histograma(img)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    '''

def cuantizacion_simple(imagen, k):
    """
    Reduce los colores de una imagen a k niveles por canal.

    Parámetros:
        imagen: numpy array (H, W) o (H, W, 3)
        k: número de niveles de color

    Retorna:
        imagen cuantizada
    """
    
    nivel = 256 // k
    
    imagen_cuantizada = (imagen // nivel) * nivel
    
    return imagen_cuantizada.astype(np.uint8)

def reduccion_peso_imagen(imagen, k, ruta_salida="cuantizada.png"):
    img_pil = Image.fromarray(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))

    img_paleta = img_pil.convert("P", palette=Image.ADAPTIVE, colors=k)

    img_paleta.save(ruta_salida)

    # peso en bytes
    peso_bytes = os.path.getsize(ruta_salida)

    # convertir a KB
    peso_kb = peso_bytes / 1024

    img_cuantizada = cv2.cvtColor(np.array(img_paleta.convert("RGB")), cv2.COLOR_RGB2BGR)

    return img_cuantizada, peso_kb

'''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "lenna.jpg"))

img = cv2.imread(ruta_imagen)

# cuantizar
k_colores = 4
img_cuantizada, peso_cuantizada = reduccion_peso_imagen(img, k_colores)
cv2.imshow(f'Cuantizada a {k_colores} colores', img_cuantizada)
cv2.imshow('Original', img)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Peso cuantizada:", round(peso_cuantizada, 2), "KB")
'''