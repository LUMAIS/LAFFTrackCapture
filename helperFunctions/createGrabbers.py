
from egrabber import *

def createGrabbers(gentl):
    grabbers = []
    for streamIndex in range(4):
        try:
            grabbers.append(EGrabber(gentl, 0, streamIndex, remote_required=False))
        except:
            break
    return grabbers

# def show(index, portname, name, getter):
#     print('grabber[{}].{}.{} = {}'.format(index, portname, name, getter(name)))

# def showGrabbers(grabbers):
#     for (index, grabber) in enumerate(grabbers):
#         # show(index, 'InterfacePort', 'InterfaceID', grabber.interface.get) --- All cameras have the same interface: PC1633 - Coaxlink Quad G3 (4-camera) - KQG13495
#         # show(index, 'DevicePort', 'DeviceID', grabber.device.get) -> device(index)
#         if grabber.remote is not None: # if grabber.remote is None port is empty
#             show(index, 'RemotePort', 'DeviceVendorName', grabber.remote.get)
#             show(index, 'RemotePort', 'DeviceModelName', grabber.remote.get)
