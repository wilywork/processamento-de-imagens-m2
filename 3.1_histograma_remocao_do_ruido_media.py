import cv2
from matplotlib import pyplot

jetplaneImg = cv2.imread('./imagens_com_ruido_removido_media/jetplane.png', cv2.IMREAD_GRAYSCALE)
lenaImg = cv2.imread('./imagens_com_ruido_removido_media/lena.png', cv2.IMREAD_GRAYSCALE)
beeImg = cv2.imread('./imagens_com_ruido_removido_media/bee.png', cv2.IMREAD_GRAYSCALE)

pyplot.hist(jetplaneImg.ravel(), 256, [0,256])
pyplot.show()

pyplot.hist(lenaImg.ravel(), 256, [0,256])
pyplot.show()

pyplot.hist(beeImg.ravel(), 256, [0,256])
pyplot.show()
