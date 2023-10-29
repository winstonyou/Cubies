
'''
import pycuber as pc

# Create a Cube object
mycube = pc.Cube()

# Do something at the cube.
mycube("B")

print(mycube)
'''

import imghdr
import cv2
import numpy as np
import matplotlib.pyplot as plt
##img = cv2.imread(r"/Users/Winston/Rubik's Cube.jpeg", cv2.IMREAD_COLOR)
##cv2.imshow('image', img)

'''
image = cv2.imread(r"/Users/Winston/Rubik's Cube.jpeg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred = cv2.GaussianBlur(gray, (3, 3), 0)
canny = cv2.Canny(blurred, 20, 40)
kernel = np.ones((3,3), np.uint8)
dilated = cv2.dilate(canny, kernel, iterations=2)


cv2.imshow('image', dilated)

cv2.waitKey(0)
cv2.destroyAllWindows()
'''

'''
##img = cv2.imread(r"/Users/Winston/Rubik's Cube.jpeg")
img = cv2.imread(r"/Users/Winston/istockphoto-1196286693-612x612.jpeg")
original = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

ROI_number = 0
cnts = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
cnts = cnts[0] if len(cnts) == 2 else cnts[1]
for cnt in cnts:
    approx = cv2.approxPolyDP(cnt,0.01*cv2.arcLength(cnt,True),True)


cv2.imshow('image', img)
cv2.imshow('Binary',thresh)
cv2.waitKey()
'''

import cv2
##image = cv2.imread(r"/Users/Winston/Downloads/testing pic.png")
image = cv2.imread(r"/Users/Winston/Rubik's Cube.jpeg")
##image = cv2.imread(r"/Users/Winston/istockphoto-1196286693-612x612.jpeg")

cap = cv2.VideoCapture(0)

while True:
    ret, image = cap.read()
    image = cv2.flip(image,1)
    ##image = cv2.blur(image, (5,5))

    ##convert image into greyscale mode
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    #find threshold of the image
    thrash = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]
    ##thrash = cv2.adaptiveThreshold(gray_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY,3,2)
    contours, _ = cv2.findContours(thrash, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)


    for contour in contours:
        shape = cv2.approxPolyDP(contour, 0.01*cv2.arcLength(contour, True), True)
        x_cor = shape.ravel()[0]
        y_cor = shape.ravel()[1]
        

        if len(shape) ==4:
            #shape cordinates
            x,y,w,h = cv2.boundingRect(shape)

            #width:height
            aspectRatio = float(w)/h
            if w and h >100:
                cv2.drawContours(image, [shape], 0, (0,255,0), 4)
                if aspectRatio >= 0.9 and aspectRatio <=1.1:
                    cv2.putText(image, "Square", (x_cor, y_cor), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0,0,0))
            ##else:
                ##cv2.putText(image, "Rectangle", (x_cor, y_cor), cv2.FONT_HERSHEY_COMPLEX, 0.5, (255,0,0))
            
    cv2.imshow("Shape", image)
    if cv2.waitKey(1) == 27:
        break
image.release()
cv2.destroyAllWindows()
