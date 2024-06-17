import tkinter as tk
from tkinter import messagebox
import random

window = tk.Tk()
window.title('Password Generator')
window.iconbitmap(r'C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\Password Generator\key.ico')

def generate(l):
    uppercase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowercase = "abcdefghijklmnopqrstuvwxyz"
    numbers = "0123456789"
    special = "@#$&*():;.,`/~-=+"
    total = ""
    if l < 8 or l > 256:
        messagebox.showwarning("WARNING", "Invalid length")
    else:
        if c1.get() == 0 and c2.get() == 0 and c3.get() == 0 and c4.get() == 0:
            messagebox.showwarning("WARNING", "Please select atleast one checkbox")
        else:
            if c1.get() == 1:
                total += uppercase
            if c2.get() == 1:
                total += lowercase
            if c3.get() == 1:
                total += numbers
            if c4.get() == 1:
                total += special
            pwd = ""
            for i in range(l):
                pwd += random.choice(total)
            output.config(state=tk.NORMAL)
            output.delete('1.0', tk.END)
            output.insert(tk.END, pwd)
            output.config(state=tk.DISABLED)


#Code for input
inp_frame = tk.Frame(window)
inp_frame.pack()

heading = tk.Label(inp_frame, text="Password Generator", font="Calibri 20 bold")
heading.grid(row=0, columnspan=2, padx=10, pady=10)

head = tk.Label(inp_frame, text="Enter the length of password (8 - 256): ", font="Calibri 15")
head.grid(row=1, column=0, padx=15, pady=10)

var = tk.IntVar()
var.set(8)
len_entry = tk.Entry(inp_frame, width=10, font="Calibri 15", textvariable=var)
len_entry.grid(row=1, column=1, padx=15, pady=10)

#Code for checkboxes and button
check_frame = tk.Frame(window)
check_frame.pack()

c1 = tk.IntVar()
c2 = tk.IntVar()
c3 = tk.IntVar()
c4 = tk.IntVar()

choice1 = tk.Checkbutton(check_frame,text="Uppercase", variable=c1, offvalue=0, onvalue=1, font="Calibri 15")
choice2 = tk.Checkbutton(check_frame,text="Lowercase", variable=c2, offvalue=0, onvalue=1, font="Calibri 15")
choice3 = tk.Checkbutton(check_frame,text="Numbers", variable=c3, offvalue=0, onvalue=1, font="Calibri 15")
choice4 = tk.Checkbutton(check_frame,text="Symbols", variable=c4, offvalue=0, onvalue=1, font="Calibri 15")

choice1.grid(row=0, column=0, sticky="W", pady=5)
choice2.grid(row=0, column=1, sticky="W", padx=20)
choice3.grid(row=1, column=0, sticky="W", pady=5)
choice4.grid(row=1, column=1, sticky="W", padx=20)

btn = tk.Button(check_frame, text="Generate", font="Calibri 15", command=lambda: generate(var.get()))
btn.grid(row=2, columnspan=2, pady=15, ipadx=15)

output = tk.Text(window, height=5, font="Calibri 15")
output.pack(padx=15, pady=(10,25))
output.config(state=tk.DISABLED)

window.mainloop()