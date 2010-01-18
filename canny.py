from webcam import WebCam
from manipulators.canny import canny

class CannyWebCam(WebCam):
    def process_image(self, image):
        return canny(image)


if __name__=="__main__":
    webcam = CannyWebCam()
    webcam.capture_video()
