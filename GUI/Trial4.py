from tkinter import *
from PIL import ImageTk, Image
import os
import pygame

class KaraokeProject():
    def __init__(self,master):
        self.master = master
        self.master.title("Karaoke Project")
        self.master.geometry("1920x1080")
        self.master.resizable(width=False, height=False)
        self.track = StringVar()
        self.status = StringVar()
        self.mainMenu()

    def mainMenu(self):
        bg=Image.open('GUI\\BG1.png') # type: ignore
        bg=ImageTk.PhotoImage(bg)
        background = Label(image=bg,borderwidth=0)
        background.place(x=0,y=0)

        self.entry1 = Entry(background,font=('Helvetica 36'),fg="#77716c",bg="#ffffff",borderwidth=0, highlightthickness=0,justify='center')
        self.entry1.place(width=350,height=50,x=220,y=515)
        submit_btn_image = PhotoImage(file='GUI\\submit.png')
        submit_btn = Button(background,image=submit_btn_image,borderwidth=0,bg="#e2dfd9",command=self.saveInput)
        submit_btn.place(x=255,y=586)
        
        root.mainloop()
    
    def saveInput(self):
        self.username = self.entry1.get()
        if self.username == "":
            warn = Label(self.master,font=('Helvetica 16'),text="Enter Username!",fg="#ff002a",bg="#e2dfd9").place(width=280,height=20,x=255,y=565)
        else :
            self.songSelectionMenu()
        # tes = Label(self.master,font=('Helvetica 36'),text=self.username).place(width=200,height=50,x=0,y=0)

    def songSelectionMenu(self):
        bg=Image.open('GUI\\Song Selection.png') # type: ignore
        bg=ImageTk.PhotoImage(bg)
        background = Label(image=bg,borderwidth=0)
        background.place(x=0,y=0)

        play_btn_image = PhotoImage(file='GUI\\play.png')
        pause_btn_image = PhotoImage(file='GUI\\pause.png')
        stop_btn_image = PhotoImage(file='GUI\\stop.png')
        play_btn = Button(background,image=play_btn_image,borderwidth=0,bg="#ffffff",command=self.unpause)
        play_btn.place(x=156,y=785)
        pause_btn = Button(background,image=pause_btn_image,borderwidth=0,bg="#ffffff",command=self.pause)
        pause_btn.place(x=434,y=785)
        stop_btn = Button(background,image=stop_btn_image,borderwidth=0,bg="#ffffff",command=self.stop)
        stop_btn.place(x=734,y=785)
        start_btn = Button(background,text="Start",borderwidth=0,bg="#ffffff",command=self.play)
        start_btn.place(x=1570,y=958,width=250,height=70)
        songsframe = Frame(background)
        songsframe.place(x=1020,y=155,width=800,height=800)
        scroll_y = Scrollbar(songsframe,orient=VERTICAL)
        self.songlist = Listbox(songsframe,yscrollcommand=scroll_y.set,selectbackground="#B0FC38",selectmode=SINGLE,font=("arial",22,"bold"))
        
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.songlist.yview)
        self.songlist.place(x=0,y=0,width=800,height=800)
        os.chdir("D:\\music")
        songtracks = os.listdir()
        for track in songtracks:
            self.songlist.insert(END,track)

        root.mainloop()


    def play(self):
        self.track.set(self.songlist.get(ACTIVE))
        self.status.set("-Playing")
        pygame.mixer.music.load(self.songlist.get(ACTIVE))
        pygame.mixer.music.play()
    def stop(self):
        self.status.set("-Stopped")
        pygame.mixer.music.stop()

    def pause(self):
        self.status.set("-Paused")
        pygame.mixer.music.pause()

    def unpause(self):
        self.status.set("-Playing")
        pygame.mixer.music.unpause()

pygame.init()
pygame.mixer.init()
root = Tk()
KaraokeProject(root)