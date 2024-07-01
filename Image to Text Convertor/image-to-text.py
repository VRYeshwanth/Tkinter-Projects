from PIL import Image
from pytesseract import pytesseract
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import subprocess

def check_tesseract_installed():
    try:
        result = subprocess.run(['tesseract', '--version'], capture_output=True, text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def browse():
    dir_path = filedialog.askdirectory()
    if dir_path:
        dir_holder.config(text=dir_path)
    else:
        dir_holder.config(text="")

def convert(p):
    if p == "":
        messagebox.showwarning("WARNING", "Please select a folder")
    else:
        if check_tesseract_installed():
            path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
            pytesseract.tesseract_cmd = path_to_tesseract
            dir_path = p
            counter = 0
            img_files = []
            for filename in os.listdir(dir_path):
                _, ext = os.path.splitext(filename)
                if ext.lower() in ['.png', '.jpeg', '.jpg', '.gif', '.tiff']:
                    img_files.append(filename)

            for filen in img_files:
                try:
                    img_path = os.path.join(dir_path, filen)
                    img = Image.open(img_path)
                    text = pytesseract.image_to_string(img)

                    file_name = f"{filen.split('.')[0]}.txt"
                    with open(os.path.join(dir_path, file_name), "w") as f:
                        f.write(text)
                except Exception as e:
                    counter += 1
                    print(f"Error converting file {filen}: {e}")

            if counter == 0:
                messagebox.showinfo("SUCCESS", "All images successfully converted")
            else:
                messagebox.showinfo("INFO", f"Could not convert {counter} images")
        else:
            messagebox.showerror("ERROR", "Tesseract not found. Please install it and retry")

window = tk.Tk()
window.title("Image to Text Convertor")
window.resizable(0, 0)

title = tk.Label(window, text="Image to Text Convertor", font="Calibri 20 bold")
title.grid(row=0, columnspan=2, padx=15, pady=15)

dir_holder = tk.Label(window, font="Calibri 18")
dir_holder.grid(row=1, columnspan=2, padx=(10, 20), pady=10)

browse_btn = tk.Button(window, text="Browse", font="Calibri 15", command=browse)
browse_btn.grid(row=2, column=0, pady=15, ipadx=10, padx=10)

convert_btn = tk.Button(window, text="Convert", font="Calibri 15", command=lambda: convert(dir_holder['text']))
convert_btn.grid(row=2, column=1, pady=15, ipadx=15, padx=10)

window.mainloop()
