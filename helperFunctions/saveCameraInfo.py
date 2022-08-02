import pandas as pd
from datetime import datetime
from helperFunctions.createFile import createFile
from debugging import debugging

def saveCameraInfo(cameraList,saveIn,expName,inputType,otherNotes):
    # Get data
    columnNames=[]
    values = []
    for cam in cameraList:
        if len(values)==0:
            # Current date time in local system
            columnNames.append('Experiment name')
            values.append(cam.expName)
            columnNames.append('Date')
            values.append(datetime.now())
            # Get other parameters information
            columnNames.append('Other notes')
            values.append(otherNotes)
        # Data for specific camera
        camName=cam.cameraName

        # Get exposure
        df=pd.read_csv('cameraControls.tsv',sep='\t',index_col=0)
        if debugging:
            exp = 10
        else:
            vendor=cam.grabber.remote.get('DeviceVendorName')
            exposureCommand = df.loc[df['Command'] == 'ExposureNow', vendor].values[0]
            exp=cam.grabber.remote.get(exposureCommand)
        
        columnNames.append('Camera exposure:'+camName)
        values.append(exp)

        # Get other data
        columnNames.append('Output resolution (height px):'+camName)
        values.append(cam.saveResolution )

        if inputType=='video':
            columnNames.append('Video format:'+camName)
            values.append(cam.videoOutput)
            columnNames.append('Encoded fps:'+camName)
            values.append(cam.fps)
        else:
            columnNames.append('Picture format:'+camName)
            values.append(cam.imgFormat)

    # Save data
    data = {'Description':columnNames, 'Values':values}
    df2 = pd.DataFrame(data)
    fileName=expName+'_'+inputType+'_SetUp'
    name = createFile(saveIn,fileName,'tsv')
    df2.to_csv(name, sep="\t")

    
    
