from ctypes import cast, POINTER, c_ubyte
from time import sleep
import cv2
import numpy as np
from PyQt5.QtCore import *
from debugging import debugging
from helperFunctions.connect import connection
from timeit import default_timer as timer
from helperFunctions.timer import MyTimer
from helperFunctions.createFile import createFile
from datetime import datetime

# conditonal imports
if not debugging:
    from egrabber import *

class Camera(QRunnable):

    def __init__(self, grabber, name,timeKeeper):
        QObject.__init__(self)
        self.grabber = grabber #Euresys grabber
        self.signals = CameraSignals() # Thread connection
        self.cameraName = name # Camera model and vendor
        self.running = True # Controls run function
        self.display_zoom = 1 # Make image smaller or bigger
        self.recording = False # Controls recording
        self.saveResolution = 1472 # Defines the height
        self.videoOutput = 'mp4' # Video format
        self.savePath=None # Path to save video
        self.expName=None # Name of the experiment to save files
        self.fps=0 # Current fps
        self.timeKeeper = timeKeeper # Is this camera taking care of time?
        self.recordingStatus='Null' # Shows info about recording
        self.everRecorded = False # To create a new container
        self.start_drag = None # Will be change to a point (x,y). Based on resized img
        self.end_drag=None # Point
        self.areaOfInteres = None # List of int representing dimensions
        self.hoverinOn = None # Point where mouse is hovering
        self.lowerThresh = 0 # Image thresholding
        self.higherThresh=255 # Image thresholding
        self.timer=None # Timer for camera

        self.capturing = False # Controls when a picture is taken
        self.imgFormat = 'png' # Saves image in this format
        self.showThresh = False # Wehater or not to threshold the image

        
    
    # Takes list of grabber from gui
    def run(self):
        # Local variables
        lastTime = 0
        measuredTime = 1
        allTimes = []

        # Open camera
        if debugging:
            cap = cv2.VideoCapture('media/randomVideo.MOV')
        else:
            # Create 3 buffers for the grabber
            self.grabber.realloc_buffers(3)
            # Start the grabber
            self.grabber.start()

        # Capture and display loop
        while self.running:
            # Get image
            if debugging:
                ret, img = cap.read()
                sleep(1)
                timeStamp=datetime.now()
                if not ret:
                    print('error reading video')
                    break
            else:
                with Buffer(self.grabber) as buffer:
                    # Get address, width, and height of image in buffer
                    ptr = buffer.get_info(BUFFER_INFO_BASE, INFO_DATATYPE_PTR)
                    w = buffer.get_info(BUFFER_INFO_WIDTH, INFO_DATATYPE_SIZET)
                    h = buffer.get_info(BUFFER_INFO_DELIVERED_IMAGEHEIGHT, INFO_DATATYPE_SIZET)
                    timeStamp = buffer.get_info(BUFFER_INFO_TIMESTAMP, INFO_DATATYPE_UINT64)
                    # Convert image to BGR format
                    bgr = buffer.convert('BGR8')
                    # Resize and display the image (using opencv and numpy)
                    data = cast(bgr.get_address(), POINTER(c_ubyte * bgr.get_buffer_size())).contents
                    img = np.frombuffer(data, count=bgr.get_buffer_size(), dtype=np.uint8).reshape((h,w,3))
                
            # Crop image
            img = self.cropImage(img)
            h, w, channels = img.shape
            # Show current pixelColor
            infoImg = self.hoveringColors(img.copy(),h)
            # Display image
            disImg=self.drawRect(infoImg)
            try:
                disImg = cv2.resize(disImg, (int(w * self.display_zoom), int(h * self.display_zoom)))
            except:
                print('Problem dimensions visualizing: ', w,h)

            if self.showThresh:
                # Threshold image 
                threshImg = self.threshold(img.copy())
                try:
                    threshImg = cv2.resize(threshImg, (int(w * self.display_zoom), int(h * self.display_zoom)))
                except:
                    print('Problem dimensions thresholding: ', w,h)
                # Send image to gui
                self.signals.images.emit(('Thresholded '+self.cameraName,threshImg))

            # Emit images
            if self.capturing:
                blank = np.full((int(h * self.display_zoom),int(w * self.display_zoom),3),255, np.uint8)
                self.signals.images.emit((self.cameraName,blank))
            else:
                self.signals.images.emit((self.cameraName,disImg))

            # Image to save
            # Resize 
            factor = self.saveResolution/h
            if factor>1:
                saveW = w
                saveH=h
            else:
                saveW = w*factor
                saveH=self.saveResolution
            outImg = cv2.resize(img, (int(saveW), int(saveH)))

            if self.recording and self.fps !=0:
                self.recordVideo(outImg,saveW,saveH,timeStamp)

            if self.capturing:
                self.capturing=False
                # Create file name
                fileName=self.expName+'_'+self.cameraName
                name = createFile(self.savePath,fileName,self.imgFormat)
                cv2.imwrite(name, outImg)

            # Measure fps
            timeNow=timer()
            timePassed= timeNow-lastTime
            allTimes.append(timeStamp)
            if  timePassed> measuredTime:
                # Set new time
                lastTime=timeNow
                # Update fps
                if len(allTimes)>2:
                    self.fps = (len(allTimes)*1000000)/(allTimes[-1]-allTimes[0])
                    allTimes=[]
                
                # Send signal
                if self.timeKeeper:
                    self.signals.updateInfo.emit()


        if not debugging:
            self.grabber.stop()
        if self.everRecorded:
            self.out.release()
            self.everRecorded = False
            self.f.close()
        print('end of camera ', self.cameraName)

    def recordVideo(self, img, w,h, timeStamp):
        # Create container to record
        if not self.everRecorded:
            videoName=self.expName+'_'+self.cameraName
            name = createFile(self.savePath,videoName,self.videoOutput)
            if self.videoOutput =='avi':
                fourcc='MJPG'
            else:
                fourcc='mp4v'
            # Create video holder
            self.out =cv2.VideoWriter(name,cv2.VideoWriter_fourcc(*fourcc),self.fps, (int(w),int(h)))
            self.everRecorded=True
            self.timer  = MyTimer()
            self.timer.start()
            # Create file with timeStamps
            timeName='times_'+self.expName+'_'+self.cameraName
            self.timeName=createFile(self.savePath,timeName,'txt')
            f = open(timeName,'w')
            f.close()
                
        # Save image in path
        f = open(self.timeName,'a')
        f.write(str(timeStamp))
        f.write('\n')
        self.out.write(img)


    def drawRect(self,img):
        if self.start_drag is not None:
            if self.end_drag is None:
                self.end_drag = (self.start_drag[0]+5,self.start_drag[1]+5)
            # Change values based on zoom
            start = (int(self.start_drag[0]/self.display_zoom),int(self.start_drag[1]/self.display_zoom))
            end = (int(self.end_drag[0]/self.display_zoom),int(self.end_drag[1]/self.display_zoom))
            # Draw rectangle
            img = cv2.rectangle(img, start, end, (102,255,102), 8)
        return img

    def setZoom(self):
        if self.areaOfInteres is None:
            x1 = int(self.start_drag[0]/self.display_zoom)
            y1=int(self.start_drag[1]/self.display_zoom)
            x2=int(self.end_drag[0]/self.display_zoom)
            y2=int(self.end_drag[1]/self.display_zoom)

            if x2<x1:
                c=x1
                x1=x2
                x2=c
            if y2<y1:
                c = y1
                y1=y2
                y2=c

            y = y2-y1
            x = x2 - x1
            if x <32 or y<32:
                self.areaOfInteres = None
            else:
                self.areaOfInteres = [x1,x2,y1,y2]
        
    def cropImage(self,img):
        if self.areaOfInteres is not None:
            x1,x2,y1,y2=self.areaOfInteres
            img=img[y1:y2, x1:x2]
        return img

    def hovering(self,x,y):
        self.hoverinOn= [int(y/self.display_zoom), int(x/self.display_zoom)]

    def hoveringColors(self,img,h):
        if self.hoverinOn is not None:
            try:
                (b, g, r) = img[self.hoverinOn[0],self.hoverinOn[1]]
            except:
                b,g,r=0,0,0
            text='B:'+str(b)+' G:'+str(g)+' R:'+str(r)
            img=cv2.putText(img,text,(15,h),cv2.FONT_HERSHEY_SIMPLEX,3,(102,255,102),2)
        return img
            
    def threshold(self,img):
        img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        ret,lowImg = cv2.threshold(img.copy(),self.lowerThresh,255,cv2.THRESH_BINARY)
        ret,highImg = cv2.threshold(img.copy(),self.higherThresh,255,cv2.THRESH_BINARY_INV)
        img = cv2.bitwise_and(lowImg, highImg)
        return img

class CameraSignals(QObject):
    images = pyqtSignal(object)
    updateInfo = pyqtSignal()
