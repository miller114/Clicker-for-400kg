import pyautogui as pg
import time
import numpy as np
from mss import mss


monitor = {
        "left": 404,
        "top": 236,
        "width": 1065,
        "height": 665,
}

def find_color(our_color, monitor={}):
    m = mss()

    img = m.grab(monitor)

    img_arr = np.array(img)

    our_map = (our_color[2], our_color[1], our_color[0], 255)
    indexes = np.where(np.all(img_arr == our_map, axis=-1))
    our_crd = np.transpose(indexes)
    return our_crd


our_color = [90, 104, 127]
tt = time.sleep(0.5)

while True:
    time1 = time.time()
    result = find_color(our_color, monitor)
    time2 = time.time()
    if result.__len__():
        x = result[0][1] + monitor.get('left')
        y = result[0][0] + monitor.get('top')

        pg.moveTo(x, y)

        pg.click(x, y)

