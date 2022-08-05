
import sys
from GUImain import Ui_CameraLayout
from PyQt5 import QtCore, QtGui, QtWidgets
from debugging import debugging

# Create grabbers
if debugging:grabberList=None   
else:
    from helperFunctions.createGrabbers import *
    from egrabber import *
    # Connect to cameras (Euresys uses grabbers)
    gentl = EGenTL()
    grabberList=createGrabbers(gentl)
    # Check current cameras
    print('Cameras created')
    for idx,grabber in enumerate(grabberList):
        if grabber.remote is not None: # if grabber.remote is None port is empty
            # set parameters
            grabber.device.set('CxpTriggerMessageFormat', 'Pulse')
            grabber.device.set('CameraControlMethod', 'RC')
            device=grabber.remote.get('DeviceModelName')
            vendor=grabber.remote.get('DeviceVendorName')
            
            print('Camera[{}]: {} from {}'.format(idx,device,vendor))

    
# Open gui
if __name__ == "__main__":
    import sys
    print('Starting app')
    app = QtWidgets.QApplication(sys.argv)
    CameraLayout = QtWidgets.QWidget()
    ui = Ui_CameraLayout()
    ui.setupUi(CameraLayout,grabberList)
    CameraLayout.show()
    sys.exit(app.exec_())
