import cv2 
import numpy as np 

img_noisy1 = cv2.imread('./imagens_com_ruido/jetplane.png', 0)
kernel = np.array([[-1, -1, -1], [-1, -1, -1], [-1, -1, -1]])

def convolve2D(image, kernel, padding=0, strides=1):
    # Cross Correlation
    kernel = np.flipud(np.fliplr(kernel))

    # Gather Shapes of Kernel + Image + Padding
    xKernShape = kernel.shape[0]
    yKernShape = kernel.shape[1]
    xImgShape = image.shape[0]
    yImgShape = image.shape[1]

    # Shape of Output Convolution
    xOutput = int(((xImgShape - xKernShape + 2 * padding) / strides) + 1)
    yOutput = int(((yImgShape - yKernShape + 2 * padding) / strides) + 1)
    output = np.zeros((xOutput, yOutput))

    # Apply Equal Padding to All Sides
    if padding != 0:
        image_padded = np.zeros((image.shape[0] + padding*2, image.shape[1] + padding*2))
        image_padded[int(padding):int(-1 * padding), int(padding):int(-1 * padding)] = image
        print(image_padded)
    else:
        image_padded = image

    # Iterate through image
    for y in range(image.shape[1]):
        # Exit Convolution
        if y > image.shape[1] - yKernShape:
            break
        # Only Convolve if y has gone down by the specified Strides
        if y % strides == 0:
            for x in range(image.shape[0]):
                # Go to next row once kernel is out of bounds
                if x > image.shape[0] - xKernShape:
                    break
                try:
                    # Only Convolve if x has moved by the specified Strides
                    if x % strides == 0:
                        output[x, y] = (kernel * image_padded[x: x + xKernShape, y: y + yKernShape]).sum()
                except:
                    break

    return output

if __name__ == '__main__':
    # Grayscale Image
    # image = processImage('Image.jpeg')
    # Edge Detection Kernel
    kernel = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    # Convolve and Save Output
    output = convolve2D(img_noisy1, kernel, padding=2)
    cv2.imshow('2DConvolved.jpg', output)
    cv2.waitKey(0)
    cv2.destroyAllWindows()