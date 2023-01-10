import json


def generate_output(input_json, template_file, output_file):
    # Load the input data from the JSON file
    with open(input_json, 'r') as f:
        input_data = json.load(f)

    # Generate the lines of code for the items
    item_lines = []
    for collection_name, items in input_data.items():
        for item in items:
            item_lines.append("initDataItem(\"{name}\", {tag}, \"{type}\", {size});".format(**item))

    print(item_lines)

# Example usage
generate_output("input_example.json", "template.cpp", "output_example.cpp")
