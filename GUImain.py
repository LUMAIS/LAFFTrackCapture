from numpy import record
import pandas as pd
from camera import Camera
import cv2 as cv
from debugging import debugging
from pathlib import Path
from helperFunctions.showInfo import showInfo
from helperFunctions.saveCameraInfo import saveCameraInfo

# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUImain.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CameraLayout(object):
    def setupUi(self, CameraLayout,grabberList):
        self.grabberList = grabberList

        CameraLayout.setObjectName("CameraLayout")
        CameraLayout.resize(441, 450)
        self.gridLayout = QtWidgets.QGridLayout(CameraLayout)
        self.gridLayout.setContentsMargins(12, -1, -1, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.notesInput = QtWidgets.QPlainTextEdit(CameraLayout)
        self.notesInput.setObjectName("notesInput")
        self.gridLayout.addWidget(self.notesInput, 6, 0, 1, 1)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.videoRecLabel = QtWidgets.QLabel(CameraLayout)
        self.videoRecLabel.setObjectName("videoRecLabel")
        self.horizontalLayout_6.addWidget(self.videoRecLabel)
        self.videoRecStartBtn = QtWidgets.QPushButton(CameraLayout)
        self.videoRecStartBtn.setObjectName("videoRecStartBtn")
        self.horizontalLayout_6.addWidget(self.videoRecStartBtn)
        self.videoRecPausetBtn = QtWidgets.QPushButton(CameraLayout)
        self.videoRecPausetBtn.setObjectName("videoRecPausetBtn")
        self.horizontalLayout_6.addWidget(self.videoRecPausetBtn)
        self.videoRecStopBtn = QtWidgets.QPushButton(CameraLayout)
        self.videoRecStopBtn.setObjectName("videoRecStopBtn")
        self.horizontalLayout_6.addWidget(self.videoRecStopBtn)
        self.videoFormatInput = QtWidgets.QComboBox(CameraLayout)
        self.videoFormatInput.setMaximumSize(QtCore.QSize(80, 16777215))
        self.videoFormatInput.setObjectName("videoFormatInput")
        self.videoFormatInput.addItem("")
        self.videoFormatInput.addItem("")
        self.horizontalLayout_6.addWidget(self.videoFormatInput)
        self.gridLayout.addLayout(self.horizontalLayout_6, 9, 0, 1, 1)
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.pictureLabel = QtWidgets.QLabel(CameraLayout)
        self.pictureLabel.setObjectName("pictureLabel")
        self.horizontalLayout_7.addWidget(self.pictureLabel)
        self.pictureTakeBtn = QtWidgets.QPushButton(CameraLayout)
        self.pictureTakeBtn.setObjectName("pictureTakeBtn")
        self.horizontalLayout_7.addWidget(self.pictureTakeBtn)
        self.pictureFormatsInput = QtWidgets.QComboBox(CameraLayout)
        self.pictureFormatsInput.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pictureFormatsInput.setObjectName("pictureFormatsInput")
        self.pictureFormatsInput.addItem("")
        self.pictureFormatsInput.addItem("")
        self.pictureFormatsInput.addItem("")
        self.pictureFormatsInput.addItem("")
        self.horizontalLayout_7.addWidget(self.pictureFormatsInput)
        self.gridLayout.addLayout(self.horizontalLayout_7, 11, 0, 1, 1)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.ExpandingFieldsGrow)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.formLayout.setFormAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.formLayout.setContentsMargins(0, 0, 0, -1)
        self.formLayout.setHorizontalSpacing(23)
        self.formLayout.setVerticalSpacing(10)
        self.formLayout.setObjectName("formLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.cameraSelectionLabel = QtWidgets.QLabel(CameraLayout)
        self.cameraSelectionLabel.setObjectName("cameraSelectionLabel")
        self.verticalLayout_2.addWidget(self.cameraSelectionLabel)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.startStreamingBtn = QtWidgets.QPushButton(CameraLayout)
        self.startStreamingBtn.setObjectName("startStreamingBtn")
        self.horizontalLayout_2.addWidget(self.startStreamingBtn)
        self.stopStreamingBtn = QtWidgets.QPushButton(CameraLayout)
        self.stopStreamingBtn.setObjectName("stopStreamingBtn")
        self.horizontalLayout_2.addWidget(self.stopStreamingBtn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout_2)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(5, -1, -1, -1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        # Create cameras and add to gui
        self.cameraNames = self.getCameras()
        self.cameraOptions=[]
        for c in self.cameraNames:
            name = c.split()
            name = name[0]
            option = QtWidgets.QCheckBox(c,CameraLayout)
            option.setObjectName(name)
            self.cameraOptions.append(option)
            self.verticalLayout_3.addWidget(option)
        
        self.formLayout.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_3)
        self.windoSzLabel = QtWidgets.QLabel(CameraLayout)
        self.windoSzLabel.setObjectName("windoSzLabel")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.windoSzLabel)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setContentsMargins(5, -1, -1, -1)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.windoSzSmall = QtWidgets.QPushButton(CameraLayout)
        self.windoSzSmall.setObjectName("windoSzSmall")
        self.horizontalLayout_5.addWidget(self.windoSzSmall)
        self.windoSzBig = QtWidgets.QPushButton(CameraLayout)
        self.windoSzBig.setObjectName("windoSzBig")
        self.horizontalLayout_5.addWidget(self.windoSzBig)
        self.formLayout.setLayout(1, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_5)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.exposureLabel = QtWidgets.QLabel(CameraLayout)
        self.exposureLabel.setObjectName("exposureLabel")
        self.horizontalLayout_3.addWidget(self.exposureLabel)
        self.exposureSelect = QtWidgets.QComboBox(CameraLayout)
        self.exposureSelect.setObjectName("exposureSelect")
        self.horizontalLayout_3.addWidget(self.exposureSelect)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_3)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.exposureInput = QtWidgets.QSlider(CameraLayout)
        self.exposureInput.setOrientation(QtCore.Qt.Horizontal)
        self.exposureInput.setObjectName("exposureInput")
        self.horizontalLayout.addWidget(self.exposureInput)
        self.exposureValue = QtWidgets.QLineEdit(CameraLayout)
        self.exposureValue.setMaximumSize(QtCore.QSize(40, 16777215))
        self.exposureValue.setObjectName("exposureValue")
        self.horizontalLayout.addWidget(self.exposureValue)
        self.formLayout.setLayout(2, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.resolutionLabel = QtWidgets.QLabel(CameraLayout)
        self.resolutionLabel.setObjectName("resolutionLabel")
        self.horizontalLayout_8.addWidget(self.resolutionLabel)
        self.resolutionSelect = QtWidgets.QComboBox(CameraLayout)
        self.resolutionSelect.setObjectName("resolutionSelect")
        self.horizontalLayout_8.addWidget(self.resolutionSelect)
        self.formLayout.setLayout(3, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_8)
        self.resolutionInput = QtWidgets.QComboBox(CameraLayout)
        self.resolutionInput.setObjectName("resolutionInput")
        self.resolutionInput.addItem("")
        self.resolutionInput.addItem("")
        self.resolutionInput.addItem("")
        self.resolutionInput.addItem("")
        self.resolutionInput.addItem("")
        self.resolutionInput.addItem("")
        self.resolutionInput.addItem("")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.resolutionInput)
        self.fpsLabel = QtWidgets.QLabel(CameraLayout)
        self.fpsLabel.setObjectName("fpsLabel")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.fpsLabel)
        self.fpsInput = QtWidgets.QDoubleSpinBox(CameraLayout)
        self.fpsInput.setMinimum(0.1)
        self.fpsInput.setMaximum(10.0)
        self.fpsInput.setObjectName("fpsInput")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.fpsInput)
        self.threshLabel = QtWidgets.QLabel(CameraLayout)
        self.threshLabel.setObjectName("threshLabel")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.threshLabel)
        self.threshInput = QtWidgets.QPushButton(CameraLayout)
        self.threshInput.setObjectName("threshInput")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.threshInput)
        self.gridLayout.addLayout(self.formLayout, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.saveInLabel = QtWidgets.QLabel(CameraLayout)
        self.saveInLabel.setObjectName("saveInLabel")
        self.horizontalLayout_4.addWidget(self.saveInLabel)
        self.saveInInput = QtWidgets.QLineEdit(CameraLayout)
        self.saveInInput.setObjectName("saveInInput")
        self.horizontalLayout_4.addWidget(self.saveInInput)
        self.saveInBtn = QtWidgets.QPushButton(CameraLayout)
        self.saveInBtn.setObjectName("saveInBtn")
        self.horizontalLayout_4.addWidget(self.saveInBtn)
        self.gridLayout.addLayout(self.horizontalLayout_4, 8, 0, 1, 1)
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.nameLabel = QtWidgets.QLabel(CameraLayout)
        self.nameLabel.setObjectName("nameLabel")
        self.horizontalLayout_9.addWidget(self.nameLabel)
        self.nameInput = QtWidgets.QLineEdit(CameraLayout)
        self.nameInput.setObjectName("nameInput")
        self.horizontalLayout_9.addWidget(self.nameInput)
        self.gridLayout.addLayout(self.horizontalLayout_9, 7, 0, 1, 1)
        self.notesLabel = QtWidgets.QLabel(CameraLayout)
        self.notesLabel.setObjectName("notesLabel")
        self.gridLayout.addWidget(self.notesLabel, 5, 0, 1, 1)

        # Connections
        self.startStreamingBtn.clicked.connect(self.startCameras)
        self.exposureInput.valueChanged.connect(self.changeExposureSlider)
        self.stopStreamingBtn.clicked.connect(self.stopCameras)
        self.windoSzBig.clicked.connect(self.goUp)
        self.windoSzSmall.clicked.connect(self.goDown)
        self.exposureSelect.currentIndexChanged.connect(self.setUpExposure)
        self.exposureValue.returnPressed.connect(self.changeExposureText)
        self.resolutionSelect.currentIndexChanged.connect(self.resolutionCameraSelected)
        self.resolutionInput.currentTextChanged.connect(self.changeResolution)
        self.videoRecStartBtn.clicked.connect(self.startRecording)
        self.videoRecPausetBtn.clicked.connect(self.pauseRecording)
        self.videoRecStopBtn.clicked.connect(self.stopRecording)
        self.saveInBtn.clicked.connect(self.selectPath)
        self.pictureTakeBtn.clicked.connect(self.getImage)
        self.fpsInput.valueChanged.connect(self.updateFPS)
        self.threshInput.clicked.connect(self.toggleThresh)

        # Initial set up
        self.enableAll(False)
        self.fpsInput.setValue(10.0)

        self.retranslateUi(CameraLayout)
        QtCore.QMetaObject.connectSlotsByName(CameraLayout)

    def retranslateUi(self, CameraLayout):
        _translate = QtCore.QCoreApplication.translate
        CameraLayout.setWindowTitle(_translate("CameraLayout", "Camera"))
        self.notesInput.setPlaceholderText(_translate("CameraLayout", "Lights and camera parameters, etc"))
        self.videoRecLabel.setText(_translate("CameraLayout", "Video recording:"))
        self.videoRecStartBtn.setText(_translate("CameraLayout", "Start"))
        self.videoRecPausetBtn.setText(_translate("CameraLayout", "Pause"))
        self.videoRecStopBtn.setText(_translate("CameraLayout", "Stop"))
        self.videoFormatInput.setItemText(0, _translate("CameraLayout", "mp4"))
        self.videoFormatInput.setItemText(1, _translate("CameraLayout", "avi"))
        self.pictureLabel.setText(_translate("CameraLayout", "Picture: "))
        self.pictureTakeBtn.setText(_translate("CameraLayout", "Take"))
        self.pictureFormatsInput.setItemText(0, _translate("CameraLayout", "jpg"))
        self.pictureFormatsInput.setItemText(1, _translate("CameraLayout", "png"))
        self.pictureFormatsInput.setItemText(2, _translate("CameraLayout", "gif"))
        self.pictureFormatsInput.setItemText(3, _translate("CameraLayout", "tiff"))
        self.cameraSelectionLabel.setText(_translate("CameraLayout", "Select camera: "))
        self.startStreamingBtn.setText(_translate("CameraLayout", "Start"))
        self.stopStreamingBtn.setText(_translate("CameraLayout", "Stop"))
        self.windoSzLabel.setText(_translate("CameraLayout", "Window size:"))
        self.windoSzSmall.setText(_translate("CameraLayout", "x 0.5"))
        self.windoSzBig.setText(_translate("CameraLayout", "x 2"))
        self.exposureLabel.setText(_translate("CameraLayout", "Exposure:"))
        self.resolutionLabel.setText(_translate("CameraLayout", "Resolution:"))
        self.resolutionInput.setItemText(0, _translate("CameraLayout", "128 px"))
        self.resolutionInput.setItemText(1, _translate("CameraLayout", "576 px"))
        self.resolutionInput.setItemText(2, _translate("CameraLayout", "1024 px"))
        self.resolutionInput.setItemText(3, _translate("CameraLayout", "1472 px"))
        self.resolutionInput.setItemText(4, _translate("CameraLayout", "1984 px"))
        self.resolutionInput.setItemText(5, _translate("CameraLayout", "2496 px"))
        self.resolutionInput.setItemText(6, _translate("CameraLayout", "3008 px"))
        self.fpsLabel.setText(_translate("CameraLayout", "FPS:"))
        self.threshLabel.setText(_translate("CameraLayout", "Show thresholds:"))
        self.threshInput.setText(_translate("CameraLayout", "Off"))
        self.saveInLabel.setText(_translate("CameraLayout", "Save in:"))
        self.saveInBtn.setText(_translate("CameraLayout", "Select folder"))
        self.nameLabel.setText(_translate("CameraLayout", "Name:"))
        self.notesLabel.setText(_translate("CameraLayout", "Other parameters:"))


    # Block and allow inputs
    def enableAll(self, toggle):
        self.windoSzBig.setEnabled(toggle)
        self.windoSzSmall.setEnabled(toggle)
        self.exposureSelect.setEnabled(toggle)
        self.exposureInput.setEnabled(toggle)
        self.exposureValue.setEnabled(toggle)
        self.resolutionSelect.setEnabled(toggle)
        self.resolutionInput.setEnabled(toggle)
        self.videoRecPausetBtn.setEnabled(toggle)
        self.videoRecStartBtn.setEnabled(toggle)
        self.videoRecStopBtn.setEnabled(toggle)
        self.pictureTakeBtn.setEnabled(toggle)
        self.stopStreamingBtn.setEnabled(toggle)
        self.videoFormatInput.setEnabled(toggle)
        self.pictureFormatsInput.setEnabled(toggle)
        self.notesInput.setEnabled(toggle)
        self.nameInput.setEnabled(toggle)
        self.saveInInput.setEnabled(toggle)
        self.saveInBtn.setEnabled(toggle)
        self.fpsInput.setEnabled(toggle)
        self.threshInput.setEnabled(toggle)
        
    # Extract camera model and vendor from grabber
    def getCameras(self):
        names = []
        if debugging:
            for n in range(3):
                names.append('cameraModel '+str(n) + 'vendor')
        else:
            for grabber in self.grabberList:
                if grabber.remote is not None:
                    vendor = grabber.remote.get('DeviceVendorName')
                    model = grabber.remote.get('DeviceModelName')
                    title = model + ' from ' + vendor
                    names.append(title)
        return names

    threadpool = QtCore.QThreadPool()
    running = False
    # Checks what cameras are selected and starts streaming
    def startCameras(self):
        # Check what cameras were selected
        camerasSelected = {}
        for index,c in enumerate(self.cameraOptions):
            # If camera was selected add to selected grabber
            if c.isChecked():
                if debugging:
                    camerasSelected[self.cameraNames[index]] = None
                else:
                    camerasSelected[self.cameraNames[index]] = self.grabberList[index]
                    # grabber = self.grabberList[index]
                    # cameraName = self.cameraNames[index]
                 
        # If cameras were selected and not already running, start streaming
        if len(camerasSelected)!=0 and not self.running:
            self.running = True
            # Block selection of new cameras
            for c in self.cameraOptions:
                c.setEnabled(False)
            self.enableAll(True)
            self.startStreamingBtn.setEnabled(False)
            self.cameras = []
            # Initialize all cameras
            timeKeeper = True
            for ix,name in enumerate(camerasSelected):
                # Get grabber from dictionary
                grabber = camerasSelected[name]
                # Set masters and slaves
                if len(camerasSelected)==1:
                    # If there is only one camera, disconnect
                    grabber.device.set('C2CLinkConfiguration', 'Disconnected')
                else:
                    grabber.device.set('C2CLinkConfiguration', 'Slave')
                    if ix+1 == len(camerasSelected):
                        grabber.device.set('C2CLinkConfiguration', 'Master')
                # Create worker
                name = name.replace(' ', '_')
                camera = Camera(grabber,name,timeKeeper)
                timeKeeper=False
                camera.signals.images.connect(self.showImg)
                camera.signals.updateInfo.connect(self.visualizeInfo)
                self.threadpool.start(camera)
                self.cameras.append(camera)
                print('starting camera ', name)
                # Create options in exposure and resolution 
                self.exposureSelect.addItem(name)
                self.resolutionSelect.addItem(name)
                # Create openCV window
                cv.namedWindow(name)
                cv.setMouseCallback(name, self.imageInteraction,ix)
                # Window for thresholds
                threshName = 'Thresholded '+name
                cv.namedWindow(threshName)
                cv.setMouseCallback(threshName, self.selectWindow,ix)
                cv.createTrackbar('Min',threshName,0,255,lambda x: self.changeThreshold(x,'min'))
                cv.createTrackbar('Max',threshName,0,255,lambda x: self.changeThreshold(x,'max'))
                cv.setTrackbarPos('Min', threshName, 0)
                cv.setTrackbarPos('Max', threshName, 255)
                print('Creating threshold window: ', threshName, ix)
        else:
            self.cameraError()

    # Stop cameras
    def stopCameras(self):
        self.running = False
        # Disable selection
        self.exposureSelect.clear()
        self.resolutionSelect.clear()
        self.enableAll(False)
        self.startStreamingBtn.setEnabled(True)
        # Turn off cameras
        for cam in self.cameras:
            cam.running = False 
        # Destroy visualization
        cv.destroyAllWindows()
        # Allow camera selection
        for c in self.cameraOptions:
            c.setEnabled(True)
        
    def cameraError(self):
        msg = QtWidgets.QMessageBox()
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Camera not selected")
        msg.setInformativeText('No cameras were selected')
        msg.setWindowTitle("Camera not selected")
        msg.exec_()

    # VISUALIZATION ------------------------
    # Resize window view
    def goUp(self):
        for cam in self.cameras:
            cam.display_zoom = cam.display_zoom * 2
    def goDown(self):
        for cam in self.cameras:
            cam.display_zoom = cam.display_zoom * 0.5

    # Shows image in main gui
    def showImg(self, bundle):
        if self.running:
            cv.imshow(*bundle)

    def toggleThresh(self):
        btn=self.threshInput.text()
        if btn =='On':
            self.threshInput.setText('Off')
            thresh = False
        else:
            self.threshInput.setText('On')
            thresh = True
        # Do not send any more images
        for cam in self.cameras:
            cam.showThresh = thresh

    dragging=False
    currentWindow = 0
    def selectWindow(self,action, x, y, flags, *userdata):
        self.currentWindow=userdata[0]

    def imageInteraction(self,action, x, y, flags, *userdata):

        index=userdata[0]
        cam=self.cameras[index]
        if action == cv.EVENT_LBUTTONDOWN:
            if not cam.recording:
                print('mouse pressed on: ', x, y)
                self.dragging = True
                cam.start_drag = (x,y)

        elif action == cv.EVENT_LBUTTONUP:
            if not cam.recording:
                print('mouse released on: ', x, y)
                cam.end_drag=(x, y)
                cam.setZoom()
                self.dragging = False
                cam.start_drag=None
                cam.end_drag=None

        
        elif action==cv.EVENT_RBUTTONUP or action==cv.EVENT_MBUTTONUP:
            print('Current area of interest ', cam.areaOfInteres)
            print('Setting ', cam.cameraName, ' areas of interest to none')
            cam.areaOfInteres=None
            print('Current area of interest ', cam.areaOfInteres)

        else:
            if self.dragging:
                cam.end_drag=(x,y)
            cam.hovering(x,y)

    def changeThreshold(self,val,thresh):
        
        cam=self.cameras[self.currentWindow]
        if thresh=='min':
            cam.lowerThresh=val
        elif thresh =='max':
            cam.higherThresh=val

    # EXPOSURE CONTROLS ------------------------
    # Takes: New value from slider
    # Void: grabber exposure changes
    def changeExposureSlider(self,val):
        self.exposureValue.setText(str(val))
        self.currentExpValue=val
        if not debugging:
            # Set grabber in camera's exposure
            self.selectedExpCamera.grabber.remote.set(self.exposureCommand, self.currentExpValue)
    
    def changeExposureText(self):
        # Get value from line input
        val =self.exposureValue.text()
        print('value changed: ', val)
        # Convert value to int 
        try:
            val=int(val)
        except:
            val = None
            print ('Value is not an int')
        
        if val is not None and self.maxExpValue >=val >= self.minExpValue and val != self.currentExpValue:
            print('new value', val)
            self.exposureInput.setValue(val)
            self.currentExpValue=val

        # Set value to accepted value (Back to last value if input not valid)
        self.exposureValue.setText(str(self.currentExpValue))
        if not debugging:
            # Set grabber in camera's exposure
            self.selectedExpCamera.grabber.remote.set(self.exposureCommand, self.currentExpValue)
        
    # Sets up exposure options in gui when a camera is selected
    def setUpExposure(self,idx):
        # Changes to -1 when options are deleted
        print('Exposure selection changed in camera: ',idx)
        if idx != -1:
            # Get command to use for specific camera
            df=pd.read_csv('cameraControls.tsv',sep='\t',index_col=0)

            # Get commands to set exposure to min and max
            if debugging:
                if idx==0:
                    vendor = 'Hikvision'
                else:
                    vendor = 'IO Industries Inc'
            else:
                # Get camera selected
                self.selectedExpCamera=self.cameras[idx]
                # Get vendor name
                vendor=self.selectedExpCamera.grabber.remote.get('DeviceVendorName')
            minCommand = df.loc[df['Command'] == 'ExposureMin', vendor].values[0]
            maxCommand = df.loc[df['Command'] == 'ExposureMax', vendor].values[0]
            self.exposureCommand = df.loc[df['Command'] == 'ExposureNow', vendor].values[0]

            # Get values to set slider
            if debugging:
                print('Getting min exposure with ',minCommand,type(minCommand))
                print('Getting max exposure with ',maxCommand,type(maxCommand))
                print('Getting current exposure with ',self.exposureCommand,type(self.exposureCommand))
                self.minExpValue = 5
                self.maxExpValue = 50
                self.currentExpValue = 8
            else:
                self.minExpValue = int(self.selectedExpCamera.grabber.remote.get(minCommand))
                self.maxExpValue = int(self.selectedExpCamera.grabber.remote.get(maxCommand))
                self.currentExpValue = int(self.selectedExpCamera.grabber.remote.get(self.exposureCommand))
                # Set grabber in camera's exposure
                self.selectedExpCamera.grabber.remote.set(self.exposureCommand, self.currentExpValue)
            # Set slider values
            self.exposureInput.setMinimum(self.minExpValue)
            self.exposureInput.setMaximum(self.maxExpValue)
            self.exposureInput.setValue(self.currentExpValue)
            # Set value in line input
            self.exposureValue.setText(str(self.currentExpValue))


    # RESOLUTION CONTROLS ------------------------
    # Selecting camera sets resolution of current camera in dropbox
    def resolutionCameraSelected(self,idx):
        # Get resolution
        self.selectedResCamera=self.cameras[idx]
        res = self.selectedResCamera.saveResolution
       
        for n in range(7): # There are 7 options for resolutions. This could be changed in code if necessary
            resolution = self.resolutionInput.itemText(n)
            if str(res) in resolution:
                self.resolutionInput.setCurrentIndex(n)
        
    # Changing dropbox value changes camera resolution
    def changeResolution(self, txt):
        if self.running:
            print('resolution changed',txt)
            val = int(txt.split()[0])
            self.selectedResCamera.saveResolution = val
            

    # VIDEO AND  IMAGES ACQUISITION  ------------------------

    def updateFPS(self,fps):
        if self.running:
            cam =self.cameras[-1]
            rate = 1000000/fps
            if not debugging:
                cam.grabber.device.set('CycleMinimumPeriod',rate)
                print('Grabber set to ', rate)
            print('FPS changed to ', fps)
        
    recording=False
    def startRecording(self):
        ('Print attempting recording')
        if not self.recording:
            print('Recording starting')
            self.recording = True
            savePath = self.saveInInput.text()
            # Get video parameters
            if savePath =='':
                savePath = str(Path.home())
                self.saveInInput.setText(savePath)
                print('Saving in: ', savePath)
            self.saveInBtn.setEnabled(False)
            self.saveInInput.setEnabled(False)
            self.videoFormatInput.setEnabled(False)
            self.fpsInput.setEnabled(False)

            expName = self.nameInput.text()
            if expName == '':
                expName = 'experiment'
                self.nameInput.setText(expName)
            print('Experiment name: ', expName)
            self.nameInput.setEnabled(False)
            expName.replace(' ','_')

            format = self.videoFormatInput.currentText()

            # Start recording
            for cam in self.cameras:
                cam.recordingStatus = 'Recording'
                cam.savePath = savePath
                cam.expName=expName
                cam.videoOutput=format
                cam.recording=True

            # Save info
            notes = self.notesInput.toPlainText()
            saveCameraInfo(self.cameras,savePath,expName,'video',notes)
        else:
            for cam in self.cameras:
                cam.recordingStatus = 'Recording'
                cam.recording=True
                cam.timer.resume()


    def pauseRecording(self):
        print('Recording paused')
        for cam in self.cameras:
            cam.recording=False
            cam.recordingStatus = 'Paused'
            cam.timer.pause()

    def stopRecording(self):
        if self.recording:
            print('Recording stop')
            for cam in self.cameras:
                cam.recording=False
                if cam.everRecorded == True:
                    cam.out.release()
                    cam.everRecorded=False
                if cam.recordingStatus != 'Paused':
                    cam.timer.pause()
                cam.recordingStatus = 'Stopped'
            self.saveInBtn.setEnabled(True)
            self.saveInInput.setEnabled(True)
            self.nameInput.setEnabled(True)
            self.videoFormatInput.setEnabled(True)
            self.fpsInput.setEnabled(True)

            self.recording=False

    def getImage(self):

        # Get parameters
        savePath = self.saveInInput.text()
        if savePath =='':
            savePath = str(Path.home())
            self.saveInInput.setText(savePath)
        
        expName = self.nameInput.text()
        if expName == '':
            expName = 'experiment'
            self.nameInput.setText(expName)

        # Iterate cameras
        format=self.pictureFormatsInput.currentText()
        print('Taking picture')
        for cam in self.cameras:
            cam.imgFormat=format
            cam.savePath = savePath
            cam.expName=expName
            cam.capturing = True 
        
        # Save info
        notes = self.notesInput.toPlainText()
        saveCameraInfo(self.cameras,savePath,expName,'img',notes)


    # SHOW INFO  ------------------------
    def visualizeInfo(self):
        if self.running:
            img =showInfo(self.cameras)
            cv.imshow('Info', img)

    # SAVE INFO  ------------------------
    # Select path where to save data
    def selectPath(self):
        # Open dialog box
        dialog = QtWidgets.QFileDialog()
        # Get directory
        filename = dialog.getExistingDirectory()
        self.saveInInput.setText(filename)

    
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CameraLayout = QtWidgets.QWidget()
    ui = Ui_CameraLayout()
    ui.setupUi(CameraLayout, None)
    CameraLayout.show()
    sys.exit(app.exec_())


