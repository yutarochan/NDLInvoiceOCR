# Tesseract OCR Result Analysis

## Trial 1: No Preprocessing
* Decent results with some mismatch of character based recognition, pretty good actually.
* Potential Preprocessing Fixes:
    * Perform image thresholding. (Sample used in experiment was slightly washedout)
    * Convert image to black and white. (Ensure consistency in data)
    * Remove noise and random artifacts from data. (Some noise may introduce random  characters)
* Additional factors to consider:
    * If the invoice seems to have a consistent format, we can potentially crop out or hand construct
    bounding parameters to use to ensure a higher accuracy in the OCR process. (Need to check to see
    if this is the case).

## Trial 2: Simple Preprocessing
To be completed...
