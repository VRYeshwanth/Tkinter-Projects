from pdf2docx import Converter
import os
import tkinter as tk
from tkinter import filedialog, messagebox
window = tk.Tk()
window.title("PDF to Word Convertor")
window.resizable(0,0)

def browse():
    dir_path = filedialog.askdirectory()
    if dir_path:
        dir_holder.config(text=dir_path)
    else:
        dir_holder.config(text="")

def convert(p):
    if p == "":
        messagebox.showerror("ERROR", "Please select a folder")
    else:
        dir_path = p

        pdf_files = []
        for filename in os.listdir(dir_path):
            _,ext = os.path.splitext(filename)
            if ext.lower() in ['.pdf']:
                pdf_files.append(filename)
        counter = 0
        for files in pdf_files:
            try:
                file_path = os.path.join(dir_path,files)
                docx_path = os.path.join(dir_path, f"{files}.docx")
                cv = Converter(file_path)
                cv.convert(docx_path)
                cv.close()
            except Exception:
                counter += 1
        
        if counter == 0:
            messagebox.showinfo("SUCCESS", "All PDF'S successfully converted")
        else:
            messagebox.showwarning("Warning", f"Could not convert {counter} PDF's")

title = tk.Label(window, text="PDF to Word Convertor", font="Calibri 20 bold")
title.grid(row=0, columnspan=2, padx=15, pady=15)

dir_holder = tk.Label(window, font="Calibri 18")
dir_holder.grid(row=1, columnspan=2, padx=(10,20), pady=10)

browse_btn = tk.Button(window, text="Browse", font="Calibri 15", command=browse)
browse_btn.grid(row=2, column=0, pady=15, ipadx=10, padx=10)

convert_btn = tk.Button(window, text="Convert", font="Calibri 15", command= lambda: convert(dir_holder['text']))
convert_btn.grid(row=2, column=1, pady=15, ipadx=15, padx=10)

window.mainloop()