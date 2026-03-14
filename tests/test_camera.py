import cv2
import numpy as np
import os
import sys

# Añadimos la raíz al path para poder importar desde cvtools
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cvtools.camera import radial_transform_normalized, focal_length_transform

def cargar_imagen_test():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.join(BASE_DIR, "..", "data", "lenna.jpg")
    
    img = cv2.imread(ruta_imagen)
    return img, ruta_imagen

def test_radial_transform():
    print("Ejecutando: test_radial_transform con imagen real...")
    img, ruta = cargar_imagen_test()
    
    if img is None:
        print(f"[ERROR] No se pudo cargar la imagen para el test en: {ruta}")
        return

    # Probar la función del módulo
    # k1 y k2 positivos crean distorsión de barril
    resultado = radial_transform_normalized(img, k1=0.2, k2=0.1)
    
    if resultado is not None and resultado.shape == img.shape:
        print(f"[PASÓ] Transformación radial exitosa sobre {ruta}")
    else:
        print("[FALLÓ] La transformación radial alteró las dimensiones o falló.")

def test_focal_transform():
    print("\nEjecutando: test_focal_transform con imagen real...")
    img, ruta = cargar_imagen_test()
    
    if img is None:
        print(f"[ERROR] No se pudo cargar la imagen en: {ruta}")
        return

    resultado = focal_length_transform(img, f_scale=1.2)
    
    if resultado is not None and resultado.shape == img.shape:
        print(f"[PASÓ] Cambio de focal exitoso sobre {ruta}")
    else:
        print("[FALLÓ] El cambio de perspectiva falló.")

if __name__ == "__main__":
    print("--- INICIANDO VALIDACIÓN DE CAMERA.PY ---")
    test_radial_transform()
    test_focal_transform()
    print("\n--- PRUEBAS FINALIZADAS ---")