import subprocess
import sys
import importlib

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3.x!")

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "FinalRecon/requirements.txt"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "LittleBrother/requirements.txt"])

import tkinter

if tkinter is None:
    print("You need to install tkinter for the GUI to work properly!")
    print("See https://tkdocs.com/tutorial/install.html")
