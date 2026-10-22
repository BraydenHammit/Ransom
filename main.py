import tkinter as tk
import random as ran
import time as t
from code import run

def okey(tf):
    global ok
    ok = tf
    root.destroy()

root = tk.Tk()
root.title('Warning / Disclaimer')
ok = False
txt = tk.Label(root,text='Warning:\nPressing Ok will partially lock your device.\nNo damage is caused by running this program.\n\n\nDiscalimer:\nThis is NOT actual ransomware, and is only based\non a character from the Roblox game "Doors".')
okbutton = tk.Button(root,text='Ok',command=lambda:okey(True))
nokbutton = tk.Button(root,text='No-k',command=lambda:okey(False))
txt.pack(pady=20)
okbutton.pack()
nokbutton.pack()
root.mainloop()

if ok == True:
    while True:
        run()
        t.sleep(ran.randint(30,300))