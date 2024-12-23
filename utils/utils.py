import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os

def openRGB(path):
    assert os.path.exists(path), f"Image path doesn't exist. {path}"
    return mpimg.imread(path)

def showRGB(imgarray):
    plt.imshow(imgarray)
    # plt.show() 

def conv2d(img, filter):
    pass


def FFT(x):
    N = len(x)

    if N == 1:
        return x

    even = x[0::2]
    odd  = x[1::2]

    r_even = FFT(even)
    r_odd  = FFT(odd)

    # second half of the factors are negative of first values
    factor = np.exp(-2j*np.pi*np.arange(N)/N)

    return np.concatenate((r_even + factor[:int(N/2)]*r_odd,
                        r_even + factor[int(N/2):]*r_odd))

def image_FFT(image):
    fft_image = np.array([FFT(row) for row in image])
    for i in range(len(fft_image[0])):
        fft_image[::,i] = FFT(fft_image[::,i])

    return fft_image


def inverse_image_FFT(fft_image):
    height = len(fft_image)
    width = len(fft_image[0])
    working_image = np.conj(np.transpose(fft_image))
    working_image = np.transpose(image_FFT(working_image))/(height*width)

    return working_image

def conv2D(image_array, kernel, pad=True):
    o_height, o_width = image_array.shape
    convoluted_image = np.zeros((o_height, o_width))
    kernel_len = len(kernel)
    pad_amount = int(len(kernel)/2)

    # flip the kernel before convolution
    kernel = np.flip(kernel)
    if pad == True:
        image_array = np.pad(image_array, pad_amount)

    # print(image_array)
    for i in range(o_height):
        for j in range(o_width):
            convoluted_image[i][j] = np.sum(image_array[i:i+kernel_len,j:j+kernel_len]*kernel)

    return convoluted_image

class filters:
    # type = ["mean", "gausian"]
    def generateKernel(kernel_type='mean', kernel_size = 3):
        if kernel_type == 'mean':
            return np.ones((kernel_size, kernel_size))

        pass

    def Gaussian(self, x,y, variance):
        return np.exp((x**2 + y**2)/(-2*variance))/(2*np.pi*variance)

    def Gaussian_kernel(self, kernel_size, sigma):
        kernel = np.zeros((kernel_size, kernel_size))
        center_offset = kernel_size//2
        for i in range(kernel_size):
            for j in range(kernel_size):
                kernel[i - center_offset][j-center_offset] = self.Gaussian(i,j, sigma**2)

        return kernel

    