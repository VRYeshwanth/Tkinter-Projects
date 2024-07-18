import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Temperature Convertor')
window.iconbitmap(r'C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\Temperature Convertor\thermometer.ico')
window.resizable(0,0)

def check_num(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def ctof(temp):
    temp = float(temp)
    return round((1.8 * temp) + 32, 3)

def ftoc(temp):
    temp = float(temp)
    return round((5/9)*(temp - 32), 3)

def ctok(temp):
    temp = float(temp)
    return round(temp + 273, 3)

def ktoc(temp):
    temp = float(temp)
    return round(temp - 273, 3)

def ktof(temp):
    temp = float(temp)
    return round((1.8 * (temp - 273)) + 32, 3)

def ftok(temp):
    temp = float(temp)
    return round((5/9)*(temp - 32) + 273, 3)

def convert():
    ch1 = m1.get()
    ch2 = m2.get()
    temp = t.get()

    if not check_num(temp):
        messagebox.showerror("ERROR", "Please enter a number")
    else:
        if not ch1 == ch2:
            if ch1 == "℃" and ch2 == "℉":
                out_temp = ctof(temp)
                out_lab.config(text=f"{temp} {ch1} = {out_temp} {ch2}")
            if ch1 == "℉" and ch2 == "℃":
                out_temp = ftoc(temp)
                out_lab.config(text=f"{temp} {ch1} = {out_temp} {ch2}")
            if ch1 == "℃" and ch2 == "K":
                out_temp = ctok(temp)
                out_lab.config(text=f"{temp} {ch1} = {out_temp} {ch2}")
            if ch1 == "K" and ch2 == "℃":
                out_temp = ktoc(temp)
                out_lab.config(text=f"{temp} {ch1} = {out_temp} {ch2}")
            if ch1 == "K" and ch2 == "℉":
                out_temp = ktof(temp)
                out_lab.config(text=f"{temp} {ch1} = {out_temp} {ch2}")
            if ch1 == "℉" and ch2 == "K":
                out_temp = ftok(temp)
                out_lab.config(text=f"{temp} {ch1} = {out_temp} {ch2}")
        else:
            out_lab.config(text=f"{temp} {ch1} = {temp} {ch2}")

def swap():
    item1 = m1.get()
    item2 = m2.get()
    m1.set(item2)
    m2.set(item1)

# Input Frame
inp_frame = tk.Frame(window)
inp_frame.pack(padx=20, pady=(20,15))

head = tk.Label(inp_frame, text="Enter the temperature : ", font="Calibri 15")
head.grid(row=0, column=0)

t = tk.StringVar()
temp_inp = tk.Entry(inp_frame, width=10, font="Calibri 14", textvariable=t)
temp_inp.grid(row=0, column=1)

# Menu Frame
menu_frame = tk.Frame(window)
menu_frame.pack(padx=20, pady=(5,15))

opt = ["℃", "℉", "K"]

m1 = tk.StringVar()
m1.set("℃")
menu1 = tk.OptionMenu(menu_frame, m1, *opt)
menu1.config(font="Calibri 15")
men1 = menu1.nametowidget(menu1.menuname)
men1.configure(font=("Calibri", 15))
menu1.grid(row=0, column=0)

to_lab = tk.Label(menu_frame, text="→", font="Calibri 15")
to_lab.grid(row=0,column=1, padx=10)

m2 = tk.StringVar()
m2.set("℉")
menu2 = tk.OptionMenu(menu_frame, m2, *opt)
menu2.config(font="Calibri 15")
men2 = menu2.nametowidget(menu2.menuname)
men2.configure(font=("Calibri", 15))
menu2.grid(row=0, column=2)

swap_btn = tk.Button(menu_frame, text="⇄", font="Calibri 15", height=1, command=swap)
swap_btn.grid(row=0, column=3, padx=(50,10))

convert_btn = tk.Button(window, text="Convert", font="Calibri 15", command=convert)
convert_btn.pack(ipadx=15, pady=(5,15))

out_lab = tk.Label(window, text="", font="Calibri 15")
out_lab.pack(pady=(5,20))

window.mainloop()