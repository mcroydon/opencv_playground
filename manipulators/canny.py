import cv

def canny(image):

    # Get the size of the image
    size = cv.GetSize(image)

    # Create a gray scale image
    gray_image = cv.CreateImage(size, 8, 1)
    cv.CvtColor(image, gray_image, cv.CV_RGB2GRAY)

    # Create an image to save edge data to
    edges_image = cv.CreateImage(size, 8, 1)

    # Canny edge detection
    # http://opencv.willowgarage.com/documentation/python/feature_detection.html
    cv.Canny(gray_image, edges_image, 70.0, 140.0)

    return edges_image
