import cv2 
import numpy as np

# monta a matriz do kernel media
kernel = np.ones((3,3), np.float32)/9

print(kernel)

jetplaneImg = cv2.imread('./imagens_com_ruido/jetplane.png', cv2.IMREAD_GRAYSCALE)
lenaImg = cv2.imread('./imagens_com_ruido/lena.png', cv2.IMREAD_GRAYSCALE)
beeImg = cv2.imread('./imagens_com_ruido/bee.png', cv2.IMREAD_GRAYSCALE)

def add_media(img):
    # aplica um filtro linear arbitrário
    return cv2.filter2D(img, -1, kernel)

cv2.imwrite('imagens_resultados/imagens_com_ruido_removido_media/jetplane.png', add_media(jetplaneImg))
cv2.imwrite('imagens_resultados/imagens_com_ruido_removido_media/lena.png', add_media(lenaImg))
cv2.imwrite('imagens_resultados/imagens_com_ruido_removido_media/bee.png', add_media(beeImg))
