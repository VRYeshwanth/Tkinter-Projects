import tkinter as tk
from tkinter import filedialog
from tkinter import messagebox
import os
import shutil

window = tk.Tk()
window.title('Directory Organizer')
window.iconbitmap(r'C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\Directory Organizer\folder_icon.ico')

def clear_text():
    path.set("")
    dir_display.config(text="")

def browse_dir():
    filedir = filedialog.askdirectory()
    if filedir:
        path.set(filedir)
        dir_display.config(text=filedir)
    else:
        path.set("")
        dir_display.config(text="")

def organize():
    videos = [".mp4", ".avi", ".mkv"]
    images = [".png", ".jpeg", ".jpg", ".gif", ".ico"]
    documents = [".txt", ".docx", ".pptx", ".xlsx", ".doc", ".ppt", ".xls"]
    pdf = [".pdf"]
    executables = [".exe"]
    p_var = path.get()
    try:
        os.makedirs(fr"{p_var}\Videos")
        os.makedirs(fr"{p_var}\Images")
        os.makedirs(fr"{p_var}\PDF")
        os.makedirs(fr"{p_var}\Documents")
        os.makedirs(fr"{p_var}\Executables")
        os.makedirs(fr"{p_var}\Others")
    except Exception as e:
        pass

    files = os.listdir(p_var)
    for file in files:
        file_name, extension = os.path.splitext(file)
        
        if extension.lower() in videos:
            if os.path.isfile(fr"{p_var}\{file}"):
                shutil.move(fr"{p_var}\{file}", fr"{p_var}\Videos")
        if extension.lower() in images:
            if os.path.isfile(fr"{p_var}\{file}"):
                shutil.move(fr"{p_var}\{file}", fr"{p_var}\Images")
        if extension.lower() in documents:
            if os.path.isfile(fr"{p_var}\{file}"):
                shutil.move(fr"{p_var}\{file}", fr"{p_var}\Documents")
        if extension.lower() in pdf:
            if os.path.isfile(fr"{p_var}\{file}"):
                shutil.move(fr"{p_var}\{file}", fr"{p_var}\PDF")
        if extension.lower() in executables:
            if os.path.isfile(fr"{p_var}\{file}"):
                shutil.move(fr"{p_var}\{file}", fr"{p_var}\Executables")
        
        else:
            if os.path.isfile(fr"{p_var}\{file}"):
                shutil.move(fr"{p_var}\{file}", fr"{p_var}\Others")
    
    messagebox.showinfo("Success", "Files Successfully Sorted")



disp_label = tk.Label(window, text="Choose your Directory", font="Calibri 15 bold")
disp_label.pack(padx=10, pady=10)

path = tk.StringVar()
dir_display = tk.Label(window, text="", font="Calibri 15", width=55, textvariable=path)
dir_display.pack(padx=10, pady=10)

button_frame = tk.Frame(window)
button_frame.pack()

browse_btn = tk.Button(button_frame, text="Browse", font="Calibri 13", command=browse_dir)
browse_btn.grid(row=0, column=1, padx=15, pady=15, ipadx=10)
clear_btn = tk.Button(button_frame, text="Clear", font="Calibri 13", command=clear_text)
clear_btn.grid(row=0, column=2, padx=15, pady=15, ipadx=10)
organize_btn = tk.Button(button_frame, text="Organize", font="Calibri 13", command=organize)
organize_btn.grid(row=0, column=3, padx=15, pady=15, ipadx=10)

window.mainloop()