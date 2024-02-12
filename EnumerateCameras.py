import cv2

# Source:
# How to Detect Objects in Real-Time Using OpenCV and Python
# https://towardsdatascience.com/how-to-detect-objects-in-real-time-using-opencv-and-python-c1ba0c2c69c0

# Enable camera
for i in range(-100,100):
    cap = cv2.VideoCapture(0)
    cap.set(3, 640)
    cap.set(4, 420)

    # import cascade file for facial recognition
    faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

    '''
        # if you want to detect any object for example eyes, use one more layer of classifier as below:
        eyeCascade = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_eye_tree_eyeglasses.xml")
    '''
    success, img = cap.read()
    # TRY:
    try:
        imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except:
        print(str(i) + " threw exception", file=open('EnumerateCamerasOutput.txt', 'a'))
    print(str(i) + " is " + str(success), file=open('EnumerateCamerasOutput.txt', 'a'))