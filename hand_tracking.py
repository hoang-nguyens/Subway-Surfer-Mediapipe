import mediapipe as mp
import cv2



class Hand():
    def __init__(self):
        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands()
        self.mpDraw = mp.solutions.drawing_utils
        self.mpDrawStye = mp.solutions.drawing_styles

    def detectHand(self, image):

        imgRGB = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        results = self.hands.process(imgRGB)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                self.mpDraw.draw_landmarks(
                    imgRGB,
                    hand_landmarks,
                    self.mpHands.HAND_CONNECTIONS,
                    self.mpDrawStye.get_default_hand_landmarks_style(),
                    self.mpDrawStye.get_default_hand_connections_style()
                    
                )
        return imgRGB, results
    
    def LCR(self, image, results):
        img_height, img_width, _ = image.shape
        img_mid_width = img_width // 2

        hand_landmark = results.multi_hand_landmarks[0]
        thump_tip = int(hand_landmark.landmark[self.mpHands.HandLandmark.THUMB_TIP].x * img_width)
        pinky_tip = int(hand_landmark.landmark[self.mpHands.HandLandmark.PINKY_TIP].x * img_width)

        if pinky_tip > img_mid_width:
            LRC = "R" # right
        elif thump_tip < img_mid_width:
            LRC = "L" # left
        else:
            LRC = "C" # center

        return LRC
    
    def JSD(self, img, results):
        img_height, img_width, _ = img.shape
        img_mid_height = img_height // 2

        hand_landmark = results.multi_hand_landmarks[0]

        wrist = int(hand_landmark.landmark[self.mpHands.HandLandmark.WRIST].y * img_height)
        middle_finger_tip = int(hand_landmark.landmark[self.mpHands.HandLandmark.MIDDLE_FINGER_TIP].y * img_height)

        if wrist <= img_mid_height:
            JSD = "J"
        elif middle_finger_tip > img_mid_height:
            JSD = "D"
        else:
            JSD = "S"
        
        return JSD
    
    def fist(self, img, results):
        img_height, img_width, _ = img.shape
        

        hand_landmark = results.multi_hand_landmarks[0]

        middle_finger_tip = int(hand_landmark.landmark[self.mpHands.HandLandmark.MIDDLE_FINGER_TIP].y * img_height)
        middle_finger_dip = int(hand_landmark.landmark[self.mpHands.HandLandmark.MIDDLE_FINGER_DIP].y * img_height)

        is_fist = False
        if middle_finger_tip < middle_finger_dip:
            is_fist = True
        
        return is_fist
    