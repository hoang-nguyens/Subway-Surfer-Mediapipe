import cv2 
from game import playGame
from hand_tracking import Hand
import time
import pyautogui

myGame = playGame()
cap = cv2.VideoCapture(0)

# Set resolution and frame rate
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# cap.set(cv2.CAP_PROP_FPS, 30)
#myGame.game_started = True
while True:
    start_time = time.time()
    
    ret, frame = cap.read()

    if not ret:
        break

    image = cv2.flip(frame, 1)

    image, results = myGame.hand.detectHand(image)
    
    if results.multi_hand_landmarks:
        if myGame.game_started:
            LCR = myGame.hand.LCR(image, results)
            myGame.moveLRC(LCR)
            
            JSD = myGame.hand.JSD(image, results)
            myGame.moveJSD(JSD)
            
        
        fist = myGame.hand.fist(image, results)
        if fist:
            myGame.start_duration += 1
            if myGame.start_duration >= 10:
                if myGame.game_started:
                    # myGame.position_x = 0
                    # myGame.position_y = 0
                    # pyautogui.press('space')
                    pass
                else:
                    myGame.game_started = True
                    print('Game started')
                myGame.start_duration = 0
        else:
            myGame.start_duration = 0  # Reset if no fist detected

    cv2.imshow("Playing game", image)
    
    # Limit frame rate
    elapsed_time = time.time() - start_time
    delay = max(1.0 / 30 - elapsed_time, 0)  # 30 FPS
    time.sleep(delay)

    if cv2.waitKey(1) & 0xFF == ord('d'):
        break

cap.release()
cv2.destroyAllWindows()
