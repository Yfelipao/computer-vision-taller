"""
cvtools: Biblioteca personalizada para el procesamiento de imágenes y visión por computadora.
"""

# Importación de funciones del módulo CAMERA
from .camera import (
    radial_transform_normalized,
    focal_length_transform
)

# Importación de funciones del módulo COLOR
from .color import (
    convertir_a_hsv,
    graficar_histograma,
    cuantizacion_simple,
    reduccion_peso_imagen
)

# Importación de funciones del módulo FILTERS
from .filters import (
    aplicar_convolucion,
    filtro_sobel,
    detector_canny,
    filtro_laplaciano
)

# Definición de la lista de funciones disponibles para exportación directa
__all__ = [
    'radial_transform_normalized',
    'focal_length_transform',
    'convertir_a_hsv',
    'graficar_histograma',
    'cuantizacion_simple',
    'reduccion_peso_imagen',
    'aplicar_convolucion',
    'filtro_sobel',
    'detector_canny',
    'filtro_laplaciano'
]