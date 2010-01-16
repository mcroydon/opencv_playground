import cv

# Load an image as grayscale
image = cv.LoadImage('image.jpg', 0)

# Get the size of the image
size = cv.GetSize(image)

# Create an image to save edge data to
edges_image = cv.CreateImage(size, 8, 1)

# Canny edge detection
# http://opencv.willowgarage.com/documentation/python/feature_detection.html
cv.Canny(image, edges_image, 70.0, 140.0)

# Save the edges image
cv.SaveImage('edges_image.jpg', edges_image)
