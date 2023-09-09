# Author : Edward Vito
# Ver : 1.0.1
# Program Karaoke, Jika Error Coba Jalankan UAS_BAK.py

from tkinter import *
import os
import pygame

class KaraokeProject():
    def __init__(self,master):
        self.master = master
        self.master.title("Karaoke Project")
        self.master.geometry("960x540")
        self.master.resizable(width=False, height=False)
        self.track = StringVar()
        self.status = StringVar()
        self.mainbg = PhotoImage(file='main.png')
        self.selectionbg = PhotoImage(file='selection.png')
        self.paymentbg = PhotoImage(file='payment.png')
        self.submitimg = PhotoImage(file='submit.png')
        self.playimg = PhotoImage(file='play.png')
        self.pauseimg = PhotoImage(file='pause.png')
        self.stopimg = PhotoImage(file='stop.png')
        os.chdir("music")
        self.songtracks = os.listdir()
        self.mainMenu()

    def mainMenu(self):
        self.main = Label(image=self.mainbg,borderwidth=0)
        self.main.place(x=0,y=0)
        
        self.totalPrice = 0
        self.entry1 = Entry(self.main,font=('Helvetica 18'),fg="#77716c",bg="#ffffff",borderwidth=0, highlightthickness=0,justify='center')
        self.entry1.place(width=175,height=25,x=110,y=257.5)
        submit_btn = Button(self.main,image=self.submitimg,borderwidth=0,bg="#e2dfd9",command=self.saveInput)
        submit_btn.place(x=127.5,y=293)
        
        root.mainloop()
    
    def saveInput(self):
        self.username = self.entry1.get()
        if self.username == "":
            warn = Label(self.main,font=('Helvetica 8'),text="Enter Username!",fg="#ff002a",bg="#e2dfd9").place(width=140,height=10,x=127.5,y=282.5)
        else :
            self.songSelectionMenu()

    def songSelectionMenu(self):
        self.main.destroy()
        self.selection = Label(image=self.selectionbg,borderwidth=0)
        self.selection.place(x=0,y=0)
        songTrack=Label(self.selection,textvariable=self.track,font=('arial',8,'bold'),bg="#ffffff").place(x=24,y=312.5)
        trackStatus=Label(self.selection,textvariable=self.status,font=('arial',8,'bold'),bg="#ffffff").place(x=24,y=330)

        play_btn = Button(self.selection,image=self.playimg,borderwidth=0,bg="#ffffff",command=self.unpause)
        play_btn.place(x=76,y=390.5)
        pause_btn = Button(self.selection,image=self.pauseimg,borderwidth=0,bg="#ffffff",command=self.pause)
        pause_btn.place(x=215,y=390.5)
        stop_btn = Button(self.selection,image=self.stopimg,borderwidth=0,bg="#ffffff",command=self.stop)
        stop_btn.place(x=365,y=390.5)

        start_btn = Button(self.selection,text="Start",font=('Helvetica 8'),borderwidth=0,bg="#ffffff",command=self.start_msg)
        start_btn.place(x=510,y=479,width=125,height=35)
        end_btn = Button(self.selection,text="End",font=('Helvetica 8'),borderwidth=0,bg="#ffffff",command=self.end_msg)
        end_btn.place(x=785,y=479,width=125,height=35)

        songsframe = Frame(self.selection)
        songsframe.place(x=511,y=77.5,width=400,height=400)
        scroll_y = Scrollbar(songsframe,orient=VERTICAL)
        self.songlist = Listbox(songsframe,yscrollcommand=scroll_y.set,selectbackground="#c89c59",selectmode=SINGLE,font=("arial",11,"bold"))
        scroll_y.pack(side=RIGHT,fill=Y)
        scroll_y.config(command=self.songlist.yview)
        self.songlist.place(x=0,y=0,width=400,height=400)
        for track in self.songtracks:
            self.songlist.insert(END,track)
        
        self.searchEntry = Entry(self.selection,font=('Helvetica 18'),fg="#77716c",bg="#ffffff",borderwidth=0, highlightthickness=0,justify='left')
        self.searchEntry.place(width=350,height=35,x=550,y=22.5)
        self.searchEntry.bind('<Return>', self.search)
        root.mainloop()
    
    def paymentMenu(self):
        self.stop()
        self.qw.destroy()
        self.selection.destroy()
        self.payment = Label(image=self.paymentbg,borderwidth=0)
        self.payment.place(x=0,y=0)

        total=Label(self.payment,text=f"Rp {self.totalPrice}.000,00",font=('Helvetica',16,'bold'),bg="#ffffff",fg="black")
        total.place(width=225,height=35,x=597.5,y=150)

        self.payEntry = Entry(self.payment,font=('Helvetica 18'),fg="#77716c",bg="#ffffff",borderwidth=0, highlightthickness=0,justify='left')
        self.payEntry.place(width=135,height=25,x=760,y=447.5)

        pay=Button(self.payment,font=('Helvetica 18'),text="Pay",command=self.pay)
        pay.place(width=125,height=30,x=647.5,y=482.5)

        root.mainloop()

    def start_msg(self):
        self.qw=Tk()
        frame1 = Frame(self.qw, highlightbackground="green", highlightcolor="green",highlightthickness=1, bd=0)
        frame1.pack()
        self.qw.overrideredirect(1)
        self.qw.geometry("200x100+650+400")
        lbl = Label(frame1, text="Are you sure you want to start?").pack()
        price = Label(frame1,text="This song costs Rp 10.000,00").pack()
        yes_btn = Button(frame1, text="Yes", bg="light blue", fg="red",command=self.play, width=10)
        yes_btn.pack(padx=10, pady=10 , side=LEFT)
        no_btn = Button(frame1, text="No", bg="light blue", fg="red",command=self.qw.destroy, width=10)
        no_btn.pack(padx=10, pady=10, side=LEFT)
        self.qw.mainloop()

    def end_msg(self):
        self.qw=Tk()
        frame1 = Frame(self.qw, highlightbackground="green", highlightcolor="green",highlightthickness=1, bd=0)
        frame1.pack()
        self.qw.overrideredirect(1)
        self.qw.geometry("220x100+650+400")
        lbl = Label(frame1, text="Are you sure you want to end this session?").pack()
        price = Label(frame1,text="You will be directed to payment menu").pack()
        yes_btn = Button(frame1, text="Yes", bg="light blue", fg="red",command=self.paymentMenu, width=10)
        yes_btn.pack(padx=10, pady=10 , side=LEFT)
        no_btn = Button(frame1, text="No", bg="light blue", fg="red",command=self.qw.destroy, width=10)
        no_btn.pack(padx=10, pady=10, side=LEFT)
        self.qw.mainloop()

    def pay_msg(self,change):
        self.qw=Tk()
        frame1 = Frame(self.qw, highlightbackground="green", highlightcolor="green",highlightthickness=1, bd=0)
        frame1.pack()
        self.qw.overrideredirect(1)
        self.qw.geometry("220x100+650+400")
        lbl = Label(frame1, text="Thankyou!").pack()
        price = Label(frame1,text=f"Change = {change}").pack()
        OK_btn = Button(frame1, text="OK", bg="light blue", fg="red",command=self.cont, width=10)
        OK_btn.pack(padx=10, pady=10 , side=LEFT)
        self.qw.mainloop()

    def cont(self):
        self.qw.destroy()
        self.mainMenu()

    def search(self,event):
        sstr=self.searchEntry.get()
        self.songlist.delete(0,END)

        if sstr =="":
            for track in self.songtracks:
                self.songlist.insert(END,track)
        else :
            for track in self.songtracks:
                if track.__contains__(sstr):
                    self.songlist.insert(END,track)

    def play(self):
        self.qw.destroy()
        self.totalPrice += 10
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

    def pay(self):
        amount=int(self.payEntry.get())
        if amount<self.totalPrice*1000:
            warn = Label(self.payment,font=('Helvetica 12'),text="Please Input The Right Amount!",fg="#ff002a",bg="#e2dfd9").place(width=225,height=35,x=600,y=200)
        else :
            self.payment.destroy()
            self.pay_msg(amount-self.totalPrice*1000)

pygame.init()
pygame.mixer.init()
root = Tk()
KaraokeProject(root)