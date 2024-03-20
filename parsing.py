import sys
import csv
import json
import xml.etree.ElementTree as ET


def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()


def write_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for row in data:
            writer.writerow(row)


def write_json(data, filename):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)


def write_xml(data, filename):
    root = ET.Element("data")
    for item in data:
        row = ET.SubElement(root, "row")
        for key, value in item.items():
            child = ET.SubElement(row, key)
            child.text = str(value)
    tree = ET.ElementTree(root)
    tree.write(filename)


def convert_txt_to_xml(data):
    lines = data.split('\n')
    data_dict = [{'line': line} for line in lines]
    return data_dict


def main():
    if len(sys.argv) != 3:
        print("Usage: python program.py filename format (-c for CSV, -j for JSON, -x for XML)")
        return

    filename = sys.argv[1]
    format_arg = sys.argv[2]

    data = read_file(filename)

    if format_arg == '-c':
        lines = [line.split() for line in data.split('\n')]
        output_filename = filename.split('.')[0] + '.csv'
        write_csv(lines, output_filename)
        print(f"CSV file saved as {output_filename}")
    elif format_arg == '-j':
        output_filename = filename.split('.')[0] + '.json'
        write_json(data, output_filename)
        print(f"JSON file saved as {output_filename}")
    elif format_arg == '-x':
        data_dict = convert_txt_to_xml(data)
        output_filename = filename.split('.')[0] + '.xml'
        write_xml(data_dict, output_filename)
        print(f"XML file saved as {output_filename}")
    else:
        print("Invalid format argument. Use -c for CSV, -j for JSON, -x for XML")


if __name__ == "__main__":
    main()

