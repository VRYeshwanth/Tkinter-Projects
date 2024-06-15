import tkinter as tk

window = tk.Tk()
window.title("Electronic Configuration Finder")
window.iconbitmap(r"C:\Users\yeshw\OneDrive\Desktop\Tkinter-Projects\Electronic Confguration\Atom.ico")

data = {
    "H": "1s1",
    "He": "1s2",
    "Li": "1s2 2s1",
    "Be": "1s2 2s2",
    "B": "1s2 2s2 2p1",
    "C": "1s2 2s2 2p2",
    "N": "1s2 2s2 2p3",
    "O": "1s2 2s2 2p4",
    "F": "1s2 2s2 2p5",
    "Ne": "1s2 2s2 2p6",
    "Na": "1s2 2s2 2p6 3s1",
    "Mg": "1s2 2s2 2p6 3s2",
    "Al": "1s2 2s2 2p6 3s2 3p1",
    "Si": "1s2 2s2 2p6 3s2 3p2",
    "P": "1s2 2s2 2p6 3s2 3p3",
    "S": "1s2 2s2 2p6 3s2 3p4",
    "Cl": "1s2 2s2 2p6 3s2 3p5",
    "Ar": "1s2 2s2 2p6 3s2 3p6",
    "K": "1s2 2s2 2p6 3s2 3p6 4s1",
    "Ca": "1s2 2s2 2p6 3s2 3p6 4s2",
    "Sc": "1s2 2s2 2p6 3s2 3p6 3d1 4s2",
    "Ti": "1s2 2s2 2p6 3s2 3p6 3d2 4s2",
    "V": "1s2 2s2 2p6 3s2 3p6 3d3 4s2",
    "Cr": "1s2 2s2 2p6 3s2 3p6 3d5 4s1",
    "Mn": "1s2 2s2 2p6 3s2 3p6 3d5 4s2",
    "Fe": "1s2 2s2 2p6 3s2 3p6 3d6 4s2",
    "Co": "1s2 2s2 2p6 3s2 3p6 3d7 4s2",
    "Ni": "1s2 2s2 2p6 3s2 3p6 3d8 4s2",
    "Cu": "1s2 2s2 2p6 3s2 3p6 3d10 4s1",
    "Zn": "1s2 2s2 2p6 3s2 3p6 3d10 4s2",
    "Ga": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p1",
    "Ge": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p2",
    "As": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p3",
    "Se": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p4",
    "Br": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p5",
    "Kr": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6",
    "Rb": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s1",
    "Sr": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 5s2",
    "Y": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d1 5s2",
    "Zr": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d2 5s2",
    "Nb": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d4 5s1",
    "Mo": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s1",
    "Tc": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d5 5s2",
    "Ru": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d7 5s1",
    "Rh": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d8 5s1",
    "Pd": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10",
    "Ag": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s1",
    "Cd": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2",
    "In": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p1",
    "Sn": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p2",
    "Sb": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p3",
    "Te": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p4",
    "I": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p5",
    "Xe": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6",
    "Cs": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 6s1",
    "Ba": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 6s2",
    "La": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 5s2 5p6 5d1 6s2",
    "Ce": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f1 5s2 5p6 5d1 6s2",
    "Pr": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f3 5s2 5p6 6s2",
    "Nd": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f4 5s2 5p6 6s2",
    "Pm": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f5 5s2 5p6 6s2",
    "Sm": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f6 5s2 5p6 6s2",
    "Eu": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f7 5s2 5p6 6s2",
    "Gd": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f7 5s2 5p6 5d1 6s2",
    "Tb": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f9 5s2 5p6 6s2",
    "Dy": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f10 5s2 5p6 6s2",
    "Ho": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f11 5s2 5p6 6s2",
    "Er": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f12 5s2 5p6 6s2",
    "Tm": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f13 5s2 5p6 6s2",
    "Yb": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 6s2",
    "Lu": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d1 6s2",
    "Hf": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d2 6s2",
    "Ta": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d3 6s2",
    "W": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d4 6s2",
    "Re": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d5 6s2",
    "Os": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d6 6s2",
    "Ir": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d7 6s2",
    "Pt": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d9 6s1",
    "Au": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s1",
    "Hg": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2",
    "Tl": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p1",
    "Pb": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p2",
    "Bi": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p3",
    "Po": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p4",
    "At": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p5",
    "Rn": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6",
    "Fr": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 7s1",
    "Ra": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 7s2",
    "Ac": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 6d1 7s2",
    "Th": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 6s2 6p6 6d2 7s2",
    "Pa": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f2 6s2 6p6 6d1 7s2",
    "U": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f3 6s2 6p6 6d1 7s2",
    "Np": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f4 6s2 6p6 6d1 7s2",
    "Pu": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f6 6s2 6p6 7s2",
    "Am": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f7 6s2 6p6 7s2",
    "Cm": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f7 6s2 6p6 6d1 7s2",
    "Bk": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f9 6s2 6p6 7s2",
    "Cf": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f10 6s2 6p6 7s2",
    "Es": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f11 6s2 6p6 7s2",
    "Fm": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f12 6s2 6p6 7s2",
    "Md": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f13 6s2 6p6 7s2",
    "No": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 7s2",
    "Lr": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 7s2 7p1",
    "Rf": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d2 7s2",
    "Db": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d3 7s2",
    "Sg": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d4 7s2",
    "Bh": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d5 7s2",
    "Hs": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d6 7s2",
    "Mt": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d7 7s2",
    "Ds": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d8 7s2",
    "Rg": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d9 7s2",
    "Cn": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2",
    "Nh": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p1",
    "Fl": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p2",
    "Mc": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p3",
    "Lv": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p4",
    "Ts": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p5",
    "Og": "1s2 2s2 2p6 3s2 3p6 3d10 4s2 4p6 4d10 4f14 5s2 5p6 5d10 5f14 6s2 6p6 6d10 7s2 7p6"
}

def display():
    num = val.get()
    if num >= 1 and num <= 118:
        for index, (key,value) in enumerate(data.items()):
            if num == index+1:
                output_display.set(f"{key} = {value}")
            else:
                continue
        inp.delete(0,tk.END)
    else:
        output_display.set("Invalid atomic number")

heading = tk.Label(window, text="Enter the atomic number : ", font="Calibri 18 bold")
heading.grid(row=0, column=0)

val = tk.IntVar(value="")
inp = tk.Entry(window, width=20, textvariable=val)
inp.grid(row=0, column=1)

inp_btn = tk.Button(window, text="ENTER", command=display, font="Calibri 14")
inp_btn.grid(row=1, columnspan=2, ipadx=10)

output_display = tk.StringVar()
output = tk.Label(window, text="", textvariable=output_display, width=90, font="Calibri 15")
output.grid(row=2, columnspan=2, pady=10)

window.mainloop()