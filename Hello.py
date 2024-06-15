import tkinter as tk

window = tk.Tk()
window.title('Hello World')
window.geometry('375x150')

def print_name():
    inp = entry_inp.get()
    output_disp.set(f"Hello {inp}, welcome to Tkinter")
    name_inp.delete(0,tk.END)

frame_1 = tk.Frame(window)
frame_1.pack()

frame_2 = tk.Frame(window)
frame_2.pack()

name_ask = tk.Label(frame_1, text="What is your name ?", font="Calibri 15 bold")
name_ask.grid(row=0, column=0, padx=(10,0), pady=10)

entry_inp = tk.StringVar()
name_inp = tk.Entry(frame_1, width=25, textvariable=entry_inp)
name_inp.grid(row=0, column=1, padx=(10,0), pady=10)

btn = tk.Button(frame_1, text="ENTER", command=print_name)
btn.grid(row=1, columnspan=2, ipadx=10, ipady=5)

output_disp = tk.StringVar()
output = tk.Label(frame_2, text="", textvariable=output_disp, font="Calibri 15")
output.grid(row=2, columnspan=2)

window.mainloop()