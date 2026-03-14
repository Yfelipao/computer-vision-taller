import cv2
import os
import numpy as np

def radial_transform_normalized(image, k1, k2):
    height, width = image.shape[:2]
    
    # 1. Definimos el centro y el factor de escala para normalizar
    center_x, center_y = width / 2, height / 2
    # Escalamos para que la distancia máxima al borde sea 1
    max_radius = np.sqrt(center_x**2 + center_y**2)

    # 2. Creamos malla de coordenadas
    x, y = np.meshgrid(np.arange(width), np.arange(height))

    # 3. NORMALIZACIÓN: Pasamos de coordenadas de imagen a un plano [-1, 1]
    # Restamos el centro y dividimos por el radio máximo
    x_norm = (x - center_x) / max_radius
    y_norm = (y - center_y) / max_radius

    # 4. Calculamos r^2 y r^4 en el espacio normalizado
    r_sq = x_norm**2 + y_norm**2
    r_quad = r_sq**2

    # 5. Aplicamos la distorsión radial
    # L(r) = 1 + k1*r^2 + k2*r^4
    distortion_factor = 1 + k1 * r_sq + k2 * r_quad
    
    # 6. DES-NORMALIZACIÓN: Volvemos al espacio de píxeles de la imagen
    new_x = (x_norm * distortion_factor) * max_radius + center_x
    new_y = (y_norm * distortion_factor) * max_radius + center_y

    # 7. INTERPOLACIÓN
    warped_image = cv2.remap(image, 
                             new_x.astype(np.float32), 
                             new_y.astype(np.float32), 
                             cv2.INTER_LINEAR)

    return warped_image

def focal_length_transform(image, f_scale):
    """
    Varía la longitud focal efectiva de la imagen.
    f_scale: Factor multiplicador (1.0 es original, >1.0 es zoom, <1.0 es gran angular)
    """
    height, width = image.shape[:2]
    
    # 1. Definimos la Matriz de la Cámara Intrínseca (K)
    # Suponemos una focal inicial basada en la dimensión mayor
    f_original = max(width, height) 
    center_x, center_y = width / 2, height / 2
    
    # Matriz Original
    K = np.array([
        [f_original, 0,          center_x],
        [0,          f_original, center_y],
        [0,          0,          1]
    ], dtype=np.float32)

    # 2. Definimos la Matriz con la nueva Longitud Focal (K_new)
    f_new = f_original * f_scale
    K_new = np.array([
        [f_new, 0,     center_x],
        [0,     f_new, center_y],
        [0,     0,     1]
    ], dtype=np.float32)

    # 3. Calculamos la transformación (Homografía) entre las dos cámaras
    # Como solo cambiamos f y no rotamos la cámara: H = K_new * inv(K)
    H = K_new @ np.linalg.inv(K)

    # 4. Aplicamos la transformación de perspectiva
    # Usamos warpPerspective para re-proyectar los puntos
    transformed_image = cv2.warpPerspective(image, H, (width, height))

    return transformed_image

'''
# --- PRUEBA DEL EFECTO ---
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ruta hacia la carpeta 'data' 
ruta_imagen = os.path.join(BASE_DIR, "..", "data", "lenna.jpg")

# Cargar la imagen
image = cv2.imread(ruta_imagen)

if image is not None:
    # f_scale < 1.0 : Aleja los puntos (más perspectiva, estilo ojo de pez ligero)
    # f_scale > 1.0 : Acerca los puntos (menos perspectiva, estilo teleobjetivo)
    wide_angle = focal_length_transform(image, f_scale=0.7)
    telephoto = focal_length_transform(image, f_scale=1.5)

    cv2.imshow('Gran Angular (f corta)', wide_angle)
    cv2.imshow('Original', image)
    cv2.imshow('Teleobjetivo (f larga)', telephoto)
    
    cv2.waitKey(0)
    cv2.destroyAllWindows()
'''