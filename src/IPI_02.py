import cv2 
import numpy as np
import matplotlib.pyplot as plt

# img = cv2.imread('../input/car.png', 0)
# equ = cv2.equalizeHist(img) 
# res = np.hstack((img, equ)) 
# cv2.imshow('',res) 
  
# cv2.waitKey(0) 
# cv2.destroyAllWindows()

def equalize(image):
    # # recebe o caminho da imagem
    # image = cv2.imread(path,0)
    
    # Calcular o histograma
    histogram, bins = np.histogram(image.flatten(), bins=256, range=[0, 256])
    # Calcular a CDF
    cdf = histogram.cumsum()
    # Normalizar a CDF
    cdf_normalized = cdf / cdf.max()
    # Aplicar a equalização de histograma
    equalized_image = np.interp(image.flatten(), bins[:-1], cdf_normalized * 255).reshape(image.shape).astype(np.uint8)
    return equalized_image

#__________main__________
image = cv2.imread(r'../input/car.png',0)
equalized_image = equalize(image)

# cv2.imshow('teste',equalized_image)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # Plotar o histograma or CDF
# plt.plot(histogram)
# plt.xlabel('Intensidade')
# plt.ylabel('Frequência')
# plt.show()

# Exibir a imagem original e a imagem equalizada
plt.subplot(1, 2, 1)
plt.imshow(image, cmap='gray')
plt.title('Imagem original')
plt.subplot(1, 2, 2)
plt.imshow(equalized_image, cmap='gray')
plt.title('Imagem equalizada')
plt.show()