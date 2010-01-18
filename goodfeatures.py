from webcam import WebCam
from manipulators.goodfeatures import goodfeatures

class GoodFeaturesWebCam(WebCam):
    def process_image(self, image):
        return goodfeatures(image)


if __name__=="__main__":
    webcam = GoodFeaturesWebCam()
    webcam.capture_video()
