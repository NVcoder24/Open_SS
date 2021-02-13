# some libraries
import pyautogui                     # to take screenshots
from pynput import mouse, keyboard   # user input tracking
from pynput.keyboard import Key      # pynput special keyboard keys
import numpy as np                   # working with huge arrays of data
from PIL import Image                # working with images
from threading import Thread         # multiprocessing and other stuff
import os                            # system commands
from cfg import config               # config

while(True):
    pos1 = None
    pos2 = None

    # open folder with screenshot
    def open_dir():
        if config["open_folder"] == True:
            os.startfile(os.path.dirname(os.path.abspath(__file__)))

    def get_file_name():
        path = os.path.dirname(os.path.abspath(__file__))
        file_base = config["base_file_name"]
        file_type = config["base_file_type"]
        i=1
        while(True):
            name = file_base.format(str(i))+file_type
            is_exist = os.path.exists(f"{path}/{name}")
            if is_exist == True:
                i = i + 1
            else:
                break
        return name

    # get first mouse position
    def on_click1(x, y, button, pressed):
        # some globals
        global pos1
        pos1 = (x, y)
        # if not released
        if not pressed:
            return False

    # get second mouse position
    def on_click2(x, y, button, pressed):
        # some globals
        global pos2
        pos2 = (x, y)
        # if not released
        if not pressed:
            return False

    # def for taking screenshot
    def take_ss():
        return pyautogui.screenshot()

    def ss():
        # takes screenshot
        image = take_ss()

        # save and opening image
        image.save(get_file_name())
        open_dir()
        if config["show_image"] == True:
            Thread(target=image.show).start()  # opening image in new thread

    # screenshot with cut
    def cut_ss():
        # mouse positions
        global pos1
        global pos2

        # start listening
        with mouse.Listener(on_click=on_click1) as listener:
            listener.join()

        # start listening
        with mouse.Listener(on_click=on_click2) as listener:
            listener.join()

        # writing indent ints from tuples
        pos1_  = pos1[0]
        pos1__ = pos1[1]
        pos2_  = pos2[0]
        pos2__ = pos2[1]

        # if user throw first pos as second (to prevent app crash)
        if pos1_ > pos2_ and pos1__ > pos2__:
            # processing positions
            pos1_p  = pos2_
            pos1__p = pos2__
            pos2_p  = pos1_
            pos2__p = pos1__

            # writing positions
            pos1_ = pos1_p
            pos1__ = pos1__p
            pos2_ = pos2_p
            pos2__ = pos2__p

        # takes screenshot
        image = take_ss()

        # cut image (stackoverflow)
        crop_rectangle = (pos1_, pos1__, pos2_, pos2__)
        cropped_image = image.crop(crop_rectangle)

        # save and opening image
        cropped_image.save(get_file_name())
        open_dir()
        if config["show_image"] == True:
            Thread(target=cropped_image.show).start()  # opening image in new thread

    def on_press(key):
        if config["key_debug"] == True:
            print(key)

        if key == config["cut_ss_btn"]:
            cut_ss()
        elif key == config["ss_btn"]:
            ss()

        return False

    with keyboard.Listener(
            on_press=on_press,) as listener:
        listener.join()
