import cv


class WebCam(object):
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.camera = cv.CreateCameraCapture(0)

    def get_image(self):
        """ Get the current frame and convert to an Image object """
        im = cv.QueryFrame(self.camera)
        im = self.process_image(im)
        return im

    def process_image(self, im):
        """ Hook to do some image processing / manipulation """
        return im

    def capture_video(self):
        fps = 30.0
        try:
            cv.NamedWindow('Camera', cv.CV_WINDOW_AUTOSIZE)
            while True:
                im = self.get_image()
                cv.ShowImage('Camera', im)
                key = cv.WaitKey(int(1000 * 1.0/fps))
                if key == 0x1b:
                    break
        except KeyboardInterrupt:
            return


if __name__=="__main__":
    webcam = WebCam()
    webcam.capture_video()
