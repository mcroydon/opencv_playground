from webcam import WebCam
from facedetect import detect

class FaceDectWebCam(WebCam):
    def process_image(self, im):
        return detect(im)

if __name__=="__main__":
    webcam = FaceDectWebCam()
    webcam.capture_video()
