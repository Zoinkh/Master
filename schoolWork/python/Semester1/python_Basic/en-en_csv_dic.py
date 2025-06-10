import csv

def load_dictionary_csv(filename):
    """Loads a dictionary from a CSV file."""
    try:
        with open(filename, mode='r', newline='', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            return {row['Key']: row['Value'] for row in reader}
    except FileNotFoundError:
        return {}
    except PermissionError:
        print(f"Error: Permission denied to read the file '{filename}'.")
        return {}

def save_dictionary_csv(dictionary, filename):
    """Saves a dictionary to a CSV file."""
    try:
        with open(filename, mode='w', newline='', encoding='utf-8') as file:
            fieldnames = ['Key', 'Value']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for key, value in dictionary.items():
                writer.writerow({'Key': key, 'Value': value})
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")

def add_entry(dictionary, key, value):
    """Adds an entry to the dictionary."""
    dictionary[key] = value

def lookup_entry(dictionary, key):
    """Looks up an entry in the dictionary."""
    return dictionary.get(key, f"No value found for key '{key}'.")

def display_dictionary_csv(dictionary):
    """Displays the dictionary."""
    print("Dictionary:")
    for key, value in dictionary.items():
        print(f"{key}: {value}")

def main():
    csv_filename = "dictionary.csv"
    dictionary = load_dictionary_csv(csv_filename)

    while True:
        print("Options:")
        print("1. Add an entry")
        print("2. Lookup an entry")
        print("3. Display dictionary")
        print("4. Save and exit")

        choice = input("Enter your choice (1/2/3/4): ")

        if choice == "1":
            key = input("Enter the key: ")
            value = input("Enter the value: ")
            add_entry(dictionary, key, value)
        elif choice == "2":
            key = input("Enter the key to lookup: ")
            result = lookup_entry(dictionary, key)
            print(result)
        elif choice == "3":
            display_dictionary_csv(dictionary)
        elif choice == "4":
            save_dictionary_csv(dictionary, csv_filename)
            print("Dictionary saved. Exiting.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
