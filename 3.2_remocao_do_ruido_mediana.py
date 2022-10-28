import cv2 
import numpy as np

jetplaneImg = cv2.imread('./imagens_com_ruido/jetplane.png', cv2.IMREAD_GRAYSCALE)
lenaImg = cv2.imread('./imagens_com_ruido/lena.png', cv2.IMREAD_GRAYSCALE)
beeImg = cv2.imread('./imagens_com_ruido/bee.png', cv2.IMREAD_GRAYSCALE)


def add_mediana(imagem_entrada):
    m, n = imagem_entrada.shape 
    # aplica o padding
    padding = 2
    img_new1 = np.zeros([m + padding, n + padding]) 
    imagem_com_borda = np.zeros((imagem_entrada.shape[0] + padding*2, imagem_entrada.shape[1] + padding*2))
    imagem_com_borda[padding:-1 * padding, padding:-1 * padding] = imagem_entrada

    # aplica o filtro mediana
    for i in range(1, padding + m - 1): 
        for j in range(1, padding + n - 1): 
            temp = [
                imagem_com_borda[i-1, j-1],   imagem_com_borda[i-1, j],   imagem_com_borda[i-1, j + 1], 
                imagem_com_borda[i, j-1],     imagem_com_borda[i, j],     imagem_com_borda[i, j + 1], 
                imagem_com_borda[i + 1, j-1], imagem_com_borda[i + 1, j], imagem_com_borda[i + 1, j + 1]
            ]
            temp = sorted(temp) 
            img_new1[i, j]= temp[4]

    #normaliza a imagem
    return img_new1.astype(np.uint8)

cv2.imwrite('imagens_resultados/imagens_com_ruido_removido_mediana/jetplane.png', add_mediana(jetplaneImg))
cv2.imwrite('imagens_resultados/imagens_com_ruido_removido_mediana/lena.png', add_mediana(lenaImg))
cv2.imwrite('imagens_resultados/imagens_com_ruido_removido_mediana/bee.png', add_mediana(beeImg))
