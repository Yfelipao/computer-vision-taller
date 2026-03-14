import cv2
import numpy as np
import os
import sys

# Asegurar que Python encuentre el módulo cvtools
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cvtools.filters import aplicar_convolucion, filtro_sobel, detector_canny, filtro_laplaciano

def cargar_imagen_test():
    """Carga la imagen usando la lógica de rutas del proyecto."""
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(BASE_DIR, "..", "data", "lenna.jpg")
    img = cv2.imread(ruta_imagen)
    return img, ruta_imagen

def test_convolucion_generica():
    print("Ejecutando: test_convolucion_generica...")
    img, _ = cargar_imagen_test()
    if img is None: return

    # Definimos un kernel de desenfoque (blur) de 5x5
    kernel = np.ones((5, 5), np.float32) / 25
    resultado = aplicar_convolucion(img, kernel)

    if resultado is not None and resultado.shape == img.shape:
        print("[PASÓ] Convolución aplicada correctamente.")
    else:
        print("[FALLÓ] Error en la aplicación de la convolución.")

def test_sobel():
    print("\nEjecutando: test_sobel...")
    img, _ = cargar_imagen_test()
    if img is None: return

    sx, sy = filtro_sobel(img)
    
    # Verificamos que devuelva dos imágenes y que sean de un solo canal (escala de grises)
    if sx is not None and sy is not None and len(sx.shape) == 2:
        print("[PASÓ] Filtros Sobel X e Y generados en escala de grises.")
    else:
        print("[FALLÓ] Error en el formato de salida de Sobel.")

def test_canny():
    print("\nEjecutando: test_canny...")
    img, _ = cargar_imagen_test()
    if img is None: return

    bordes = detector_canny(img)
    
    if bordes is not None and len(bordes.shape) == 2:
        print("[PASÓ] Detector Canny ejecutado exitosamente.")
    else:
        print("[FALLÓ] Error en el detector Canny.")

def test_laplaciano():
    print("\nEjecutando: test_laplaciano...")
    img, _ = cargar_imagen_test()
    if img is None: return

    lap = filtro_laplaciano(img)
    
    if lap is not None and len(lap.shape) == 2:
        print("[PASÓ] Filtro Laplaciano aplicado (bordes resaltados).")
    else:
        print("[FALLÓ] Error en el filtro Laplaciano.")

if __name__ == "__main__":
    print("--- INICIANDO VALIDACIÓN DE FILTERS.PY ---")
    test_convolucion_generica()
    test_sobel()
    test_canny()
    test_laplaciano()
    print("\n--- PRUEBAS FINALIZADAS ---")