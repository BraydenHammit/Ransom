import tkinter as tk

def run():
    root = tk.Tk()
    root.title('RANSOM.EXE')
    root.protocol("WM_DELETE_WINDOW", lambda: None)
    #root.attributes('-fullscreen', True)
    root.config(bg='#E51A1A')
    root.wm_attributes("-topmost", True)
    try:root.attributes('-toolwindow', True)
    except: None

    timeM = 1
    timeS = 30
    remgold = 500
    images = {
        'a90': tk.PhotoImage(file='ext/a90.png'),
        'gold': tk.PhotoImage(file='ext/gold.png').subsample(3,3)
    }

    def disable(_):
        root.protocol("WM_DELETE_WINDOW", root.destroy)
        #root.attributes('-fullscreen', False)
        root.wm_attributes("-topmost", False)
        try:root.attributes('-toolwindow', False)
        except:None

    def gold():
        global remgold
        remgold -= 1
        if remgold < 10:
            goldam.configure(text=f'00{remgold}')
        elif remgold < 100:
            goldam.configure(text=f'0{remgold}')
        else:
            goldam.configure(text=remgold)
        if remgold <= 0:
            win()

    def time():
        global timeM, timeS
        if (timeM <= 0) and (timeS <= 0):
            jumpscare()
        else:
            timeS -= 1
            if timeS == -1:
                timeM -= 1
                timeS = 59
            if timeS < 10:
                timer.configure(text=f'TIME:    {timeM}:0{timeS}')
            else:
                timer.configure(text=f'TIME:    {timeM}:{timeS}')
            root.after(1000,time)

    def jumpscare():
        root.destroy()

    def win():
        root.destroy()

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

    topframe = tk.Frame(root,bg='#E51A1A',borderwidth=0,highlightthickness=0)
    ransom = tk.Label(topframe,image=images['a90'],bg='black',borderwidth=0,highlightthickness=0)
    txt1 = tk.Label(topframe,text='YOUR FILES\nHAVE BEEN\nENCRYPTED',font=('Helvetica Bold',40,"bold"),bg='#E51A1A',fg='white')
    midframe = tk.Frame(root,bg='#000000',highlightcolor='white',highlightthickness=2)
    txt2 = tk.Label(midframe,text='IF YOU DO NOT PAY THIS RANSOM BEFORE\nTHE TIMER ENDS, YOUR FILES WILL BE',font=('Helvetica Bold',20,'bold'),bg='#000000',fg='white')
    txt3 = tk.Label(midframe,text='UNRECOVERABLE BY ANY MEANS.',font=('Helvetica Bold',20,'bold'),bg='#000000',fg='red')
    bttmframe = tk.Frame(root,bg='#E51A1A',borderwidth=0,highlightthickness=0)
    goldframe = tk.Frame(bttmframe,bg='#000000',highlightcolor='yellow',highlightthickness=2)
    goldam = tk.Label(goldframe,fg='yellow',bg="#000000",text=remgold,font=('Helvetica Bold',30,"bold"))
    goldbt = tk.Button(goldframe,command=gold,image=images['gold'],bg="#000000",borderwidth=0,highlightthickness=0)
    timer = tk.Label(bttmframe,fg='black',bg="#FA0000",text=f'TIME:    {timeM}:{timeS}',font=('Helvetica Bold',30,"bold"),highlightcolor='black',highlightthickness=2)

    topframe.pack()
    ransom.pack(side=tk.LEFT)
    txt1.pack(side=tk.RIGHT,padx=20)
    midframe.pack(pady=10)
    txt2.pack()
    txt3.pack()
    bttmframe.pack(pady=10)
    goldframe.pack(side=tk.LEFT)
    goldam.pack(side=tk.LEFT)
    goldbt.pack(side=tk.RIGHT)
    timer.pack(side=tk.RIGHT,padx=20)
    root.bind('<q>',disable)
    root.bind("<Leave>", mouse)
    root.after(1000,time)
    root.mainloop()