from tkinter import *
import argparse
import subprocess

def retrain(event):
	print("hello world")
	subprocess.call("./retrain.py", shell="True")
	print("done")

root = Tk()
label = Label(root, text="Hello World")
label.pack()

retrainButton = Button(root, text="Retrain")

retrainButton.pack()
retrainButton.bind('<Button-1>', retrain)

root.mainloop()
