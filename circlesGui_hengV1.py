# New version of circlesGui_hengV1.py  29July2023
# Version1 include comments at beginning same diameter sorted group 30 July 2023

import tkinter as tk
from tkinter import filedialog
import ezdxf


def extract_circles(input_file, output_file):
    try:
        doc = ezdxf.readfile(input_file)
        msp = doc.modelspace()

        num_coord = 0
        circles_data = []
        for entity in msp:
            if entity.dxftype() == 'CIRCLE':
                center = entity.dxf.center
                diameter = entity.dxf.radius * 2
                circles_data.append({"Center": center, "Diameter": diameter})
                num_coord += 1

        # Sort circles_data based on diameter in ascending order
        sorted_circles = sorted(circles_data, key=lambda x: x["Diameter"])

        with open(output_file, 'w') as f:
            f.write(f'(DXF FILE: {input_file})\n')
            f.write(f'(TXT FILE: {output_file})\n')
            f.write(f'{num_coord} \n')
            f.write(("(Coord X,Y) \n"))
            current_diameter = None
            for data in sorted_circles:
                center = data["Center"]
                diameter = data["Diameter"]
                if diameter != current_diameter:
                    f.write(f'\n(circles with same diameter {diameter:.2f})\n')
                    current_diameter = diameter
                f.write(f'54, {center[0]:.4f}, {center[1]:.4f} \n')

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
    output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
    if output_file:
        extract_circles(input_file, output_file)


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
