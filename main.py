import tkinter as tk

root = tk.Tk()
root.title('RANSOM.EXE')
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.attributes('-fullscreen', True)
root.wm_attributes("-topmost", True)
try:root.attributes('-toolwindow', True)
except: None

def disable(_):
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.attributes('-fullscreen', False)
    root.wm_attributes("-topmost", False)
    try:root.attributes('-toolwindow', False)
    except:None

root.bind('<q>',disable)
root.mainloop()