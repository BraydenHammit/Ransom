import tkinter as tk

root = tk.Tk()
root.title('RANSOM.EXE')
root.protocol("WM_DELETE_WINDOW", lambda: None)
root.attributes('-fullscreen', True)
root.config(bg='#E51A1A')
root.wm_attributes("-topmost", True)
try:root.attributes('-toolwindow', True)
except: None

images = {
    'a90': tk.PhotoImage(file='ext/a90.png')
}

def disable(_):
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    root.attributes('-fullscreen', False)
    root.wm_attributes("-topmost", False)
    try:root.attributes('-toolwindow', False)
    except:None

topframe = tk.Frame(root,bg='#E51A1A',borderwidth=0,highlightthickness=0)
ransom = tk.Label(topframe,image=images['a90'],bg='black',borderwidth=0,highlightthickness=0)
txt1 = tk.Label(topframe,text='YOUR ITEMS\nHAVE BEEN\nENCRYPTED',font=('Helvetica Bold',40),bg='#E51A1A',fg='white')
midframe = tk.Frame(root,bg='#000000',highlightcolor='white')

topframe.pack()
ransom.pack(side=tk.LEFT)
txt1.pack(side=tk.RIGHT,padx=20)
midframe.pack(pady=10)
root.bind('<q>',disable)
root.mainloop()