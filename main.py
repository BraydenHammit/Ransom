import tkinter as tk

root = tk.Tk()
root.title('RANSOM.EXE')
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.attributes('-fullscreen', True)
root.wm_attributes("-topmost", True)

def disable(_):
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.attributes('-fullscreen', False)
    root.wm_attributes("-topmost", False)


root.bind('<q>',disable)
root.mainloop()