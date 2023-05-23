import cv2 
import numpy as np
import matplotlib.pyplot as plt

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
    return equalized_image, histogram, cdf_normalized

def gamma(image,gamma):
    gamma_table = np.array([((i/255.0) ** (1/gamma)) * 255 for i in np.arange(0, 256)]).astype("uint8")
    corrected_image = cv2.LUT(image, gamma_table)
    return corrected_image

def printIm(tag, image):
    # Plotar imagem equalizada com imshow ( equalização )
    cv2.imshow(tag, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def print2Im(old_image, new_image, arg_a ='Imagem Original', arg_b ='Imagem Corrigida'):
    # Mostra a imagem original e a imagem corrigida ( gama )
    cv2.imshow(arg_a, old_image)
    cv2.imshow(arg_b, new_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def printPl(image, arg_a ='Intensidade', arg_b ='Frequência'):
    # Plotar  imagem com plt ( histograma || CDF )
    plt.plot(image)
    plt.xlabel(arg_a)
    plt.ylabel(arg_b)
    plt.show()

def print2Pl(old_image, new_image, arg_a ='Imagem original', arg_b ='Imagem equalizada'):
    # Exibir a imagem original e a imagem equalizada ( equalização )
    plt.subplot(1, 2, 1)
    plt.imshow(old_image, cmap='gray')
    plt.title(arg_a)
    plt.subplot(1, 2, 2)
    plt.imshow(new_image, cmap='gray')
    plt.title(arg_a)
    plt.show()

# __________main__________
image = cv2.imread(r'../input/car.png',0)
equalized_image, histogram, cdf = equalize(image)
corrected_image = gamma(image, 0.6)

# printa imagem equalizada
# printIm('imagem equalizada', equalized_image) 
# print2Pl(image, equalized_image)

# # print histograma e cdf
# printPl(cdf)

# print gama
# print2Im(image, corrected_image)





