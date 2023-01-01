from tkinter import*
from tkinter import ttk,messagebox,filedialog
from PIL import Image,ImageTk
import pyperclip as pc
from pathlib import Path
from pytube import YouTube
import pytube.request
import urllib.request
from PIL import Image,ImageTk
import os
import threading

def exit():
    close=messagebox.askyesno("Close the app","Are you sure you want to quit",default="no")
    
    if close :
        Win.destroy()
    
def activbtn(event):
    if len(urlinput.get()) > 0:
        nxtbtn.configure(state="normal")
    else:
        nxtbtn.configure(state="disabled")

def pst():
    urlinput.delete(0,END)
    urlinput.insert(0,pc.paste())
   
    if len(urlinput.get()) > 0:
        nxtbtn.configure(state="normal")
    else:
        nxtbtn.configure(state="disabled")

def loc():
    if loca2.cget("text")=="Downloads":
        loca2.configure(text="Always ask")
        statustxt4.configure(text=" ")
    else:
        loca2.configure(text="Downloads")
        statustxt4.configure(text=downloads)

def nxt0():
    t1=threading.Thread(target=nxt)
    t1.start()

def download0(x):
    t2=threading.Thread(target=download, args=(x,))
    t2.start()

def nxt():
    try:
        global prog
        prog=Frame(Win,bg="#C70039",height=2,width=25)
        prog.place(x=0,y=472)

        nxtbtn.configure(state="disabled")
        
        prog.configure(width=50)
        
        pytube.request.default_range_size=256000

        global yt
        yt=YouTube(urlinput.get())
        yt.register_on_progress_callback(progress)
        yt.register_on_complete_callback(done)

        urllib.request.urlretrieve(yt.thumbnail_url,'thumbnail.png')
        thumbnailimg=Image.open('thumbnail.png')
        picre=thumbnailimg.resize((280,210),Image.Resampling.LANCZOS)
        pic=ImageTk.PhotoImage(picre)

        prog.configure(width=450)
        
        global frame2
        frame2=Frame(Win,height=471,width=600,bg="#670349")

        imglabel2=Label(frame2,image=pic,bd=0)
        imglabel2.place(x=5,y=5)
        imglabel2.image=pic

        global title
        title=yt.title

        global titlelabel
        titlelabel=Label(frame2,bg="#670349",text=title,fg="white",font=("Times 15"),wraplength=300, justify="center")
        titlelabel.place(x=290,y=5,width=305,height=67)

        dndframe=Frame(frame2,height=350,width=305,bg="#470132")
        dndframe.place(x=290,y=77)

        prog.configure(width=500)
        
        l1080=Label(dndframe,text="1080p Video",bg="#470132",fg="white",font=("Times 15"), justify="center")
        l1080.place(x=0,y=0,height=70,width=150)

        global d1080
        d1080=Button(dndframe,bg="#670349",text="Download",fg="white",font=("Times 13"),bd=0,command= lambda:download0(1080))
        d1080.place(x=160,y=28,height=35,width=141)

        prog.configure(width=550)
        
        sep1=ttk.Separator(dndframe, orient='horizontal')
        sep1.place(x=0,y=68,width=305)

        l720=Label(dndframe,text="720p Video",bg="#470132",fg="white",font=("Times 15"), justify="center")
        l720.place(x=0,y=70,height=70,width=150)

        prog.configure(width=600)
        
        global d720
        d720=Button(dndframe,bg="#670349",text="Download",fg="white",font=("Times 13"),bd=0,command= lambda:download0(720))
        d720.place(x=160,y=98,height=35,width=141)

        sep2=ttk.Separator(dndframe, orient='horizontal')
        sep2.place(x=0,y=138,width=305)

        l480=Label(dndframe,text="480p Video",bg="#470132",fg="white",font=("Times 15"), justify="center")
        l480.place(x=0,y=140,height=70,width=150)

        prog.configure(width=650)
        
        global d480
        d480=Button(dndframe,bg="#670349",text="Download",fg="white",font=("Times 13"),bd=0,command= lambda:download0(480))
        d480.place(x=160,y=168,height=35,width=141)

        sep3=ttk.Separator(dndframe, orient='horizontal')
        sep3.place(x=0,y=208,width=305)

        l360=Label(dndframe,text="360p Video",bg="#470132",fg="white",font=("Times 15"), justify="center")
        l360.place(x=0,y=210,height=70,width=150)

        prog.configure(width=700)
        
        global d360
        d360=Button(dndframe,bg="#670349",text="Download",fg="white",font=("Times 13"),bd=0,command= lambda:download0(360))
        d360.place(x=160,y=238,height=35,width=141)

        sep4=ttk.Separator(dndframe, orient='horizontal')
        sep4.place(x=0,y=278,width=305)

        lmp3=Label(dndframe,text="Mp3 Audio",bg="#470132",fg="white",font=("Times 15"), justify="center")
        lmp3.place(x=0,y=280,height=70,width=150)

        prog.configure(width=750)
        
        sep5=ttk.Separator(dndframe, orient='horizontal')
        sep5.place(x=0,y=348,width=305)

        global dmp3
        dmp3=Button(dndframe,bg="#670349",text="Download",fg="white",font=("Times 13"),bd=0,command= lambda:download0(3))
        dmp3.place(x=160,y=308,height=35,width=141)

        bckbtn=Button(frame2,bg="#470132",text="Back",fg="white",font=("Times 13"),bd=0,command=bck)
        bckbtn.place(x=446,y=432,height=35,width=149)

        prog.configure(width=800)
        
        frame2.place(x=0,y=0)
        statustxt2.configure(text="Download page...")

        Win.after(500,destroyprog())
    except Exception as e:
        messagebox.showerror("An error occurred",e)
        nxtbtn.configure(state="normal")
        prog.destroy()

def bck():
    frame2.destroy()
    nxtbtn.configure(state="normal")
    changebtn.configure(state="normal")

def destroyprog():
    prog.destroy()

def download(x):
    global value
    value=x

    btn(DISABLED)
    try:
        dst()
    except:
        pass

    if loca2.cget("text")=="Downloads":
        sto=str(Path.home()/"Downloads") 
        statustxt4.configure(text=sto)    
    else:
        changebtn.configure(state="disable")
        sto=filedialog.askdirectory(title="Select a directory")

        global audpath
        audpath=sto
        if sto:
            statustxt4.configure(text=sto)
        else:
            btn(NORMAL)
            return
    
    frame()
    
    if x==3:
        v="Downloading Mp3 audio..."
    else:
        v="Downloading "+str(x)+"p video..."
    statustxt2.configure(text=v)

    global size
    if x==360:
        
        try:
            size=round(int(yt.streams.get_by_itag("18").filesize)/1000000,1)
        except Exception as e:
            error(e)
            return
        
        total="0/"+str(size)+" MB"
        dndtxt.configure(text=total)

        try:
            yt.streams.get_by_itag("18").download(sto)
        except Exception as e:
            error(e)

    elif x==720:
        
        try:
            size=round(int(yt.streams.get_by_itag("22").filesize)/1000000,1)
        except Exception as e:
            error(e)
            return
        
        total="0/"+str(size)+" MB"
        dndtxt.configure(text=total)

        try:
            yt.streams.get_by_itag("22").download(sto)
        except Exception as e:
            error(e)

    elif x==3:
        audiodownload(sto)

    elif x==480:
        
        try:
            size=round(int(yt.streams.get_by_itag("135").filesize)/1000000,1)
        except Exception as e:
            error(e)
            return
    
        total="0/"+str(size)+" MB"
        dndtxt.configure(text=total)
   
        try:
            yt.streams.get_by_itag("135").download(sto)

            au=str(v)+"(audio)"
            statustxt2.configure(text=au)

            btn(DISABLED)
            frame()
            value=3
            audiodownload(sto)

            dndtxt.configure(text="Download Complete")

        except Exception as e:
           error(e)

    elif x==1080:
        
        try:
            size=round(int(yt.streams.get_by_itag("137").filesize)/1000000,1)
        except Exception as e:
            error(e)
            return
        
        total="0/"+str(size)+" MB"
        dndtxt.configure(text=total)
        
        try:
            yt.streams.get_by_itag("137").download(sto)

            au=str(v)+"(audio)"
            statustxt2.configure(text=au)

            btn(DISABLED)
            frame()
            value=3
            audiodownload(sto)

            dndtxt.configure(text="Download Complete")

        except Exception as e:
            error(e)

def audiodownload(x):
    
    try:
        global size
        size=round(int(yt.streams.get_by_itag("251").filesize)/1000000,1)
    except Exception as e:
        error(e)
        return
    
    total="0/"+str(size)+" MB"
    dndtxt.configure(text=total)
 
    try:
        yt.streams.get_by_itag("251").download(x)
    except Exception as e:
        error(e)

def error(x):
    messagebox.showerror("Error",x)
    downloadframe.destroy()
    btn(NORMAL)
    statustxt2.configure(text="Download page...")

def frame():
    global downloadframe
    downloadframe=Frame(frame2,width=436,height=35,bg="#470132")
    downloadframe.place(x=5,y=432)

    global dndprog
    dndprog=ttk.Separator(downloadframe,orient="horizontal")
    dndprog.place(x=10,y=17,width=300)

    global dndtxt
    dndtxt=Label(downloadframe,bg="#470132",fg="white",font=("Times 11"))
    dndtxt.place(x=320,y=7)

    global progbar
    progbar=Frame(downloadframe,height=4,bg="#900C3F")
    progbar.place(x=10,y=16)

def progress(stream,chunk,bytes_remaining):
    
    bytes=size-(round((bytes_remaining/1000000),1))

    sp=str(bytes).split(".")
    if len(sp[1]) > 1:
        bytes=round(bytes,1)

    total=str(bytes)+"/"+str(size)+" MB"
    dndtxt.configure(text=total)

    w=int((int(round(bytes,0))/int(round(size,0)))*300)
    progbar.configure(width=w) 

def done(stream,file_path):
    dndprog.destroy()
    progbar.destroy()
    dndtxt.place(x=10,y=7)

    if value==3:
        dndtxt.configure(text="Please wait as we convert...")

        if loca2.cget("text")=="Downloads":
            audpath=str(Path.home()/"Downloads")    
        else:
            audpath=statustxt4.cget("text")

        name=titlelabel.cget("text")
        if name.find(".") > -1:
            nm=name.split(".")
            title=str(nm[0])+str(nm[1])
        else:
            title=titlelabel.cget("text")

        orgfile=str(audpath)+"/"+str(title)+".webm"
        mp3file=str(audpath)+"/"+str(title)+".mp3"
        try:
            os.rename(orgfile,mp3file)
            dndtxt.configure(text="Download Complete")
            statustxt2.configure(text="Download Complete")
        except Exception as e:
            messagebox.showerror("Error",e)
            downloadframe.destroy()
    else:
        dndtxt.configure(text="Download Complete")
        statustxt2.configure(text="Download Complete")
    
    btn(NORMAL)

def dst():
    downloadframe.destroy()

def btn(x):
    changebtn.configure(state=x)
    d1080.configure(state=x)
    d720.configure(state=x)
    d480.configure(state=x)
    d360.configure(state=x)
    dmp3.configure(state=x)

Win=Tk()
Win.title("Video Downloader")
Win.geometry("800x500+220+120")
Win.resizable(False,False)

frame1=Frame(Win,height=500,width=800,bg="#670349")
frame1.place(x=0,y=0)

text=Label(frame1,bg="#670349",text="Insert the Youtube URL, below",fg="white",font=("Times 15"))
text.place(x=0,y=40,height=50,width=600)

urlinput=Entry(frame1,font=("Times 13"))
urlinput.bind("<KeyRelease>",activbtn)
urlinput.place(x=2,y=120,height=28,width=500)

pastebtn=Button(frame1,bg="#470132",text="Paste",fg="white",font=("Times 13"),bd=0,command=pst)
pastebtn.place(x=505,y=120,height=28,width=92)

info=Label(frame1,bg="#670349",text="Paste button automatically clears the previous link",fg="white",font=("Times 15"))
info.place(x=0,y=160,height=30,width=600)

nxtbtn=Button(frame1,bg="#470132",text="Next",fg="white",font=("Times 13"),bd=0,state="disabled",command=nxt0)
nxtbtn.place(x=200,y=430,height=35,width=200)

sideframe=Frame(Win,height=472,width=200,bg="#470132")
sideframe.place(x=600,y=0)

image=Image.open("Signature.png")
resize=image.resize((200,200))
img=ImageTk.PhotoImage(resize)

imglabel=Label(sideframe,image=img,bd=0)
imglabel.place(x=0,y=0)

loca=Label(sideframe,bg="#470132",text="Storage: ",fg="white",font=("Times 15"))
loca.place(x=2,y=200)

downloads=str(Path.home()/"Downloads")

loca2=Label(sideframe,bg="#470132",text="Downloads",fg="white",font=("Times 15"))
loca2.place(x=85,y=200)

changebtn=Button(sideframe,bg="#670349",text="Change location",fg="white",font=("Times 13"),bd=0,command=loc)
changebtn.place(x=15,y=350,height=35,width=170)

sep=ttk.Separator(frame1, orient='horizontal')
sep.place(x=0,y=472,width=820)
statusbar=Frame(Win,height=25,width=800,bg="#470132")
statusbar.place(x=0,y=475)

statustxt=Label(statusbar,text="Status : ",bg="#470132",font=("Times 13"))
statustxt.place(x=0,y=0)

statustxt2=Label(statusbar,text="Startup page...",bg="#470132",font=("Times 13"),fg="white")
statustxt2.place(x=60,y=0)

statustxt3=Label(statusbar,text="Storage : ",bg="#470132",font=("Times 13"))
statustxt3.place(x=400,y=0)

statustxt4=Label(statusbar,text=downloads,bg="#470132",font=("Times 13"),fg="white")
statustxt4.place(x=470,y=0)

histbtn=Button(sideframe,bg="#670349",text="History",fg="white",font=("Times 13"),bd=0)
histbtn.place(x=15,y=390,height=35,width=170)

ext=Button(sideframe,bg="#670349",text="Quit",fg="white",font=("Times 13"),bd=0,command=exit)
ext.place(x=15,y=430,height=35,width=170)

mainloop()

# Art by:

#     ...     ..      ..                                      ....        .   
#   x*8888x.:*8888: -"888:                                 .x88" `^x~  xH(`   
#  X   48888X `8888H  8888             .u    .            X888   x8 ` 8888h   
# X8x.  8888X  8888X  !888>          .d88B :@8c          88888  888.  %8888   
# X8888 X8888  88888   "*8%-        ="8888f8888r        <8888X X8888   X8?    
# '*888!X8888> X8888  xH8>            4888>'88"         X8888> 488888>"8888x  
#   `?8 `8888  X888X X888>            4888> '           X8888>  888888 '8888L 
#   -^  '888"  X888  8888>            4888>             ?8888X   ?8888>'8888X 
#    dx '88~x. !88~  8888>      .    .d888L .+      .    8888X h  8888 '8888~ 
#  .8888Xf.888x:!    X888X.:  .@8c   ^"8888*"     .@8c    ?888  -:8*"  <888"  
# :""888":~"888"     `888*"  '%888"     "Y"      '%888"    `*88.      :88%    
#     "~'    "~        ""      ^*                  ^*         ^"~====""`      