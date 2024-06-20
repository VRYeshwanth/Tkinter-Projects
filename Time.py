import tkinter as tk
from tkinter import ttk
from datetime import datetime

window = tk.Tk()
window.title('Date and Time')

def update_time():
    time = datetime.now()

    ftime = time.strftime("%d-%m-%Y %H:%M:%S")
    time_label.config(text=ftime)
    window.after(1000, update_time)

time_label = ttk.Label(window, text="", font="Calibri 20 bold")
time_label.pack(padx=20, pady=20)
update_time()

window.mainloop()