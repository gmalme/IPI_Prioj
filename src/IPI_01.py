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

def verifica_row(matriz):
    result = []
    for row in range(len(matriz)):
        if(all(elemento == 0 for elemento in matriz[row])):
            result.append(row)

    return result

def verifica_coll(matriz):
    result = []
    for row in range(len(matriz)):
        if( np.all(matriz[:, row] == 0) ):
            result.append(row)

    return result

def odd_fill(matriz, white_lines):
    for row in white_lines:
        linha = np.copy(matriz[row-1])
        matriz[row] = linha
                    
    return matriz

def pair_fill(matriz, white_coll):
    for row in range(len(matriz)):
        for item in white_coll:
            matriz[row][item] = matriz[row][item-1]
 
    return matriz

def tam2(image):
    fill_image = fill(image)

    for x in range(fill_image.shape[2]):
        white_lines = verifica_row(fill_image[:,:,x])
        fill_image[:,:,x] = odd_fill(fill_image[:,:,x], white_lines)
        white_coll = verifica_coll(fill_image[:,:,x])
        fill_image[:,:,x] = pair_fill(fill_image[:,:,x], white_coll)

    return fill_image


#______________________MAIN______________________
image = cv2.imread(r'../input/fruit1.jpg')
#image = np.ones((4, 4, 3), dtype=np.uint8)

#print(image,"____________AQUI____________\n")
image = tam2(image)
cv2.imwrite('../output/fruit1.jpg',image)


for size in range(image.shape[2]):
    print(image[:,:,size],'\n')