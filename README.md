# taller_computer_vision
Taller 1 de visión por computadora. 

Este taller consiste en el desarrollo de un conjunto de herramientas básicas para el manejo, análisis y transformación de imágenes digitales utilizando Python y OpenCV.

## Estructura del Proyecto
El proyecto está organizado como un paquete de Python para facilitar la reutilización de sus funciones:

- **data/**: Contiene las imágenes de prueba (ej. `lenna.jpg`).
- **cvtools/**: Paquete principal que contiene la lógica del taller.
- **main.py**: Script principal para ejecutar demostraciones de todas las funciones.
- **requirements.txt**: Lista de dependencias necesarias.

---

## Módulos Detallados

### 1. camera.py
Este módulo contiene funciones para modelar fenómenos físicos y geométricos de la cámara:
* **Distorsión Radial**: La función `radial_transform_normalized` permite aplicar distorsión (efecto barril/cojín) utilizando coordenadas normalizadas y coeficientes $k_1, k_2$.
* **Longitud Focal**: La función `focal_length_transform` simula cambios en el zoom mediante el ajuste de la matriz intrínseca y transformaciones de perspectiva (homografías).

### 2. color.py
Módulo dedicado al tratamiento del color y optimización de archivos:
* **Espacios de Color**: Incluye la conversión de BGR a HSV (útil para segmentación por tono y saturación).
* **Histogramas**: La función `graficar_histograma` genera una visualización de la distribución de intensidades para los canales Blue, Green y Red.
* **Cuantización**: 
    * `cuantizacion_simple`: Reduce los colores a niveles discretos por canal.
    * `reduccion_peso_imagen`: Utiliza paletas de colores adaptativas (vía PIL) para disminuir el tamaño del archivo en disco manteniendo la calidad visual.

### 3. filters.py
Contiene herramientas para el filtrado espacial y detección de características:
* **Convolución**: Función `aplicar_convolucion` para operar con kernels personalizados sobre la imagen.
* **Filtros de Bordes**:
    * **Sobel**: Detecta cambios de intensidad en ejes X e Y (derivadas de primer orden).
    * **Canny**: Detector de bordes avanzado para obtener contornos nítidos.
    * **Laplaciano**: Resalta bordes en todas las direcciones mediante la segunda derivada.

---

## Instalación y Uso

1. **Clonar el repositorio o descargar los archivos.**
2. **Instalar dependencias**:
   ```bash
   pip install -r requirements.txt
