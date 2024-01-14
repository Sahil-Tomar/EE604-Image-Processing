import cv2
import matplotlib.pyplot as plt
import numpy as np


# Usage
def solution(image_path):
    """
        1. performs a mean-shift clustering on the given image to segment different sections of the image
        2. converts to YCrCb color format as the information about lava is contained in the color (HSV was not that sensitive to change in color
        3. uses K-means with K=2 to separate foreground from background
        4. finally, uses Otsu's thresholding to actually seperate the two segments of the image (and to ultimately create the final image)
        5. The image has is grayscale and has only one channel with 0 or 255 values, convert it into [0,0,0] and [255,255,255]
    """

    image = cv2.imread(image_path)
    '''
    The pixel values of output should be 0 and 255 and not 0 and 1
    '''

    # mean-shift algorithm
    mean_shift_segmentation = cv2.pyrMeanShiftFiltering(image, 30, 100)

    # convert to YCbCr
    cr_value = cv2.cvtColor(mean_shift_segmentation, cv2.COLOR_BGR2YCrCb)[:, :, 1]

    # Apply K-means on the Cr component of the image
    flat_image = cr_value.reshape(-1)
    flat_image = np.float32(flat_image)

    # define criteria, number of clusters(K) and apply kmeans()
    criteria = (cv2.TERM_CRITERIA_EPS, 10, 1.0)
    k = 2

    ret, label, center = cv2.kmeans(flat_image, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # Now convert back into uint8, and make original image
    center = np.uint8(center)
    result = center[label.flatten()]

    reshaped_result = result.reshape(cr_value.shape)

    # Otsu's Thresholding
    _, thresh_image = cv2.threshold(reshaped_result, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Make this one channel image to 3 channel image
    final_image = np.stack((thresh_image, thresh_image, thresh_image), axis=-1)

    return final_image
