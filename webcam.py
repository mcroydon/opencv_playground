import cv
import Image
import pygame
import sys
from pygame.locals import *


class WebCam(object):
    def __init__(self, width=640, height=480):
        self.width = width
        self.height = height
        self.camera = cv.CreateCameraCapture(0)

    def get_image(self):
        """ Get the current frame and convert to an Image object """
        im = cv.QueryFrame(self.camera)
        return Image.fromstring("RGB", (im.width, im.height), im.tostring())

    def capture_video(self):
        fps = 30.0
        pygame.init()
        window = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption("WebCam Demo")
        screen = pygame.display.get_surface()
        try:
            while True:
                events = pygame.event.get()
                for event in events:
                    if event.type == QUIT or event.type == KEYDOWN:
                        sys.exit(0)
                im = self.get_image()
                pg_img = pygame.image.frombuffer(im.tostring(), im.size, im.mode)
                screen.blit(pg_img, (0,0))
                pygame.display.flip()
            pygame.time.delay(int(1000 * 1.0/fps))
        except KeyboardInterrupt:
            return

if __name__=="__main__":
    webcam = WebCam()
    webcam.capture_video()
