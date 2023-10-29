import cv2
import os

colorList = []

cap = cv2.VideoCapture(0)
##cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
##cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

def getColor(squareColor):

        hue_value = squareColor[0]
        global color

        color = "Undefined"
        if squareColor[1]<100 and squareColor[2] >150:
            color = "w"
        ##elif hue_value < 8:
            ##color = "r"
        elif hue_value < 22:
            color = "o"
        elif hue_value < 40:
            color = "y"
        elif hue_value < 78:
            color = "g"
        elif hue_value < 131:
            color = "b"
        elif hue_value < 200:
            color = "r"
        else:
            color = "ERROR"
            print("ERROR")

        print(squareColor)
        return(color)
        
        ##pixel_center_bgr = frame[550, 450]

        ##b, g, r = int(pixel_center_bgr[0]), int(pixel_center_bgr[1]), int(pixel_center_bgr[2])
    


def scanSide(key):
    if key == 32:
        #3
        squareColor = hsv_frame[250,750]
        colorList.append(getColor(squareColor))
        
        #2
        squareColor = hsv_frame[250,650]
        colorList.append(getColor(squareColor))

        #1
        squareColor = hsv_frame[250,550]
        colorList.append(getColor(squareColor))

        #6
        squareColor = hsv_frame[350,750]
        colorList.append(getColor(squareColor))

        #5
        squareColor = hsv_frame[350,650]
        colorList.append(getColor(squareColor))

        #4
        squareColor = hsv_frame[350,550]
        colorList.append(getColor(squareColor))

        #9
        squareColor = hsv_frame[450,750]
        colorList.append(getColor(squareColor))

        #8
        squareColor = hsv_frame[450,650]
        colorList.append(getColor(squareColor))

        #7
        squareColor = hsv_frame[450,550]
        colorList.append(getColor(squareColor))
        

        cv2.putText(frame, "side scanned", (200, 100), 0, 3, (255, 255,0), 5)
        print("SIDE SCANNED")
        print(colorList)
        return(colorList)

print("scan order is: YELLOW, BLUE, RED, GREEN, ORGANGE, WHITE")
while True:
    key = cv2.waitKey(30) 
    ret, frame = cap.read()
    frame = cv2.flip(frame,1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    height, width, _ = frame.shape

    # Pick pixel value
    
    ##pixel_center = hsv_frame[cy, cx]

    cv2.putText(frame, "space to scan", (600, 100), 0, 3, (255, 255, 0), 5)


    
    scanSide(key)
    


    ##cv2.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)


    ##drawing frames
    cv2.rectangle(frame, (500,500), (600,400), (0,255, 0), 7)
    cv2.rectangle(frame, (600,500), (700,400), (0,255, 0), 7)
    cv2.rectangle(frame, (700,300), (800,200), (0,255, 0), 7)

    cv2.rectangle(frame, (500,300), (600,200), (0,255, 0), 7)
    cv2.rectangle(frame, (700,500), (800,400), (0,255, 0), 7)
    cv2.rectangle(frame, (700,400), (800,300), (0,255, 0), 7)

    cv2.rectangle(frame, (600,300), (700,200), (0,255, 0), 7)
    cv2.rectangle(frame, (500,400), (600,300), (0,255, 0), 7)
    cv2.rectangle(frame, (600,400), (700,300), (0,255, 0), 7)

    ##cv2.putText(frame, color, (x7 - 200, 100), 0, 3, (b, g, r), 5)
    ##cv2.circle(frame, (x7, y7), 5, (25, 25, 25), 3)

    finalList = "".join(colorList)
    cv2.imshow("Frame", frame)

    if key == 27:
        os.system("rubik_solver -i " + finalList + " -s Kociemba")
        break
    elif key == 97:
        print("last scan deleted")
        del colorList[-9:]
        print("updated list:", colorList)

    elif "ERROR" in colorList:
        print("error in scanning, please try again")
        del colorList[-9:]
    ##elif key != -1:
      ##  print(key)

    
    ##print("rubik_solver -i " + finalList + " -s Kociemba")
    
obyryggybwbyobbbggrbowrowrywyowgyogybogroyrgwrwgrwwrob

yyyyyyybbbbrbbbrybgrrwrrwrryggggggggoooooooobowwrwwwww
