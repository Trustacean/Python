from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image
from tkinter import ttk,filedialog
import pygame
import os

root=Tk()
root.title("Music Player")
root.geometry("500x300")

pygame.mixer.init()

menubar = Menu(root)
root.config(menu=menubar)


organise_menu = Menu(menubar)
organise_menu.add_command(label='select folder')
menubar.add_cascade(label='Organise',menu=organise_menu)


songlist = Listbox(root,bg="black",fg="white",width=100,height=15)
songlist.pack()

play_btn_image = PhotoImage(file='MP\\play.png')
pause_btn_image = PhotoImage(file='MP\\pause.png')
next_btn_image = PhotoImage(file='MP\\next.png')
previous_btn_image = PhotoImage(file='MP\\previous.png')

control_frame = Frame(root)
control_frame.pack()

play_btn = Button(control_frame,image=play_btn_image,borderwidth=0)
pause_btn = Button(control_frame,image=pause_btn_image,borderwidth=0)
next_btn = Button(control_frame,image=next_btn_image,borderwidth=0)
prev_btn = Button(control_frame,image=previous_btn_image,borderwidth=0)

play_btn.grid(row=0,column=1,padx=7,pady=10)
pause_btn.grid(row=0,column=2,padx=7,pady=10)
next_btn.grid(row=0,column=3,padx=7,pady=10)
prev_btn.grid(row=0,column=0,padx=7,pady=10)



root.mainloop()