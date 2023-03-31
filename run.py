#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
:Description: CameraApp startup file

:Authors: (c) Andrea Chavez Munoz <chavezmunoz.a@northeastern.edu>, Artem Lutov <lav@lumais.com>
:Date: 2023-03
"""

import sys
import debugging
from GUImain import Ui_CameraLayout
from PyQt6 import QtCore, QtGui, QtWidgets
from camera import camNames
from helperFunctions.createGrabbers import *
from egrabber import *

# Create grabbers
grabberList = None
idx = 0
# Connect to cameras (Euresys uses grabbers)
try:
    gentl = EGenTL()
    grabberList=createGrabbers(gentl)
    # Check current cameras
    for idx, grabber in enumerate(grabberList):
        if grabber.remote is not None: # if grabber.remote is None port is empty
            # set parameters
            grabber.device.set('CxpTriggerMessageFormat', 'Pulse')
            grabber.device.set('CameraControlMethod', 'RC')
            grabber.device.set('C2CLinkConfiguration', 'Disconnected')
            device=grabber.remote.get('DeviceModelName')
            vendor=grabber.remote.get('DeviceVendorName')
            
            camNames.append(device)
            print('Camera[{}]: {} from {}'.format(idx, device, vendor))
except GenTLException as err:
    print('The grabber is not available: ' + str(err))
    if grabberList:
        grabberList = grabberList[:len(camNames)]
    debugging.debugging = True
print('{} cameras are available in the grabber'.format(idx))

    
# Open gui
if __name__ == "__main__":
    print('Starting app')
    app = QtWidgets.QApplication(sys.argv)
    CameraLayout = QtWidgets.QWidget()
    ui = Ui_CameraLayout(grabberList)
    ui.setupUi(CameraLayout)
    CameraLayout.show()
    res = app.exec()
    # Close cameras if necessary
    ui.stopCameras()
    sys.exit(res)
