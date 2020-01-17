import platform
import tkinter as tk
import subprocess
import sys
import os

window = tk.Tk()
window.title("Osint multi-tools")
window.configure(background="white")
window.geometry("300x100")

if platform.system() == "Windows":
    tk.Button(window, text="FinalRecon", command=lambda:
              subprocess.Popen("{} finalrecon_gui.py".format(sys.executable), cwd=os.path.join(os.getcwd(), "FinalRecon"), creationflags=subprocess.CREATE_NEW_CONSOLE)).pack()

    tk.Button(window, text="LittleBrother", command=lambda:
              subprocess.Popen("{} LittleBrother.pyw".format(sys.executable), cwd=os.path.join(os.getcwd(), "LittleBrother"))).pack()
else:
    tk.Button(window, text="FinalRecon", command=lambda:
              subprocess.Popen("{} finalrecon_gui.py".format(sys.executable), cwd=os.path.join(os.getcwd(), "FinalRecon"), shell=True)).pack()

    tk.Button(window, text="LittleBrother", command=lambda:
              subprocess.Popen("{} LittleBrother.pyw".format(sys.executable), cwd=os.path.join(os.getcwd(), "LittleBrother"), shell=True)).pack()


window.mainloop()
