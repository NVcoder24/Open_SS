# Open_SS
Open ScreenShoter<br>
a program that makes screenshotes (open source)

## libraries (PIP)
```
pip install Pillow
pip install pyautogui
pip install pynput
pip install numpy
```

## config file
```python
from pynput.keyboard import Key

config = {
    "base_file_name":"Screenshot_{0}",   # must have {0}
    "base_file_type":".png",             # for example .png
    "cut_ss_btn":Key.print_screen,       # for example Key.print_screen
    "ss_btn":Key.scroll_lock,            # for example Key.scroll_lock
    "key_debug":False,                   # keys debugging
    "show_image":False,                  # show screenshot after taking it
}
```
