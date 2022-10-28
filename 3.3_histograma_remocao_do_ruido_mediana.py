import cv2
from matplotlib import pyplot

jetplaneImg = cv2.imread('./imagens_resultados/imagens_com_ruido_removido_mediana/jetplane.png', cv2.IMREAD_GRAYSCALE)
lenaImg = cv2.imread('./imagens_resultados/imagens_com_ruido_removido_mediana/lena.png', cv2.IMREAD_GRAYSCALE)
beeImg = cv2.imread('./imagens_resultados/imagens_com_ruido_removido_mediana/bee.png', cv2.IMREAD_GRAYSCALE)

pyplot.hist(jetplaneImg.ravel(), 256, [0,256])
pyplot.show()

pyplot.hist(lenaImg.ravel(), 256, [0,256])
pyplot.show()

pyplot.hist(beeImg.ravel(), 256, [0,256])
pyplot.show()
