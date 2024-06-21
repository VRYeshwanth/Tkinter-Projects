import tkinter as tk
from tkinter import messagebox

window = tk.Tk()
window.title('Base Convertor')
window.iconbitmap(r'C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\Number System Convertor\base.ico')
window.resizable(0,0)

frame = tk.Frame(window)
frame.pack()

def check_hex(i):
    for ch in i.upper():
        if ((ch < '0' or ch > '9') and (ch < 'A' or ch > 'F')):
            return False
    return True

def convert():
    c1 = d1.get()
    c2 = d2.get()
    inp = ie.get()
    if c1 == c2:
        if c1 == "Binary":
            if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
            if all(ch == '0' or ch == '1' for ch in inp) == False:
                messagebox.showerror("ERROR", "Please enter a binary number")
            else:
                oe.set(inp)
        if c1 == "Decimal":
            if not inp.isdigit() and inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
            elif not inp.isdigit():
                messagebox.showerror("ERROR", "Please enter a decimal number")
            else:
                oe.set(inp)
        if c1 == "Octal":
            if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
            if all(ch >= '0' and ch <= '7' for ch in inp) == False:
                messagebox.showerror("ERROR", "Please enter an octal number")
            else:
                oe.set(inp)
        if c1 == "Hexadecimal":
            if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
            if check_hex(inp):
                oe.set(inp)
            else:
                messagebox.showerror("ERROR", "Please enter a hexadecimal number")
    
    if c1 == "Binary" and c2 == "Decimal":
        if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
        if all(ch == '0' or ch == '1' for ch in inp) == False:
            messagebox.showerror("ERROR", "Please enter a binary number")
        else:
            oe.set(int(inp, 2))
    
    if c1 == "Binary" and c2 == "Octal":
        if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
        if all(ch == '0' or ch == '1' for ch in inp) == False:
            messagebox.showerror("ERROR", "Please enter a binary number")
        else:
            s = int(inp, 2)
            num = ""
            while s > 0:
                r = s % 8
                num += str(r)
                s //= 8
            oe.set(num[::-1])
    
    if c1 == "Binary" and c2 == "Hexadecimal":
        if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
        if all(ch == '0' or ch == '1' for ch in inp) == False:
            messagebox.showerror("ERROR", "Please enter a binary number")
        else:
            s = int(inp, 2)
            num = ""
            while s > 0:
                rem = s % 16
                if rem == 10:
                    num = 'A' + num
                elif rem == 11:
                    num = 'B' + num
                elif rem == 12:
                    num = 'C' + num
                elif rem == 13:
                    num = 'D' + num
                elif rem == 14:
                    num = 'E' + num
                elif rem == 15:
                    num = 'F' + num
                else:
                    num = str(rem) + num
                s //= 16
            oe.set(num)

    if c1 == "Decimal" and c2 == "Binary":
        if not inp.isdigit():
            messagebox.showerror("ERROR", "Please enter a decimal number")
        else:
            n = int(inp)
            s = ""
            while n > 0:
                rem = n % 2
                s = str(rem) + s
                n //= 2
            oe.set(s)
    
    if c1 == "Decimal" and c2 == "Octal":
        if not inp.isdigit():
            messagebox.showerror("ERROR", "Please enter a decimal number")
        else:
            n = int(inp)
            s = ""
            while n > 0:
                rem = n % 8
                s = str(rem) + s
                n //= 8
            oe.set(s)
    
    if c1 == "Decimal" and c2 == "Hexadecimal":
        if not inp.isdigit():
            messagebox.showerror("ERROR", "Please enter a decimal number")
        else:
            n = int(inp)
            s = ""
            while n > 0:
                rem = n % 16
                if rem == 10:
                    s = 'A' + s
                elif rem == 11:
                    s = 'B' + s
                elif rem == 12:
                    s = 'C' + s
                elif rem == 13:
                    s = 'D' + s
                elif rem == 14:
                    s = 'E' + s
                elif rem == 15:
                    s = 'F' + s
                else:
                    s = str(rem) + s
                n //= 16
            oe.set(s)
    
    if c1 == "Octal" and c2 == "Binary":
        if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
        if all(ch >= '0' and ch <= '7' for ch in inp) == False:
            messagebox.showerror("ERROR", "Please enter an octal number")
        else:
            s = int(inp, 8)
            val = ""
            while s > 0:
                rem = s % 2
                val = str(rem) + val
                s //= 2
            oe.set(val)
    
    if c1 == "Octal" and c2 == "Decimal":
        if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
        if all(ch >= '0' and ch <= '7' for ch in inp) == False:
            messagebox.showerror("ERROR", "Please enter an octal number")
        else:
            oe.set(int(inp, 8))
    
    if c1 == "Octal" and c2 == "Hexadecimal":
        if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
        if all(ch >= '0' and ch <= '7' for ch in inp) == False:
            messagebox.showerror("ERROR", "Please enter an octal number")
        else:
            s = int(inp, 8)
            val = ""
            while s > 0:
                rem = s % 16
                if rem == 10:
                    val = 'A' + val
                elif rem == 11:
                    val = 'B' + val
                elif rem == 12:
                    val = 'C' + val
                elif rem == 13:
                    val = 'D' + val
                elif rem == 14:
                    val = 'E' + val
                elif rem == 15:
                    val = 'F' + val
                else:
                    val = str(rem) + val
                s //= 16
            oe.set(val)
    
    if c1 == "Hexadecimal" and c2 == "Binary":
        if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
        if not check_hex(inp):
            messagebox.showerror("ERROR", "Please enter a hexadecimal number")
        else:
            n = int(inp, 16)
            s = ""
            while n > 0:
                rem = n % 2
                s = str(rem) + s
                n //= 2
            oe.set(s)
    
    if c1 == "Hexadecimal" and c2 == "Decimal":
        if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
        if not check_hex(inp):
            messagebox.showerror("ERROR", "Please enter a hexadecimal number")
        else:
            oe.set(int(inp, 16))
    
    if c1 == "Hexadecimal" and c2 == "Octal":
        if inp == "":
                messagebox.showerror("ERROR", "Please enter a number")
        if not check_hex(inp):
            messagebox.showerror("ERROR", "Please enter a hexadecimal number")
        else:
            n = int(inp, 16)
            s = ""
            while n > 0:
                rem = n % 8
                s = str(rem) + s
                n //= 8
            oe.set(s)

opt = ["Binary", "Decimal", "Octal", "Hexadecimal"]

inp_head = tk.Label(frame, text="Input number : ", font="Calibri 15")
inp_head.grid(row=0, column=0, sticky="W", padx=10, pady=(20,10))

ie = tk.StringVar()
inp_entry = tk.Entry(frame, font="Calibri 15", textvariable=ie)
inp_entry.grid(row=0, column=1, sticky="W", padx=10, pady=(20,10))

from_head = tk.Label(frame, text="From : ", font="Calibri 15")
from_head.grid(row=1, column=0, sticky="W", padx=10, pady=(0,10))

d1 = tk.StringVar()
d1.set("Binary")
dd1 = tk.OptionMenu(frame, d1, *opt)
dd1.grid(row=1, column=1, sticky="W", padx=10, pady=(0,10))
dd1.config(width=10, font="Calibri 15")
menu1 = dd1.nametowidget(dd1.menuname)
menu1.configure(font=("Calibri", 15))

to_head = tk.Label(frame, text="To : ", font="Calibri 15")
to_head.grid(row=2, column=0, sticky="W", padx=10, pady=(0,10))

d2 = tk.StringVar()
d2.set("Binary")
dd2 = tk.OptionMenu(frame, d2, *opt)
dd2.grid(row=2, column=1, sticky="W", padx=10, pady=(0,10))
dd2.config(font="Calibri 15", width=10)
menu2 = dd2.nametowidget(dd2.menuname)
menu2.configure(font=("Calibri", 15))

out_head = tk.Label(frame, text="Output : ", font="Calibri 15")
out_head.grid(row=4, column=0, sticky="W", padx=10, pady=(0,10))

oe = tk.StringVar()
out_entry = tk.Entry(frame, font="Calibri 15", textvariable=oe)
out_entry.grid(row=4, column=1, sticky="W", padx=10, pady=(0,10))

btn = tk.Button(frame, text="Convert", command=convert, font="Calibri 15")
btn.grid(row=5, columnspan=2, padx=15, pady=15, ipadx=15)

window.mainloop()