import json

# Example data
data_to_write = {
    "name": "John Doe",
    "age": 30,
    "city": "Example City",
    "is_student": False,
    "grades": [90, 85, 78]
}

# Writing to a JSON file
json_filename = "example.json"

try:
    with open(json_filename, "w") as json_file:
        json.dump(data_to_write, json_file, indent=2)
except PermissionError:
    print(f"Error: Permission denied to write to the file '{json_filename}'.")

# Reading from the JSON file
try:
    with open(json_filename, "r") as json_file:
        data_read = json.load(json_file)
    print("Data read from JSON file:")
    print(data_read)
except FileNotFoundError:
    print(f"Error: The file '{json_filename}' not found.")
except PermissionError:
    print(f"Error: Permission denied to read the file '{json_filename}'.")
except json.JSONDecodeError:
    print(f"Error: JSON decoding failed for file '{json_filename}'.")
