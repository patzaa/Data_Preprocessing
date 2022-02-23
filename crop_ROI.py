import cv2
import numpy as np
import os 


#dataset path
PATH = "/media/dan/Samsung USB/Litzen_Dataset"

PATHSAVETO = "/media/dan/Samsung USB/Litzen_Dataset_cropped/"

#read sample image to crop
img_raw = cv2.imread(PATH + '/Basler_a2A5328-4gcPRO__40171598__20220221_090708089_0000.tiff')

#Precrop for better ROI detection
img_crop = img_raw[2000:4000, 1000:4000]

#select ROI function
roi = cv2.selectROI(img_crop)

#print rectangle points of selected roi
print(roi)

#Crop selected roi from raw image
roi_cropped = img_crop[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

#show cropped image
cv2.imshow("ROI", roi_cropped)


#Save cropped image
cv2.imwrite(os.path.join(PATHSAVETO, "Litze_crop" + '_0' + ".jpeg"),roi_cropped)


for i, filename in enumerate(os.listdir(PATH)):
    
    img_raw = cv2.imread(PATH + "/" + filename)
    img_crop = img_raw[2000:4000, 1000:4000]
    #Crop selected roi from raw image
    roi_cropped = img_crop[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]

    #Save cropped image
    current_image = os.path.join(PATHSAVETO, "Litze_crop" + str(i) + ".jpeg")
    cv2.imwrite(current_image,roi_cropped)

    print(f'croping image: {i}')

#hold window
cv2.waitKey(0)