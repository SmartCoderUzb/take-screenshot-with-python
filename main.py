import cv2
import pyautogui
import numpy as np
cv2.imwrite("new.png", np.array(pyautogui.screenshot()))
