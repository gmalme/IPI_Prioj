import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carrega a imagem
image = cv2.imread(r'../input/car.png',0)

# Define o valor do parâmetro de gama
gamma = 0.5

# Cria a tabela de pesquisa (lookup table) para a correção de gama
gamma_table = np.array([((i/255.0) ** (1/gamma)) * 255 for i in np.arange(0, 256)]).astype("uint8")

# Aplica a correção de gama na imagem usando a tabela de pesquisa
corrected_image = cv2.LUT(image, gamma_table)

# # Mostra a imagem original e a imagem corrigida
# cv2.imshow('Imagem Original', image)
# cv2.imshow('Imagem Corrigida', corrected_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# Calcular o histograma
histogram, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])

# Calcular a CDF
cdf = histogram.cumsum()

# Normalizar a CDF
cdf_normalized = cdf / cdf.max()

# # Plotar o histograma
# plt.plot(histogram)
# plt.xlabel('Intensidade')
# plt.ylabel('Frequência')
# plt.show()

# # Plotar a CDF
# plt.plot(cdf_normalized)
# plt.xlabel('Intensidade')
# plt.ylabel('CDF Normalizada')
# plt.show()

# Aplicar a equalização de histograma
equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized * 255).reshape(image.shape).astype(np.uint8)

# Exibir a imagem original e a imagem equalizada
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem original')
plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Imagem equalizada')
plt.show()