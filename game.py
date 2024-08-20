import mediapipe as mp
import pyautogui 
from hand_tracking import Hand
class playGame():
    def __init__(self):
        self.hand = Hand()
        self.game_started = False
        self.position_x = 0 # -1 is left, 0 is center, 1 is right
        self.position_y = 0 # -1 is down, 0 is standing, 1 is jumping
        self.start_duration = 0

    def moveLRC(self, LRC):
        if self.position_x == 0:
            if LRC == 'L':
                pyautogui.press('left')
                print('left')
                self.position_x = -1
            if LRC == 'R':
                pyautogui.press('right')
                print('right')
                self.position_x = 1

        elif self.position_x == -1:
            if LRC == 'R':
                pyautogui.press('right')
                print('right')
                self.position_x = 0

        elif  self.position_x == 1:
            if LRC == 'L':
                pyautogui.press('left')
                print('right')
                self.position_x = 0
        return
    
    def moveJSD(self, JSD):
        
        if JSD == 'D':
            if self.position_y == 0 or self.position_y == 1:
                pyautogui.press('down')
                print('down')
                self.position_y = -1
        elif JSD == "J":
            if self.position_y == 0 or self.position_y == -1:
                pyautogui.press('up')
                print('up')
                self.position_y = 1
        elif JSD == 'S':
            print('stand')
            self.position_y = 0
        return

    


