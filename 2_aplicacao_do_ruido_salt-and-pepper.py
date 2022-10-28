import random
import cv2

jetplaneImg = cv2.imread('./imagens_originais/jetplane.png', cv2.IMREAD_GRAYSCALE)
lenaImg = cv2.imread('./imagens_originais/lena.png', cv2.IMREAD_GRAYSCALE)
beeImg = cv2.imread('./imagens_originais/bee.png', cv2.IMREAD_GRAYSCALE)


def add_salt_and_pepper(img):
    # Getting the dimensions of the image
    row , col = img.shape
    # Randomly pick some pixels in the
    # image for coloring them white
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
        # Color that pixel to white
        img[y_coord][x_coord] = 255
    # Randomly pick some pixels in
    # the image for coloring them black
    # Pick a random number between 300 and 10000
    number_of_pixels = random.randint(300 , 10000)
    for i in range(number_of_pixels):
        # Pick a random y coordinate
        y_coord=random.randint(0, row - 1)
        # Pick a random x coordinate
        x_coord=random.randint(0, col - 1)
        # Color that pixel to black
        img[y_coord][x_coord] = 0
    return img


cv2.imwrite('imagens_com_ruido/jetplane.png', add_salt_and_pepper(jetplaneImg))
cv2.imwrite('imagens_com_ruido/lena.png', add_salt_and_pepper(lenaImg))
cv2.imwrite('imagens_com_ruido/bee.png', add_salt_and_pepper(beeImg))

