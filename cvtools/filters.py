import cv2
import os
import numpy as np

def aplicar_convolucion(imagen, kernel):
    """
    1. Implementa una convolución genérica.
    El parámetro -1 mantiene la misma profundidad (depth) que la imagen original.
    """
    if imagen is None: return None
    return cv2.filter2D(imagen, -1, kernel)

def filtro_sobel(imagen):
    """
    2. Aplica el filtro Sobel en los ejes X e Y.
    """
    if imagen is None: return None
    
    # Convertir a escala de grises si es necesario
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) if len(imagen.shape) == 3 else imagen
    
    sobel_x = cv2.Sobel(gris, cv2.CV_64F, 1, 0, ksize=3)
    sobel_y = cv2.Sobel(gris, cv2.CV_64F, 0, 1, ksize=3)
    
    # Convertir de vuelta a 8 bits para visualización
    abs_sobel_x = cv2.convertScaleAbs(sobel_x)
    abs_sobel_y = cv2.convertScaleAbs(sobel_y)
    
    return abs_sobel_x, abs_sobel_y

def detector_canny(imagen, umbral_bajo=50, umbral_alto=150):
    """
    3. Implementa el detector de bordes Canny.
    """
    if imagen is None: return None
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) if len(imagen.shape) == 3 else imagen
    return cv2.Canny(gris, umbral_bajo, umbral_alto)

def filtro_laplaciano(imagen):
    """
    4. Implementa el filtro Laplaciano.
    """
    if imagen is None: return None
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY) if len(imagen.shape) == 3 else imagen
    
    laplacian = cv2.Laplacian(gris, cv2.CV_64F)
    return cv2.convertScaleAbs(laplacian)

''''
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
ruta_imagen = os.path.join(BASE_DIR, "..", "data", "lenna.jpg")
img = cv2.imread(ruta_imagen)

if img is not None:
    # 1. Probar Convolución (Filtro de desenfoque/Average)
    kernel_blur = np.ones((5, 5), np.float32) / 25
    img_blur = aplicar_convolucion(img, kernel_blur)
    
    # 2. Probar Sobel
    s_x, s_y = filtro_sobel(img)
    
    # 3. Probar Canny
    bordes_canny = detector_canny(img)
    
    # 4. Probar Laplaciano
    bordes_laplace = filtro_laplaciano(img)

    # Mostrar resultados
    cv2.imshow('Original', img)
    cv2.imshow('1. Convolucion (Blur)', img_blur)
    cv2.imshow('2. Sobel X (Verticales)', s_x)
    cv2.imshow('2. Sobel Y (Horizontales)', s_y)
    cv2.imshow('3. Canny (Bordes definidos)', bordes_canny)
    cv2.imshow('4. Laplaciano (Estructura)', bordes_laplace)

    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print(f"Error: No se pudo cargar la imagen en {ruta_imagen}")
'''