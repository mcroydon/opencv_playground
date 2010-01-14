# -*- coding: utf-8 -*-
"""
An example of face detection using OpenCV and the new Python bindings.

You can detect faces in an image from your local filesystem::

    python facedetect.py -f image.jpg

You can also detect faces in an image from a remote URL::

    python facedetect.py -u http://example.com/image.jpg

You'll need to set an environment variable (HAAR_PATH) to the location that you installed
OpenCV Haar support files to.  This defaults to ``/usr/local/share/opencv/haarcascades``,
the default location on OSX 10.5 and perhaps other platforms.

This program is based on code from `Fun with Python, OpenCV and face detection`_
which in turn was based on code from `Face Detection on the OLPC XO`_ and updated
to use the `OpenCV 2.0 Python API`_, heavily referencing the `OpenCV 2.0 Python Reference`_.

.. _Fun with Python, OpenCV and face detection: http://blog.jozilla.net/2008/06/27/fun-with-python-opencv-and-face-detection/
.. _Face Detection on the OLPC XO: http://eclecti.cc/code/face-detection-on-the-olpc-xo
.. _OpenCV 2.0 Python API: http://opencv.willowgarage.com/wiki/PythonInterface
.. _OpenCV 2.0 Python Reference: http://opencv.willowgarage.com/documentation/python/index.html
"""

__author__ = 'Matt Croydon'
__version__ = ('0', '1', '0', 'alpha')
__license__ = 'BSD'

from optparse import OptionParser
import cv, os, urllib

HAAR_PATH = os.environ.get('HAAR_PATH', '/usr/local/share/opencv/haarcascades/')

def detect(imagename):
    # Load the image
    image = cv.LoadImage(imagename)

    # Make a grayscale copy
    size = cv.GetSize(image)
    gray_image = cv.CreateImage(size, 8, 1)
    cv.CvtColor(image, gray_image, cv.CV_RGB2GRAY)

    # Equalize histogram
    cv.EqualizeHist(gray_image, gray_image)

    # Detect faces
    cascade = cv.Load(os.path.join(HAAR_PATH, "haarcascade_frontalface_default.xml"))
    faces = cv.HaarDetectObjects(gray_image, cascade, cv.CreateMemStorage())
    for (x,y,w,h),n in faces:
        cv.Rectangle(image, (x,y), (x+w,y+h), 255)

    # Return the face-detected image
    return image

if __name__ == '__main__':
    usage = "usage: %prog [options] (-h for help)"
    parser = OptionParser(usage)
    parser.add_option("-f", "--file", dest="filename", help="read data from FILENAME")
    parser.add_option("-u", "--url", dest="url",help="read data from URL")
    
    (options, args) = parser.parse_args()
    if options.filename and options.url:
        parser.error("Cannot use both file and url options.")
    if not options.filename and not options.url:
        parser.error("Either a file or url are required.")
    if options.filename:
        image = detect(options.filename)
    elif options.url:
        (filename, headers) = urllib.urlretrieve(options.url)
        image = detect(filename)

    cv.NamedWindow('Detect')
    cv.ShowImage('Camera', image)
    
    while 1:
        # Break on ESC
        key = cv.WaitKey(10)
        if key == 0x1b:
            break