import cv2 
import numpy as np

jetplaneImg = cv2.imread('./imagens_com_ruido/jetplane.png', cv2.IMREAD_GRAYSCALE)
lenaImg = cv2.imread('./imagens_com_ruido/lena.png', cv2.IMREAD_GRAYSCALE)
beeImg = cv2.imread('./imagens_com_ruido/bee.png', cv2.IMREAD_GRAYSCALE)


def add_mediana(img_noisy1):
    m, n = img_noisy1.shape 
    # aplica o padding
    padding = 2
    img_new1 = np.zeros([m + padding, n + padding]) 
    image_padded = np.zeros((img_noisy1.shape[0] + padding*2, img_noisy1.shape[1] + padding*2))
    image_padded[padding:-1 * padding, padding:-1 * padding] = img_noisy1

    # aplica o filtro mediana
    for i in range(1, padding + m - 1): 
        for j in range(1, padding + n - 1): 
            temp = [
                image_padded[i-1, j-1],   image_padded[i-1, j],   image_padded[i-1, j + 1], 
                image_padded[i, j-1],     image_padded[i, j],     image_padded[i, j + 1], 
                image_padded[i + 1, j-1], image_padded[i + 1, j], image_padded[i + 1, j + 1]
            ]
            temp = sorted(temp) 
            img_new1[i, j]= temp[4]
    return img_new1.astype(np.uint8)

cv2.imwrite('imagens_com_ruido_removido_mediana/jetplane.png', add_mediana(jetplaneImg))
cv2.imwrite('imagens_com_ruido_removido_mediana/lena.png', add_mediana(lenaImg))
cv2.imwrite('imagens_com_ruido_removido_mediana/bee.png', add_mediana(beeImg))
