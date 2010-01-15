Installing OpenCV 2.0 on OSX
============================

Tested on OpenCX 2.0 on OSX 10.5.  This is a condensed version of the `Mac OS X OpenCV Port`_ page on the OpenCV wiki.

`Download`_ OpenCV 2.0.0 and `CMake`_.

Unarchive::

    $ cd ~/Downloads
    $ tar xjvf OpenCV-2.0.0.tar.bz2

Make a build dir::

    $ mkdir OpenCV-2.0.0/build
    $ cd OpenCV-2.0.0/build

Configure using CMake::

    $ cmake ..
    $ ccmake .

Hit c to configure and g to generate the config.  Make sure that it's set up to build the new-style Python bindings if
you're planning to use them.

Make it::

    $ make -j8

Install it::

    $ sudo make install

At this point you should have everything you need to play with `facedetect.py`_.

You may also want to build the OpenCV framework but I haven't made use of it yet::

    $ cd ..
    $ ./make_frameworks.sh

Install the framework::

    $ sudo cp -r OpenCV.framework /Library/Frameworks/

.. _Mac OS X OpenCV Port: http://opencv.willowgarage.com/wiki/Mac_OS_X_OpenCV_Port
.. _Download: http://sourceforge.net/projects/opencvlibrary/files/
.. _CMake: http://www.cmake.org/
.. _facedetect.py: http://github.com/mcroydon/opencv_playground/blob/master/facedetect.py
