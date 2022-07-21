import numpy as np
import matplotlib
import matplotlib.pyplot as plt

def pixel_to_number(pix, shape=(768,1366)):
    """
    0:768 - -1:1
    0:1366 - -2:1
    """
    x = 2*pix[0]/shape[0] - 1
    y = 3*pix[1]/shape[1] - 2
    return y,x

def mandelbrot_if_bounded(number : list):
    """
    number : (b, a) where number = a + i*b

    if after 1000 iteration number is less than 1000, it's ok

    z(i) = z(i-1)^2 + number
    """

    z = list(number)


    try:
        for i in range(100):

            z[0], z[1] = z[0]**2 - z[1]**2 + number[0], 2*z[0]*z[1] + number[1]

        if (z[0]**2 + z[1]**2)**0.5 >= 100*(number[0]**2 + number[1]**2)**0.5:
            return 0
        return 255
    except OverflowError:
        return 0

shape = (768,1366) #(360,640)

image = np.zeros(shape)

for a in range(image.shape[0]):
    for b in range(image.shape[1]):
        image[a,b] = mandelbrot_if_bounded(pixel_to_number((a,b), shape=shape))
    if a%10 == 0:
        print(a)

matplotlib.image.imsave('mandelbrot.png', image)

plt.imshow(image, interpolation='nearest', cmap='gray')

plt.show()