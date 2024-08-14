import tkinter as tk
from tkinter import filedialog, messagebox
import qrcode


def select_file():
    file_path = filedialog.askopenfilename(
        title="Select a file containing the YouTube link",
        filetypes=(("Text files", "*.txt"), ("All files", "*.*"))
    )
    if file_path:
        with open(file_path, 'r') as file:
            youtube_link.set(file.read().strip())


def generate_qrcode():
    link = youtube_link.get()
    if not link:
        messagebox.showerror("Error", "No link provided!")
        return

    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")

    save_path = filedialog.asksaveasfilename(
        defaultextension=".png",
        filetypes=(("PNG files", "*.png"), ("All files", "*.*")),
        title="Save QR Code"
    )
    if save_path:
        img.save(save_path)
        messagebox.showinfo("Success", f"QR code saved as '{save_path}'")


# Create main application window
root = tk.Tk()
root.title("YouTube QR Code Generator")

youtube_link = tk.StringVar()

# Create and place widgets
tk.Label(root, text="YouTube Link:").pack(pady=5)
link_entry = tk.Entry(root, textvariable=youtube_link, width=50)
link_entry.pack(pady=5)

select_button = tk.Button(root, text="Select File with Link", command=select_file)
select_button.pack(pady=5)

generate_button = tk.Button(root, text="Generate QR Code", command=generate_qrcode)
generate_button.pack(pady=20)

# Run the application
root.mainloop()
