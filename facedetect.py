from webcam import WebCam
from manipulators.facedetect import detect

class FaceDectWebCam(WebCam):
    def process_image(self, im):
        return detect(im)

if __name__=="__main__":
    webcam = FaceDectWebCam()
    webcam.capture_video()
