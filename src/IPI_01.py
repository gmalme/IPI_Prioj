import cv2
import numpy as np
import matplotlib.pyplot as plt

def Tam2(imagem, tam):
    # Verificar se a imagem foi carregada corretamente
    if imagem is not None:
        # Converter a imagem para uma matriz NumPy
        matriz_imagem = np.array(imagem)

        # Exibir a matriz resultante
        print(matriz_imagem)
    else:
        print("Falha ao carregar a imagem.")

#______________________MAIN______________________
image = cv2.imread(r'../input/fruit1.jpg',1)
cv2.imshow("original", image)
cv2.waitKey(0)