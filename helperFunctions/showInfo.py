import cv2 as cv
import numpy as np
import pandas as pd
from pandas.plotting import table 
import matplotlib.pyplot as plt

# Takes a list of cameras and creates an image with the information

def showInfo(cameraList):
    # Get information
    info=[]
    for cam in cameraList:
        if len(info)==0:
            info.append('----- General Info -----')
            info.append('Window display:    '+str(cam.display_zoom))
            info.append('Experiment name:    '+str(cam.expName))
            info.append('Recording status:    '+str(cam.recordingStatus))
            info.append('Video Format:    '+str(cam.videoOutput))
            if cam.timer is not None:
                t = str(cam.timer.get())
            else:
                t = '00:00:00'
            info.append('Recording length:  '+t)

        info.append('----- '+cam.cameraName+' -----')
        info.append('Resolution:    '+str(cam.saveResolution)+' px height')
        info.append('FPS:    '+str(cam.fps))
        info.append('Lower threshold:    '+str(cam.lowerThresh))
        info.append('Higher threshold:    '+str(cam.higherThresh))



    # Variables
    font = cv.FONT_HERSHEY_DUPLEX
    scale=1
    thick = 1
    verticalSpacing = 10
    valuesShown = len(info)+1
    horizontalBuffer = 15

    # Image size
    testText=max(info, key=len)
    textSize = cv.getTextSize(text=testText, fontFace=font, fontScale=scale, thickness=thick)
    (width, stringHeigth),_base = textSize 
    stringHeigth=stringHeigth+verticalSpacing

    # Create image
    height = stringHeigth * valuesShown
    width=width + 2*horizontalBuffer
    info_image = np.full((height,width,3),255, np.uint8)

    h=stringHeigth # current position 
    for text in info:
        info_image = cv.putText(info_image,text , (horizontalBuffer,h), font,scale, (30,37,72), thick, cv.LINE_AA)
        h = h+stringHeigth

    return(info_image)
    
