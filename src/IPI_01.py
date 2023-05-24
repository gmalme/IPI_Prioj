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

def fill_matriz(matriz, image_b):
    for z in range(image_b.shape[2]):
        for x in range(image_b.shape[1]):
            for y in range(image_b.shape[0]):
                matriz[((x+1)*2)-1, ((y+1)*2)-1, z] = image_b[x,y,z]
    
    return matriz

def med_matriz(matriz):
    for z in range(matriz.shape[2]):
        for x in range(matriz.shape[1]):
            for y in range(matriz.shape[0]):
                if( matriz[x,y,z] == 0 ):
                    result = 0
                    idx = 0

                    for cell in range(-1,1,2):
                        if( x+cell >= 0 and x+cell < matriz.shape[1]):
                            result += matriz[x+cell,y,z]
                            idx+=1
                        if( y+cell >= 0 and  y+cell < matriz.shape[0]):
                            result += matriz[x,y+cell,z]
                            idx+=1

                    matriz[x,y,z] = result/idx

    return matriz
    

def merge_image(image_a, image_b):
    fill_image = fill(image_a)
    fill_matriz(fill_image, image_b)
    med_matriz(fill_image)

    return fill_image

#______________________MAIN______________________
image = cv2.imread(r'../input/fruit1.jpg')
image_b = cv2.imread(r'../input/fruit2.jpg')

# image = np.ones((2, 2, 3), dtype=np.uint8)
# image_b = np.ones((2, 2, 3), dtype=np.uint8)
# image = np.stack([image_row] * 2)

#image = tamm(image)
#image = tam2(image)
#cv2.imwrite('../output/fruit3.jpg',image)
#cv2.imwrite('../output/fruit2.jpg',image2)

image = merge_image(image,image_b)
cv2.imwrite('../output/fruit3.jpg',image)

#print(image_b.shape)

for size in range(image.shape[2]):
    print(image[:,:,size],'\n')