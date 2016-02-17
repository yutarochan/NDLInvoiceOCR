# Inovoice OCR TODO

* Sample Dataset Creation (use word, or any other existing papers).
    * Image Based
    * PDF -> Image Conversion Codebase
    * Find/Develop libraries to preprocess data in a consistent filetype (png or jpg)
        * ImageMagick with Wand wrapping: http://garmoncheg.blogspot.com/2013/07/python-converting-pdf-to-image.html
        * Another ImageMagick implementation: http://www.xavierdupre.fr/blog/2014-03-12_nojs.html
* Data Preprocessing Pipeline
    * Research methods to denoise image to make sure we can have a consistent output of information
    * Look to using OpenCV and scikit-image
    * Preprocessing Techniques We can Implement:
        * Convert image to a grayscale
        * Apply image thresholding
        * Apply image bounding box
        * Segment images to smaller blobs or text regions
* Try out different OCR Libraries for Text Scraping and perform error rate analysis for each frameworks.
    * OpenCV
    * Ocropus
    * ScikitLearn
    * Tesseract (Claims to be the best one)
* If all else fails, we'll roll our own OCR library using a KNN or LSTM Neural
Network architecture,
* Devise extraction pipeline for converting many documents
    * Establish a pipeline workflow.
    * Obtain further requirement details to make sure we build out the system
    for the proper users

## Research and Sources
* http://stackoverflow.com/questions/11464397/image-preprocessing-for-text-recognition/11471322#11471322
* http://stackoverflow.com/questions/9413216/simple-digit-recognition-ocr-in-opencv-python/9620295#9620295
* http://blog.damiles.com/2008/11/basic-ocr-in-opencv/

## Dependencies
The program used to develop the OCR pipline requires the following dependencies.
Assuming you are using a Debian based system, make sure you have the following
packages installed:

### Tesseract OCR
Install the following dependencies to utilize Tesseract API

    sudo pip install pytesseract
    sudo apt-get install tesseract-ocr
