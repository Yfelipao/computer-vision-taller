import cv2
import os
import numpy as np
import matplotlib.pyplot as plt
from cvtools import (
    radial_transform_normalized,
    focal_length_transform,
    convertir_a_hsv,
    cuantizacion_simple,
    reduccion_peso_imagen,
    aplicar_convolucion,
    filtro_sobel,
    detector_canny,
    filtro_laplaciano
)

def main():
    # --- 1. CONFIGURACIÓN Y CARGA ---
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_input = os.path.join(BASE_DIR, "data", "lenna.jpg")
    img = cv2.imread(ruta_input)

    if img is None:
        print("No se encontró la imagen de prueba.")
        return

    print("Iniciando procesamiento total...")

    # --- 2. MÓDULO CAMERA: Transformaciones Geométricas ---
    # Aplicamos distorsión radial (efecto barril) y luego un cambio de focal (zoom)
    img_distorsionada = radial_transform_normalized(img, k1=0.3, k2=0.1)
    img_geometria = focal_length_transform(img_distorsionada, f_scale=1.3)

    # --- 3. MÓDULO FILTERS: Extracción de Estructura ---
    # Usamos una convolución para suavizar antes de buscar bordes
    kernel_smooth = np.ones((3,3), np.float32) / 9
    img_suave = aplicar_convolucion(img_geometria, kernel_smooth)
    
    # Obtenemos diferentes tipos de bordes
    sobel_x, sobel_y = filtro_sobel(img_suave)
    bordes_canny = detector_canny(img_suave, 50, 150)
    bordes_laplace = filtro_laplaciano(img_suave)

    # --- 4. MÓDULO COLOR: Análisis y Optimización ---
    # Convertimos a HSV la imagen procesada
    img_hsv = convertir_a_hsv(img_geometria)
    
    # Cuantizamos colores para estilo artístico
    img_art = cuantizacion_simple(img_geometria, k=4)
    
    # Reducimos peso real y guardamos archivo optimizado
    ruta_out = os.path.join(BASE_DIR, "lenna_optimizada.png")
    img_final, peso_kb = reduccion_peso_imagen(img_geometria, k=16, ruta_salida=ruta_out)

    # --- 5. VISUALIZACIÓN DE RESULTADOS ---
    print(f"¡Procesamiento terminado! Peso del archivo optimizado: {peso_kb:.2f} KB")

    # Preparamos ventanas de comparación
    # Fila 1: Evolución Geométrica
    res1 = np.hstack((img, img_distorsionada, img_geometria))
    cv2.imshow('1. Geometria: Original -> Radial -> Focal Zoom', res1)

    # Fila 2: Análisis de Bordes (convertimos a BGR para poder juntar con hstack)
    canny_bgr = cv2.cvtColor(bordes_canny, cv2.COLOR_GRAY2BGR)
    laplace_bgr = cv2.cvtColor(bordes_laplace, cv2.COLOR_GRAY2BGR)
    res2 = np.hstack((img_geometria, canny_bgr, laplace_bgr))
    cv2.imshow('2. Filtros: Base -> Canny -> Laplaciano', res2)

    # Fila 3: Color y Salida
    res3 = np.hstack((img_hsv, img_art, img_final))
    cv2.imshow('3. Color: HSV -> Cuantizacion (4 niveles) -> Resultado Final', res3)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()