import random
import cv2

jetplaneImg = cv2.imread('./imagens_originais/jetplane.png', cv2.IMREAD_GRAYSCALE)
lenaImg = cv2.imread('./imagens_originais/lena.png', cv2.IMREAD_GRAYSCALE)
beeImg = cv2.imread('./imagens_originais/bee.png', cv2.IMREAD_GRAYSCALE)

def add_salt_and_pepper(img):
    linha , coluna = img.shape

    numero_aleatorio = random.randint(300, 10000)
    for i in range(numero_aleatorio):
        coordy=random.randint(0, linha - 1)
        coordx=random.randint(0, coluna - 1)
        img[coordy][coordx] = 255

    numero_aleatorio = random.randint(300 , 10000)
    for i in range(numero_aleatorio):
        coordy=random.randint(0, linha - 1)
        coordx=random.randint(0, coluna - 1)
        img[coordy][coordx] = 0
    return img


cv2.imwrite('imagens_resultados/imagens_com_ruido/jetplane.png', add_salt_and_pepper(jetplaneImg))
cv2.imwrite('imagens_resultados/imagens_com_ruido/lena.png', add_salt_and_pepper(lenaImg))
cv2.imwrite('imagens_resultados/imagens_com_ruido/bee.png', add_salt_and_pepper(beeImg))

