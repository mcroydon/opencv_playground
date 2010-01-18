import cv

# Load an image
image = cv.LoadImage('image.jpg')

# Get the size of the image
size = cv.GetSize(image)

# Convert to gray
gray_image = cv.CreateImage(size, 8, 1)
cv.CvtColor(image, gray_image, cv.CV_RGB2GRAY)

# Create temporary images for processing
eig_image = cv.CreateImage(size, 32, 1)
temp_image = cv.CreateImage(size, 32, 1)

# http://opencv.willowgarage.com/documentation/python/feature_detection.html#goodfeaturestotrack
corners = cv.GoodFeaturesToTrack(gray_image, eig_image, temp_image, 100, 0.04, 2)

for corner in corners:
    print corner
    cv.Circle(image, corner, 5, cv.RGB(0,255,0), -1)

cv.NamedWindow('Good features')
cv.ShowImage('Good features', image)

while 1:
    # Break on ESC
    key = cv.WaitKey(10)
    if key == 0x1b:
        break