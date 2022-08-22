import cv2

video = 'media/experiment1_Victorem_262G41MCX_from_IO_Industries_Inc.mp4'
cap = cv2.VideoCapture(video)


ret, img = cap.read()

image_path = video.split('.')[0]+'.png'
img = cv2.imwrite(image_path,img)