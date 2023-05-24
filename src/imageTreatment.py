import cv2
import numpy as np
import matplotlib.pyplot as plt

class imageTreatment:
    def __init__(self) -> None:
        pass

    def fill(self, image):
        try:
            matriz_imagem = np.array(image)
            matriz_final = np.zeros((matriz_imagem.shape[0]*2,matriz_imagem.shape[1]*2,matriz_imagem.shape[2]))
            matriz_final[::2, ::2, :] = matriz_imagem
                        
            return matriz_final
        except Exception as erro:
            print("Ocorreu um erro:", erro)

    def verifica_row(self, matriz):
        result = []
        for row in range(len(matriz)):
            if(all(elemento == 0 for elemento in matriz[row])):
                result.append(row)

        return result

    def verifica_coll(self, matriz):
        result = []
        for row in range(len(matriz)):
            if( np.all(matriz[:, row] == 0) ):
                result.append(row)

        return result

    def odd_fill(self, matriz, white_lines):
        for row in white_lines:
            linha = np.copy(matriz[row-1])
            matriz[row] = linha
                        
        return matriz

    def pair_fill(self, matriz, white_coll):
        for row in range(len(matriz)):
            for item in white_coll:
                matriz[row][item] = matriz[row][item-1]
    
        return matriz

    def m_odd_fill(self, matriz, white_lines):
        for row in white_lines:
            linha = np.copy(matriz[row-1])
            linha_2 = np.copy(matriz[row-1])
            if(linha_2 is not None):
                linha = (linha + linha_2)/2
            matriz[row] = linha
                        
        return matriz

    def m_pair_fill(self, matriz, white_coll):
        for row in range(len(matriz)):
            for item in white_coll:
                cell = matriz[row][item-1]

                if(item+1 < len(matriz)):
                    cell_2 = matriz[row][item+1]
                    cell = (cell + cell_2)/2
                
                matriz[row][item] = cell
    
        return matriz

    def tam2(self, image):
        fill_image = self.fill(image)

        for x in range(fill_image.shape[2]):
            white_lines = self.verifica_row(fill_image[:,:,x])
            fill_image[:,:,x] = self.odd_fill(fill_image[:,:,x], white_lines)
            white_coll = self.verifica_coll(fill_image[:,:,x])
            fill_image[:,:,x] = self.pair_fill(fill_image[:,:,x], white_coll)

        return fill_image

    def tamm(self, image):
        fill_image = self.fill(image)

        for x in range(fill_image.shape[2]):
            white_lines = self.verifica_row(fill_image[:,:,x])
            fill_image[:,:,x] = self.m_odd_fill(fill_image[:,:,x], white_lines)
            white_coll = self.verifica_coll(fill_image[:,:,x])
            fill_image[:,:,x] = self.m_pair_fill(fill_image[:,:,x], white_coll)

        return fill_image

    def fill_matriz(self, matriz, image_b):
        for z in range(image_b.shape[2]):
            for x in range(image_b.shape[1]):
                for y in range(image_b.shape[0]):
                    matriz[((x+1)*2)-1, ((y+1)*2)-1, z] = image_b[x,y,z]
        
        return matriz

    def med_matriz(self, matriz):
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
        
    def merge_image(self, image_a, image_b):
        fill_image = self.fill(image_a)
        self.fill_matriz(fill_image, image_b)
        self.med_matriz(fill_image)

        return fill_image
