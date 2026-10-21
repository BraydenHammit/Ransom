import tkinter as tk

root = tk.Tk()
root.title('RANSOM.EXE')
root.protocol("WM_DELETE_WINDOW", lambda: None)
#root.attributes('-fullscreen', True)
root.config(bg='#E51A1A')
root.wm_attributes("-topmost", True)
try:root.attributes('-toolwindow', True)
except: None

images = {
    'a90': tk.PhotoImage(file='ext/a90.png')
}

def disable(_):
    root.protocol("WM_DELETE_WINDOW", root.destroy)
    #root.attributes('-fullscreen', False)
    root.wm_attributes("-topmost", False)
    try:root.attributes('-toolwindow', False)
    except:None

def mouse(event):
    root.update_idletasks()
    x = root.winfo_rootx()
    y = root.winfo_rooty()
    w = root.winfo_width()
    h = root.winfo_height()
    mx = root.winfo_pointerx()
    my = root.winfo_pointery()
    if not (x <= mx <= x + w and y <= my <= y + h):
        windex = w // 2
        windey = h // 2
        root.event_generate("<Motion>", warp=True, x=x + windex, y=y + windey)
    root.event_generate("<Motion>", warp=True, x=windex, y=windey)

topframe = tk.Frame(root,bg='#E51A1A',borderwidth=0,highlightthickness=0)
ransom = tk.Label(topframe,image=images['a90'],bg='black',borderwidth=0,highlightthickness=0)
txt1 = tk.Label(topframe,text='YOUR ITEMS\nHAVE BEEN\nENCRYPTED',font=('Helvetica Bold',40,"bold"),bg='#E51A1A',fg='white')
midframe = tk.Frame(root,bg='#000000',highlightcolor='white',highlightthickness=2)
txt2 = tk.Label(midframe,text='IF YOU DO NOT PAY THIS RANSOM BEFORE\nTHE TIMER ENDS, YOUR ITEMS WILL BE',font=('Helvetica Bold',20,'bold'),bg='#000000',fg='white')
txt3 = tk.Label(midframe,text='UNRECOVERABLE BY ANY MEANS.',font=('Helvetica Bold',20,'bold'),bg='#000000',fg='red')
bttmframe = tk.Frame(root,bg='#E51A1A',borderwidth=0,highlightthickness=0)

topframe.pack()
ransom.pack(side=tk.LEFT)
txt1.pack(side=tk.RIGHT,padx=20)
midframe.pack(pady=10)
txt2.pack()
txt3.pack()
root.bind('<q>',disable)
root.bind("<Leave>", mouse)
root.mainloop()