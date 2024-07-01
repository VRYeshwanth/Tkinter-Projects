import tkinter as tk
from tkinter import filedialog,messagebox
import os,shutil

window = tk.Tk()
window.title('Directory Backup')
window.resizable(0,0)

def browseSrc():
    source = filedialog.askdirectory()
    if source:
        src_lab.config(text=source)
    else:
        src_lab.config(text="")

def browseDest():
    destination = filedialog.askdirectory()
    if destination:
        dest_lab.config(text=destination)
    else:
        dest_lab.config(text="")

def createBackup(src, dest):
    if src == "" or dest == "":
        messagebox.showwarning("WARNING", "Please select the folder/folders to create a backup")
    else:
        if not os.path.isdir(src):
            messagebox.showwarning("WARNING", "Source folder doesnt exist")
        elif not os.path.isdir(dest):
            messagebox.showwarning("WARNING", "Destination folder doesnt exist")
        else:
            files = os.listdir(src)
            for file in files:
                src_path = os.path.join(src, file)
                dest_path = os.path.join(dest, file)
                counter = 0
                try:
                    if os.path.isdir(src_path):
                        shutil.copytree(src_path, dest_path)
                    else:
                        shutil.copy(src_path, dest_path)
                except Exception:
                    counter += 1
                
            if counter == 0:
                messagebox.showinfo("SUCCESS", "Folder backed up successfully")
            else:
                messagebox.showwarning("WARNING", f"Failed to backup {counter} items")
            

main_frame = tk.LabelFrame(window)
main_frame.pack(padx=20, pady=20)

head = tk.Label(main_frame, text="Directory Backup", font="Calibri 20 bold")
head.grid(row=0, columnspan=2, padx=20, pady=15)

src_inp = tk.Label(main_frame, text="Source : ", font="Calibri 15")
src_inp.grid(row=1,column=0, padx=10, pady=10, sticky="W")

src_lab = tk.Label(main_frame, text="", font="Calibri 15", wraplength=500)
src_lab.grid(row=1, column=1, padx=10, pady=10, sticky="W")

src_btn = tk.Button(main_frame, text="Browse", font="Calibri 14", command=browseSrc)
src_btn.grid(row=2, columnspan=2, padx=10, pady=10, ipadx=15)

dest_inp = tk.Label(main_frame, text="Destination : ", font="Calibri 15")
dest_inp.grid(row=3,column=0, padx=10, pady=10, sticky="W")

dest_lab = tk.Label(main_frame, text="", font="Calibri 15", wraplength=500)
dest_lab.grid(row=3, column=1, padx=10, pady=10, sticky="W")

dest_btn = tk.Button(main_frame, text="Browse", font="Calibri 14", command=browseDest)
dest_btn.grid(row=4, columnspan=2, padx=10, pady=10, ipadx=15)

backup_btn = tk.Button(window, text="BACKUP", font="Calibri 14", command=lambda : createBackup(src_lab["text"], dest_lab['text']))
backup_btn.pack(padx=10, pady=10, ipadx=15)

window.mainloop()