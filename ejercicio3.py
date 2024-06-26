# -*- coding: utf-8 -*-
"""Ejercicio3.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1uLwpmkU5dueiumkG8dRMz68ZXJbB2iWp
"""

from google.colab import files
import cv2
import numpy as np
from matplotlib import pyplot as plt
uploaded = files.upload()
if len(uploaded) != 2:
    print("Por favor sube exactamente dos imágenes.")
image_files = list(uploaded.keys())
imagen1 = cv2.imread(image_files[0])
imagen2 = cv2.imread(image_files[1])
if imagen1 is None:
    print(f"Error al cargar {image_files[0]}")
if imagen2 is None:
    print(f"Error al cargar {image_files[1]}")
if imagen1.shape != imagen2.shape:
    print("Las imágenes deben tener el mismo tamaño.")
    exit()
image_sum = cv2.add(imagen1, imagen2)
image_diff = cv2.subtract(imagen1, imagen2)
titles = ['Imagen 1', 'Imagen 2', 'Suma', 'Resta']
images = [imagen1, imagen2, image_sum, image_diff]
for i in range(4):
    plt.subplot(2, 2, i + 1)
    plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()