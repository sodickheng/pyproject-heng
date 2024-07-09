# Version3 select one dxf and output multiple sorted diameter text files and overwrite previous generated text files.
# 31 July 2023
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

        # Sort circles_data based on diameter in ascending order in one horizontal list
        sorted_circles = sorted(circles_data, key=lambda x: x["Diameter"])

        # Group circles_data based on sorted diameter in one vertical list
        grouped_data = {}
        for data in sorted_circles:
            diameter = data["Diameter"]
            if diameter not in grouped_data:
                grouped_data[diameter] = []
            grouped_data[diameter].append(data)

        # output filename in three sorted diameter filename
        for diameter, data_list in grouped_data.items():
            filename = f"dia_{diameter:.2f}.txt"
            output_file = f"{output_folder}/{filename}"

            # Check if the file already exists and delete it for overwrite
            if os.path.exists(output_file):
                os.remove(output_file)

            # write data into files
            with open(output_file, 'w') as f:
                f.write(f'({output_file})\n')
                f.write(f"(Circles with Diameter {diameter:.2f})\n")

                f.write(f'(coord x,y)\n')
                total_circles = 0
                for data in data_list:
                    center = data["Center"]
                    diameter = data["Diameter"]
                    # f.write(f"Center: ({center[0]}, {center[1]}), Diameter: {diameter}\n")
                    f.write(f"54, {center[0]:.4f}, {center[1]:.4f}\n")
                    total_circles += 1
                f.write(f'(Total drill holes: {total_circles})\n')

        print('Extraction, sorting, and grouping successful.')
        status_label.config(text="Extraction, sorting, and grouping successful.", fg="green")
    except IOError:
        print('Error reading or writing files.')
        status_label.config(text="Error reading or writing files.", fg="red")


def open_file():
    input_file = filedialog.askopenfilename(filetypes=[("DXF Files", "*.dxf")])
    if input_file:
        save_folder(input_file)


def save_folder(input_file):
    output_folder = filedialog.askdirectory()
    if output_folder:
        extract_circles(input_file, output_folder)


window = tk.Tk()
window.title("DXF To TXT")
window.geometry("300x120")

# Label for status messages
status_label = tk.Label(window, text="")
status_label.pack(pady=5)

# Button to select DXF file
select_button = tk.Button(window, text="Select DXF File", height=3, width=20, command=open_file)
select_button.pack(pady=10)

# Run the GUI loop
window.mainloop()
