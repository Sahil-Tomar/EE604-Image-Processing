import cv2
import numpy as np


def k_means(img, k):
    """Blurs the Image and then applies k-means clustering to the image"""

    # blur the image before applying k-means clustering
    img = cv2.GaussianBlur(img, (5, 5), 2)

    # reshape the Image
    reshaped_image = img.reshape((-1, 3))

    # convert to np.float32
    reshaped_image = np.float32(reshaped_image)

    # define the criteria
    criteria = (cv2.TERM_CRITERIA_EPS, 10, 1.0)

    # apply k-means
    ret, label, center = cv2.kmeans(reshaped_image, k, None, criteria, 10, cv2.KMEANS_RANDOM_CENTERS)

    # converting back into uint8
    center = np.uint8(center)

    # reshape again
    res = center[label.flatten()]
    k_means_img = res.reshape(img.shape)

    return k_means_img


def morphological_transformation(mask):
    """morphologically transform the mask that detects the heads of Raavana"""

    # take only the top half of the ravana image
    mask_up = mask[:mask.shape[0] // 2, :]

    # open the image in order to remove small noise
    opening = cv2.morphologyEx(mask_up, cv2.MORPH_OPEN, kernel=cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5)))

    # take a threshold on the distance transform of the opening
    dist_transform = cv2.distanceTransform(opening, cv2.DIST_L2, 5)
    _, thresh = cv2.threshold(dist_transform, 0.3 * dist_transform.max(), 255, 0)

    # open once again to remove the noise
    morph_image = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel=cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3)), iterations=5).astype(np.uint8)

    return morph_image


def count_contours_left_right(binary_image):
    """1.finds the contours in the morphologically transformed mask-image
       2. finds the max-area contour for the central head
       3. Counts the number of contours left and right of the central head
       returns the number of contours left and right of the largest contours respectively
    """
    # Find contours
    contours, hierarchy = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # Find the contour with the maximum area
    max_contour = max(contours, key=cv2.contourArea)

    # Calculate the centroid of the maximum area contour
    max_area_centroid = np.array([int(cv2.moments(max_contour)['m10'] / cv2.moments(max_contour)['m00']),
                                  int(cv2.moments(max_contour)['m01'] / cv2.moments(max_contour)['m00'])])

    # Initialize counters for contours on the left and right
    contours_left = 0
    contours_right = 0

    # Iterate through contours
    for contour in contours:
        # Skip the maximum area contour
        if contour is max_contour:
            continue

        # Calculate the centroid of the current contour
        contour_centroid = np.array([int(cv2.moments(contour)['m10'] / cv2.moments(contour)['m00']),
                                     int(cv2.moments(contour)['m01'] / cv2.moments(contour)['m00'])])

        # Check if the contour is on the left or right
        if contour_centroid[0] < max_area_centroid[0]:
            contours_left += 1
        else:
            contours_right += 1

    return contours_left, contours_right


def solution(image_path):
    # load image
    img = cv2.imread(image_path)

    # apply k-means with k=5
    k_means_img = k_means(img, 5)

    # threshold the image to take out only the heads of Raavana
    mask = cv2.inRange(cv2.cvtColor(k_means_img, cv2.COLOR_BGR2GRAY), 160, 175)

    # morphologically transform the image to get only the head's contours
    morph_transform = morphological_transformation(mask)

    # get the number of heads left and right of the main head
    left, right = count_contours_left_right(morph_transform)

    # default class
    class_name = 'fake'

    # only case where it is real
    # when there are 4 heads to the left of central head 
    # and there are 5 heads to the right of central head 
    if left == 4 and right == 5:
        class_name = 'real'

    return class_name
