
import sys
print('PATH: ',sys.path)
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
            print('Camera[{}]: {} from {}'.format(idx,grabber.remote.get('DeviceModelName'),grabber.remote.get('DeviceVendorName')))

    
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
