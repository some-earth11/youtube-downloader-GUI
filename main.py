# Importing Necessary Libraries

import pafy as pf                           #youtube-dl should also be installed as Pafy uses it

import tkinter as tk
from tkinter import *
from tkinter import messagebox, filedialog


# Creating object of tk class
root = tk.Tk()

# Setting up the Box
root.geometry("720x480")                      
root.resizable(False, False)    
root.title("YouTube Downloader")
root.config(background="red")

# Creating the tkinter Variables
URL = StringVar()
Download_Path = StringVar()

def Widgets():

    head_label = Label(root,
                    text="YouTube Audio/Video Downloader",
					padx=15,
					pady=15,
					font="Lemonmilk 18",
					bg="red",
					fg="white")
    head_label.grid(row=1,
					column=1,
					pady=10,
					padx=30,
					columnspan=4)
    
    link_label = Label(root,
                    text='URL :',
                    font='SegoeUI 12',
                    bg='black',
                    fg='white',
                    pady=5,
                    padx=5)
    link_label.grid(row=2,
                    column=0,
                    pady=5,
                    padx=5)

    root.linkText = Entry(root,
                    width=35,
                    textvariable=URL,
                    font='SegoeUI 14')
    root.linkText.grid(row=2,
                    column=1,
                    pady=5,
                    padx=5,
                    columnspan=2)

    destination_label = Label(root,
                    text='Destination :',
                    font='SegoeUI 12',
                    bg='black',
                    fg='white',
                    pady=5,
                    padx=5)
    destination_label.grid(row=3,
                    column=0,
                    pady=5,
                    padx=5)

    root.destinationText = Entry(root,
                    width=35,
                    textvariable=Download_Path,
                    font='SegoeUI 14')
    root.destinationText.grid(row=3,
                    column=1,
                    pady=5,
                    padx=5,
                    columnspan=2)

    browse_button = Button(root,
                    text='Browse',
                    command=Browse,
                    width=10,
                    bg='white',
                    relief='groove')
    browse_button.grid(row=3,
                    column=3,
                    pady=1,
                    padx=1)

    VDownload = Button(root,
                    text="Download Video",
                    command=DownloadVideo,
                    width=20,
                    bg='white',
                    padx=10,
                    pady=15,
                    relief='groove',)
    VDownload.grid(row=4,
                    column=1,
                    pady=20,
                    padx=20)


def Browse():
	download_Directory = filedialog.askdirectory(initialdir="YOUR DIRECTORY PATH", title="Save Video")

	Download_Path.set(download_Directory)


Download_Folder = Download_Path.get()

def DownloadVideo(): 
    # Getting user-input Youtube Link
    url = URL.get()
    Download_Folder = Download_Path.get()
    video = pf.new(url)
    # Getting the best resolution video   
    best = video.getbest()                 
    best.download(Download_Folder)
    # Displaying the Confirmation message
    messagebox.showinfo("SUCCESSFULLY","VIDEO DOWNLOADED AND SAVED IN\n" + Download_Folder)

def DownloadAudio():
    
    url = URL.get()
    Download_Folder = Download_Path.get()
    video = pf.new(url)
    # Getting the best quality audio
    bestaudio = video.getbestaudio()
    bestaudio.download(Download_Folder)
    
    messagebox.showinfo("SUCCESSFULLY","AUDIO DOWNLOADED AND SAVED IN\n" + Download_Folder)



# Calling all Widgets into Action    
Widgets()

# Infinte Loop for the Program
root.mainloop()



#Code Created by Samarth Kumar