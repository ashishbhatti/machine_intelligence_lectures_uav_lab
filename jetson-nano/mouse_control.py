'''
Author: Ashish Kumar
Date: Nov 17, 2023
Place: UAV Lab, IIT Kanpur
'''

'''
This file contains the necessary auxiliary functions to be used in other code.
'''


# This library is good for controlling, but not good for monitoring
import pyautogui as pgui


def mouse_coordinate():
    '''
    Print the coordinate of  the point which the mouse is currently on.
    '''
    try:
        while True:
            x, y = pgui.position()
            print("Mouse coordinates: x = {}, y = {}".format(x, y))
    except KeyboardInterrupt:
        print("Mouse coordinate capturing stopped.")

if __name__ == "__main__":
    mouse_coordinate()