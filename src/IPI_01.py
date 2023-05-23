import cv2
import numpy as np
import matplotlib.pyplot as plt

def fill(image):
    try:
        matriz_imagem = np.array(image)
        matriz_final = np.zeros((matriz_imagem.shape[0]*2,matriz_imagem.shape[1]*2,matriz_imagem.shape[2]))
        matriz_final[::2, ::2, :] = matriz_imagem
                    
        return matriz_final
    except Exception as erro:
        print("Ocorreu um erro:", erro)

def tam2(image):
    fill_image = fill(image)
    
    return  fill_image


#______________________MAIN______________________
image = cv2.imread(r'../input/fruit1.jpg')
image = np.ones((2, 2, 3), dtype=np.uint8)
#image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

#print(image,"____________AQUI____________\n")
image = tam2(image)

for x in image[:,:,]:
    for y in x[:,]:
        print(y,end='')
    print('\n')
    

# print(image.shape)
# cv2.imshow("original", image)
# cv2.waitKey(0)
# cv2.imwrite("../output/fruit1.jpg", image)