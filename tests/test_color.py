import cv2
import numpy as np
import os
import sys

# Asegurar que Python encuentre el módulo cvtools
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from cvtools.color import convertir_a_hsv, graficar_histograma, cuantizacion_simple, reduccion_peso_imagen

def cargar_imagen_test():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    ruta_imagen = os.path.normpath(os.path.join(BASE_DIR, "..", "data", "lenna.jpg"))
    img = cv2.imread(ruta_imagen)
    return img, ruta_imagen

def test_hsv_conversion():
    print("Ejecutando: test_hsv_conversion...")
    img, _ = cargar_imagen_test()
    if img is None: return
    
    hsv = convertir_a_hsv(img)
    if hsv is not None and hsv.shape == img.shape:
        print("[PASÓ] Conversión a HSV exitosa.")
    else:
        print("[FALLÓ] Error en la conversión a HSV.")

def test_cuantizacion_y_peso():
    print("\nEjecutando: test_cuantizacion_y_peso...")
    img, _ = cargar_imagen_test()
    if img is None: return

    k = 4
    img_c = cuantizacion_simple(img, k)
    
    ruta_tmp = "test_output.png"
    img_p, peso_kb = reduccion_peso_imagen(img, k, ruta_salida=ruta_tmp)
    
    if img_c.shape == img.shape and peso_kb > 0:
        print(f"[PASÓ] Cuantización realizada. Peso resultante: {peso_kb:.2f} KB")
        if os.path.exists(ruta_tmp):
            os.remove(ruta_tmp) # Limpiar archivo de prueba
    else:
        print("[FALLÓ] Error en la reducción de colores o peso.")

def test_histograma_visual():
    print("\nEjecutando: test_histograma_visual (requiere cerrar ventana)...")
    img, _ = cargar_imagen_test()
    if img is None: return
    
    print("Generando gráfico...")
    graficar_histograma(img)
    print("[PASÓ] Función de histograma ejecutada.")

if __name__ == "__main__":
    print("--- INICIANDO VALIDACIÓN DE COLOR.PY ---")
    test_hsv_conversion()
    test_cuantizacion_y_peso()
    test_histograma_visual()
    print("\n--- PRUEBAS FINALIZADAS ---")