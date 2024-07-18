import qrcode
from PIL import ImageTk
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_qr_code():
    text = entry.get()
    if not text:
        messagebox.showerror("Input Error", "Please enter some text to generate a QR code.")
        return
    
    try:
        qr = qrcode.QRCode(version=1, box_size=10, border=5)
        qr.add_data(text)
        qr.make(fit=True)
        img = qr.make_image(fill='black', back_color='white')
        
        
        img = img.resize((250, 250))
        img = ImageTk.PhotoImage(img)
        qr_label.config(image=img)
        qr_label.image = img
        save_button.config(state=tk.NORMAL)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def save_qr_code():
    try:
        file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
        if file_path:
            qr_image = qr_label.image._PhotoImage__photo
            qr_image.write(file_path, format="png")
            messagebox.showinfo("Save Success", f"QR code saved to {file_path}")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred while saving: {e}")

def reset():
    entry.delete(0, tk.END)
    qr_label.config(image='')
    qr_label.image = None
    save_button.config(state=tk.DISABLED)

window = tk.Tk()
window.title("QR Code Generator")

head = tk.Label(window, text="QR Code Generator", font="Calibri 20 bold")
head.pack(pady=10)

label = tk.Label(window, text="Enter text to generate QR code:", font="Calibri 15")
label.pack(pady=10)

entry = tk.Entry(window, width=30, font="Calibri 15")
entry.pack(pady=5)

generate_button = tk.Button(window, text="Generate QR Code", command=generate_qr_code, font="Calibri 15")
generate_button.pack(pady=10)

qr_label = tk.Label(window)
qr_label.pack(pady=10)

save_button = tk.Button(window, text="Save QR Code", command=save_qr_code, state=tk.DISABLED, font="Calibri 15")
save_button.pack(pady=10)

reset_button = tk.Button(window, text="Reset", command=reset, font="Calibri 15")
reset_button.pack(pady=10)

window.mainloop()