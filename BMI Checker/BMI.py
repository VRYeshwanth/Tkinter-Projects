import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('BMI Calculator')
window.iconbitmap(r'C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\BMI Checker\bmi.ico')
window.resizable(0,0)

def calculate():
    try:
        weight = float(w.get())
        height = float(h.get())
        height = height / 100
        bmi = weight/(height ** 2)
        if bmi <= 18.4:
            output.config(text=f"BMI = {round(bmi,2)}\nUnderweight")
        elif bmi <= 24.9:
            output.config(text=f"BMI = {round(bmi,2)}\nNormal")
        elif bmi <= 39.9:
            output.config(text=f"BMI = {round(bmi,2)}\nOverweight")
        else:
            output.config(text=f"BMI = {round(bmi,2)}\nObese")
    except ValueError:
        messagebox.showerror("ERROR", "Please enter numbers only")

inp_frame = tk.Frame(window)
inp_frame.pack()

w_label = tk.Label(inp_frame, text="Enter your weight (in kg) : ", font="Calibri 18")
w_label.grid(row=0, column=0, sticky="W", padx=20, pady=20)

w = tk.StringVar()
w_inp = tk.Entry(inp_frame, font="Calibri 15", width=10, textvariable=w)
w_inp.grid(row=0, column=1, sticky="W", padx=20, pady=20)

h_label = tk.Label(inp_frame, text="Enter your height (in cm) : ", font="Calibri 18")
h_label.grid(row=1, column=0, sticky="W", padx=20, pady=20)

h = tk.StringVar()
h_inp = tk.Entry(inp_frame, font="Calibri 15", width=10, textvariable=h)
h_inp.grid(row=1, column=1, sticky="W", padx=20, pady=20)

calc_btn = tk.Button(window, text="Calculate", font="Calibri 18", command=calculate)
calc_btn.pack()

output = tk.Label(window, font="Calibri 18", text="")
output.pack(padx=10, pady=25)

window.mainloop()