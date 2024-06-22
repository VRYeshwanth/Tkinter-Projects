import tkinter as tk
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
from pytube import YouTube
from ttkbootstrap import Style

style = Style('darkly')
window = style.master
window.title('Youtube Video Downloader')
window.iconbitmap(r'C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\Youtube Video Downloader\Video Download.ico')
window.resizable(0,0)

def browse_dir():
    filedir = filedialog.askdirectory()
    if filedir:
        dirpath.set(filedir)
        dir_label.config(text=filedir)

def download_video():
    yurl = url.get()
    ypath = dirpath.get()
    try:
        yt = YouTube(yurl)
        yd = yt.streams.get_highest_resolution()
        yd.download(ypath)
        messagebox.showinfo("Success", "Video successfully downloaded")
        inp_entry.delete(0,tk.END)
        dirpath.set("")
        dir_label.config(text="")
    except Exception as e:
        messagebox.showerror("Error", f"Error downloading Video, {str(e)}")

img = ImageTk.PhotoImage(Image.open(r"C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\Youtube Video Downloader\Youtube_Logo.png"))
img_label = tk.Label(window, image=img)
img_label.pack()

heading = tk.Label(window, text="Youtube Video Downloader", fg="#F40000", font="Calibri 20 bold")
heading.pack(padx=20, pady=5)

#Code for the input frame
inp_frame = tk.Frame(window)
inp_frame.pack()

inp_head = tk.Label(inp_frame, text="Enter the url = ", font="Calibri 15")
inp_head.grid(row=0, column=0, padx=15, pady=5)

url = tk.StringVar()
inp_entry = tk.Entry(inp_frame, width=35, textvariable=url)
inp_entry.grid(row=0, column=1, padx=15)

#Code for directory input frame
dir_inp_frame = tk.Frame(window)
dir_inp_frame.pack()

dir_head_name = tk.Label(dir_inp_frame, text="Directory = ", font="Calibri 15")
dir_head_name.grid(row=0, column=0)

dirpath = tk.StringVar()
dir_label = tk.Label(dir_inp_frame, text="", font="Calibri 15", width=27, textvariable=dirpath)
dir_label.grid(row=0, column=1)

#Code for button frame
btn_frame = tk.Frame(window)
btn_frame.pack()

folder_img = ImageTk.PhotoImage(Image.open(r"C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\Youtube Video Downloader\browse.png"))
down_img = ImageTk.PhotoImage(Image.open(r"C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\Youtube Video Downloader\download.png"))

browse_btn = tk.Button(btn_frame, image=folder_img, font="Calibri 12", command=browse_dir, text="Browse", compound=tk.TOP)
browse_btn.grid(row=0, column=0, padx=(0,20), ipadx=10, ipady=5, pady=(5,25))

download_btn = tk.Button(btn_frame, image=down_img, font="Calibri 12", command=download_video, text="Download", compound=tk.TOP)
download_btn.grid(row=0, column=1, padx=(20,0), ipadx=10, ipady=5, pady=(5,25))

window.mainloop()