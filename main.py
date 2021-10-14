from tkinter import *
from PIL import ImageTk, Image

from pytube import YouTube

def clear():
    msg=" "*500
    error_msg=Message(main_window,text=msg,width=500)
    error_msg.place(x=170,y=330)
    error_msg=Message(main_window,text=msg,width=500)
    error_msg.place(x=170,y=350)
    error_msg=Message(main_window,text=msg,width=500)
    error_msg.place(x=250,y=300)

def error(k):
    clear()
    if k==-1:
        #clear()
        msg="Downloading..."
        error_msg=Message(main_window,text=msg,width=500)
        error_msg.place(x=240,y=300)
    elif k==0:
        #clear()
        msg="Invalid Link!"
        error_msg=Message(main_window,text=msg,width=500)
        error_msg.place(x=240,y=300)
    else:
        #clear()
        msg="The given Resolution is not available"
        msg2=''
        for i in k:
            msg2+=i+" "
        msg2+="are available"

        error_msg=Message(main_window,text=msg,width=500)
        error_msg.place(x=170,y=330)
        error_msg=Message(main_window,text=msg2,width=500)
        error_msg.place(x=170,y=350)





def download_video():
    clear()
    actual_link=link.get()
    resolution=(clicked.get())
    d_path="C://Users//Lenovo//Downloads"
    if resolution=="":
        resolution="1080p"

    d_path="C://Users//Lenovo//Downloads"

    try:
        yt=YouTube(actual_link)
        available_downloads = yt.streams
        temp=(available_downloads.filter(res=resolution,mime_type="video/mp4"))
        if len(temp)<1:
            index=resolution_list.index(resolution)
            available_downloads_set=list()
            for i in range(6):
                temp=(available_downloads.filter(res=resolution_list[i],mime_type="video/mp4"))
                if len(temp)>0:
                    available_downloads_set.append(resolution_list[i])
            error(available_downloads_set)
        else:
            error(-1)
            video=temp.first()
            video.download(d_path)


    except:
        error(0)
        return

    #      https://youtu.be/USn19iuBJv0


#for window
main_window=Tk()
main_window.title("YouTube Video Downloader")
main_window.geometry("600x400")

#for youtube logo
img_path="logo.png"

canvas = Canvas(main_window, width = 500, height = 200)

canvas.place(x=252,y=138)
img = ImageTk.PhotoImage(Image.open(img_path))
canvas.create_image(0,0 ,anchor=NW, image=img)

#Enter link label
link_label=Message(main_window,text="Enter link")
link_label.place(x=250,y=190)

#Resolution label
link_label_res=Message(main_window,text="Resolution",width=100)
link_label_res.place(x=470,y=190)

#text box (Entry) to enter the link
link=Entry(main_window)
link.place(x=150,y=220,width=300)

#selecting resolution

resolution_list=["1080p","720p","480p","360p","240p","144p"]
clicked = StringVar()
res_clicked = OptionMenu( main_window , clicked , *resolution_list )
res_clicked.place(x=480,y=215)

#download button
download=Button(main_window,text="Download",command=download_video)
download.place(x=250,y=250)


main_window.mainloop()
