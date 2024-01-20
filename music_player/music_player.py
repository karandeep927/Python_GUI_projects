from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
from tkinter import *
from tkinter.filedialog import askopenfile
from tkinter.ttk import *
from pygame import mixer
from PIL import ImageTk, Image
import audioread


BG = "#000066"
FG = "#fff"

def about():
    about_win = Toplevel(root)
    about_win.geometry("300x200")
    about_win.resizable(0,0)
    Label(about_win,text="Music Player",font=("arial",30,"bold")).grid(row=0,column=0,columnspan=3)
    Label(about_win,text="Created by :- @karandeep927\n version 1.0",font=("arial",10,"bold")).grid(row=2,column=1)
    
def play_pause():
    playing = mixer.music.get_busy()
    if playing:
        play_btn.config(text="Play")
        mixer.music.pause()
    else:
        mixer.music.unpause()
        play_btn.config(text="Pause")
        start()

def replay():
    mixer.music.play()
    start()

def start():
    if mixer.music.get_busy():
        current_position = mixer.music.get_pos() / 1000  # Get current playback position in seconds
        progress_rate = (current_position / music_duration) * 100  # Calculate progress percentage
        progress['value'] = progress_rate
        play_time.config(text=f"{int(current_position // 60)}:{int(current_position % 60)}")
        total_play_time.config(text=f"{int(music_duration // 60)}:{int(music_duration % 60)}")
        root.after(1000, start)

def open_media():
    #choosing music and enabling buttons
    loc = askopenfile()
    if loc != "":
        play_btn.config(state=ACTIVE,text="Pause")
        volume_up_btn.config(state=ACTIVE)
        volume_down_btn.config(state=ACTIVE)
        mute_btn.config(state=ACTIVE)
        
    
    mixer.music.load(str(loc.name)) 
    mixer.music.set_volume(0.3)
    mixer.music.play()
    
    #getting the duration of the music
    with audioread.audio_open(loc.name) as f: 
        global music_duration 
        music_duration = f.duration
    start()

def create_menubar():
    menubar = Menu(root) 
    # Adding File Menu and commands 
    file = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Media', menu = file) 
    file.add_command(label ='Open File', command = open_media) 
    file.add_separator() 
    file.add_command(label ='Exit', command = root.destroy) 

    edit = Menu(menubar, tearoff = 0)
    menubar.add_cascade(label ='Playback', menu = edit) 
    edit.add_command(label ='Play', command = play_pause) 
    edit.add_command(label ='Pause', command = play_pause) 
    edit.add_command(label ='Replay', command = replay) 
    edit.add_command(label ='volume up', command = volume_up) 
    edit.add_command(label ='volume down', command = volume_down) 
    edit.add_command(label ='Mute', command = mute) 
    
    help_ = Menu(menubar, tearoff = 0) 
    menubar.add_cascade(label ='Help', menu = help_) 
    help_.add_command(label ='About', command = about) 
    help_.add_command(label ='Version 1.0', command = None) 

    root.config(menu = menubar)

def move_forward():
    current_pos = mixer.music.get_pos()
    mixer.music.set_pos(current_pos + 5000)
    play_pause()
    start()

def volume_up():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(current_volume + 0.1, None)
    except:
        print("volume is high")

def volume_down():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(current_volume - 0.1, None)
    except:
        print("volume is low")

def mute():
    try:
        devices = AudioUtilities.GetSpeakers()
        interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
        volume = cast(interface, POINTER(IAudioEndpointVolume))
        current_volume = volume.GetMasterVolumeLevelScalar()
        volume.SetMasterVolumeLevelScalar(0.0, None)
    except:
        print("volume is muted")

root = Tk()
root.title("Music Player")
root.geometry('500x300+400+200')
root.resizable(0,0)
root.configure(background=BG)
create_menubar()
mixer.init()

#adding background
img = ImageTk.PhotoImage(Image.open("image2.jpg").resize((495,235)))
frame = Frame(root,width=500,height=260)
frame.pack()
Label(frame,image=img,background=BG).pack()


play_btn = Button(root,text="Play",command=play_pause,state=DISABLED)
play_btn.place(x=20,y=270)    
volume_up_btn = Button(root,text="vol+",command=volume_up,state=DISABLED,width=4)
volume_up_btn.place(x=420,y=270)    
volume_down_btn = Button(root,text="vol-",command=volume_down,state=DISABLED,width=4)
volume_down_btn.place(x=455,y=270)    
mute_btn = Button(root,text="Mute",command=mute,state=DISABLED,width=5)
mute_btn.place(x=375,y=270)    

progress = Progressbar(root, orient = HORIZONTAL,length = 410, mode = 'determinate') 
progress.place(x=40,y=240)

play_time = Label(root,text="0:0",background=BG,foreground=FG)
play_time.place(x=10,y=240)
total_play_time = Label(root,text="0:0",background=BG,foreground=FG)
total_play_time.place(x=460,y=240)


root.mainloop()

