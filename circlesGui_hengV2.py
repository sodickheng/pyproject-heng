# New version of circlesGui_hengV1.py  29July2023
# Version2 include comments at beginning same diameter sorted group 30 July 2023
# and save sorted diameter to different filename through Gui


import tkinter as tk
from tkinter import filedialog
import ezdxf
import os


def extract_circles(input_file, output_folder):
    try:
        doc = ezdxf.readfile(input_file)
        msp = doc.modelspace()

        circles_data = []
        for entity in msp:
            if entity.dxftype() == 'CIRCLE':
                center = entity.dxf.center
                diameter = entity.dxf.radius * 2
                circles_data.append({"Center": center, "Diameter": diameter})

        # Sort circles_data based on diameter in ascending order
        sorted_circles = sorted(circles_data, key=lambda x: x["Diameter"])

        current_diameter = None
        current_file = None
        for data in sorted_circles:
            center = data["Center"]
            diameter = data["Diameter"]
            if diameter != current_diameter:
                if current_file:
                    current_file.close()

                    # Prompt the user to enter the new filename for the current diameter group
                    new_filename = filedialog.asksaveasfilename(defaultextension=".txt",
                                                                filetypes=[("Text Files", "*.txt")],
                                                                initialdir=output_folder,
                                                                initialfile=f"Cir_D{diameter}")
                    if not new_filename:
                        continue

                filename = os.path.join(output_folder,  f'circles with same diameter {diameter:.2f}\n')
                current_file = open(filename, 'w')
                current_file.write(f'circles with same dia {diameter:.2f} \n')
                current_diameter = diameter
            current_file.write(f'54, {center[0]:.4f}, {center[1]:.4f} \n')

        if current_file:
            current_file.close()

        print('Extraction and sorting successful.')
        status_label.config(text="Extraction and sorting successful.", fg="green")
    except IOError:
        print('Error reading or writing files.')
        status_label.config(text="Error reading or writing files.", fg="red")


def open_file():
    input_file = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if input_file:
        save_file(input_file)

def save_file(input_file):
    output_folder = filedialog.askdirectory()
    if output_folder:
        extract_circles(input_file, output_folder)


window = tk.Tk()
window.title("DXF Circle Data Extractor")
window.geometry("300x120")

# Label for status messages
status_label = tk.Label(window, text="")
status_label.pack(pady=5)

# Button to select DXF file
select_button = tk.Button(window, text="Select DXF File", height=3, width=20, command=open_file)
select_button.pack(pady=10)

# Run the GUI loop
window.mainloop()
