import subprocess
import sys
import importlib

if sys.version_info[0] < 3:
    raise Exception("Must be using Python 3.x!")

subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "FinalRecon/requirements.txt"])
subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "LittleBrother/requirements.txt"])

found = False
if sys.version_info[1] < 4:
    spam_loader = importlib.find_loader('tkinter')
    found = spam_loader is not None
else:
    spam_spec = importlib.util.find_spec("spam")
    found = spam_spec is not None

if not found:
    print("You need to install tkinter for the GUI to work properly!")
    print("See https://tkdocs.com/tutorial/install.html")
