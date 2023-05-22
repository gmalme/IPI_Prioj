import cv2
import numpy as np

# Carrega a imagem
image = cv2.imread('input/car.png')

# Define o valor do parâmetro de gama
gamma = 1.5

# Cria a tabela de pesquisa (lookup table) para a correção de gama
gamma_table = np.array([((i/255.0) ** (1/gamma)) * 255 for i in np.arange(0, 256)]).astype("uint8")

# Aplica a correção de gama na imagem usando a tabela de pesquisa
corrected_image = cv2.LUT(image, gamma_table)

# Mostra a imagem original e a imagem corrigida
cv2.imshow('Imagem Original', image)
cv2.imshow('Imagem Corrigida', corrected_image)
cv2.waitKey(0)
cv2.destroyAllWindows()