import cv2
import numpy as np


# Usage
def solution(image_path):
    image = cv2.imread(image_path)
    ######################################################################
    ######################################################################
    #####  WRITE YOUR CODE BELOW THIS LINE ###############################

    # LOGIC :
    # 1. Convert the image to hue
    # 2. Create a mask for orange color (pixel==255 if color == orange)
    # 3. Divide the image into the top half, the bottom half, the left half and the right half.
    # The half which contains more 1s i.e. more orange pixels will have the top orange part of the flag
    # 4. Once you get the orientation of the image, create the output image to be returned by using cv2's inbuilt circle and line function

    # try to get the orientation of the flag given, i.e., on which side of the image is the top orange located

    # Convert to hue
    hue = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)[:, :, 0]

    # Create a mask for orange color
    mask_for_orange_color = np.array(hue == 15)  # 15 is the hue for orange color in the given image
    m, n = mask_for_orange_color.shape

    # Get the number of orange pixels in all the halves
    top, bottom = np.sum(mask_for_orange_color[:m // 2, :]), np.sum(mask_for_orange_color[m // 2:, :])
    left, right = np.sum(mask_for_orange_color[:, :n // 2]), np.sum(mask_for_orange_color[:, n // 2:])

    # The half with maximum pixels is the top part
    orientation_indicator = np.argmax([top, bottom, left, right])

    if orientation_indicator == 0:
        orientation = 'top'
    elif orientation_indicator == 1:
        orientation = 'bottom'
    elif orientation_indicator == 2:
        orientation = 'left'
    elif orientation_indicator == 3:
        orientation = 'right'

    # initialise output image
    output_image = np.ones((600, 600, 3), dtype=np.uint8)

    # set some constants for colors
    orange = [51, 153, 255]
    white = [255, 255, 255]
    green = [0, 128, 0]
    blue = [255, 0, 0]

    # create the backbone of the output image according to the orientation
    if orientation == 'top':
        output_image[:200, :, :] = orange
        output_image[200:400, :, :] = white
        output_image[400:, :, :] = green
    if orientation == 'bottom':
        output_image[:200, :, :] = green
        output_image[200:400, :, :] = white
        output_image[400:, :, :] = orange
    if orientation == 'left':
        output_image[:, :200, :] = orange
        output_image[:, 200:400, :] = white
        output_image[:, 400:, :] = green
    if orientation == 'right':
        output_image[:, :200, :] = green
        output_image[:, 200:400, :] = white
        output_image[:, 400:, :] = orange

    # Draw the central circle
    cv2.circle(output_image, [300, 300], 100, blue, 2, cv2.LINE_AA)

    # Draw the spokes of the Ashok Chakra at 24 degrees each
    for angle in range(0, 360, 360 // 24):
        angle_rad = np.deg2rad(angle)
        x = int(300 + 100 * np.cos(angle_rad))
        y = int(300 + 100 * np.sin(angle_rad))

        cv2.line(output_image, [300, 300], [x, y], blue, 1, cv2.LINE_AA)

    ######################################################################

    return output_image
