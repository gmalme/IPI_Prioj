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

def m_odd_fill(matriz, white_lines):
    for row in white_lines:
        linha = np.copy(matriz[row-1])
        linha_2 = np.copy(matriz[row-1])
        if(linha_2 is not None):
            linha = (linha + linha_2)/2
        matriz[row] = linha
                    
    return matriz

def m_pair_fill(matriz, white_coll):
    for row in range(len(matriz)):
        for item in white_coll:
            cell = matriz[row][item-1]

            if(item+1 < len(matriz)):
               cell_2 = matriz[row][item+1]
               cell = (cell + cell_2)/2
               
            matriz[row][item] = cell
 
    return matriz

def tam2(image):
    fill_image = fill(image)

    for x in range(fill_image.shape[2]):
        white_lines = verifica_row(fill_image[:,:,x])
        fill_image[:,:,x] = odd_fill(fill_image[:,:,x], white_lines)
        white_coll = verifica_coll(fill_image[:,:,x])
        fill_image[:,:,x] = pair_fill(fill_image[:,:,x], white_coll)

    return fill_image

def tamm(image):
    fill_image = fill(image)

    for x in range(fill_image.shape[2]):
        white_lines = verifica_row(fill_image[:,:,x])
        fill_image[:,:,x] = m_odd_fill(fill_image[:,:,x], white_lines)
        white_coll = verifica_coll(fill_image[:,:,x])
        fill_image[:,:,x] = m_pair_fill(fill_image[:,:,x], white_coll)

    return fill_image

def print2Pl(old_image, new_image, arg_a ='Imagem original', arg_b ='Imagem equalizada'):
    # Exibir a imagem original e a imagem equalizada ( equalização )
    plt.subplot(1, 2, 1)
    plt.imshow(old_image, cmap='gray')
    plt.title(arg_a)
    plt.subplot(1, 2, 2)
    plt.imshow(new_image, cmap='gray')
    plt.title(arg_a)
    plt.show()

#______________________MAIN______________________
image = cv2.imread(r'../input/fruit1.jpg')

image_row = np.array(([3, 2, 3],[5,3,3]))
image = np.stack([image_row] * 2)
print(image)
input()

image = tamm(image)
#image = tam2(image)
cv2.imwrite('../output/fruit1.jpg',image)
#cv2.imwrite('../output/fruit2.jpg',image2)

#print2Pl(image,image2)

for size in range(image.shape[2]):
    print(image[:,:,size],'\n')