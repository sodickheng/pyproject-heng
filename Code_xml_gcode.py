# cnc_job.xml
import xml.etree.ElementTree as ET

def parse_xml_to_gcode(xml_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    gcode = []

    # Iterate through the toolpath moves
    for move in root.find('ToolPath').findall('Move'):
        move_type = move.get('type')
        x = move.get('x')
        y = move.get('y')
        z = move.get('z')
        feed_rate = move.get('feedRate')

        # Convert the XML move to G-code
        if move_type == 'rapid':
            # G0 is for rapid moves
            gcode_line = f"G0 X{x} Y{y} Z{z}"
        elif move_type == 'cut':
            # G1 is for cutting moves (linear interpolation)
            gcode_line = f"G1 X{x} Y{y} Z{z}"
            if feed_rate:
                gcode_line += f" F{feed_rate}"
        else:
            # Unknown move type
            continue

        gcode.append(gcode_line)

    return gcode


# Example usage
xml_file = 'cnc_job.xml'
gcode = parse_xml_to_gcode(xml_file)

# Save the G-code to a file or print it
with open('output.gcode', 'w') as gcode_file:
    for line in gcode:
        gcode_file.write(line + '\n')

# Alternatively, print the generated G-code
for line in gcode:
    print(line)
