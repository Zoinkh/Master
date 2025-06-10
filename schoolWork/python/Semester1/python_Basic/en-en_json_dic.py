import json

def load_dictionary(filename):
    """Loads a dictionary from a JSON file."""
    try:
        with open(filename, "r") as file:
            dictionary = json.load(file)
        return dictionary
    except FileNotFoundError:
        return {}  # Return an empty dictionary if the file doesn't exist.
    except json.JSONDecodeError:
        print(f"Error: JSON decoding failed for file '{filename}'.")
        return {}  # Return an empty dictionary in case of decoding error.

def save_dictionary(dictionary, filename):
    """Saves a dictionary to a JSON file."""
    try:
        with open(filename, "w") as file:
            json.dump(dictionary, file, indent=2)
    except PermissionError:
        print(f"Error: Permission denied to write to the file '{filename}'.")

def add_word(dictionary, word, meaning):
    """Adds a word and its meaning to the dictionary."""
    dictionary[word.lower()] = meaning

def lookup_word(dictionary, word):
    """Looks up the meaning of a word in the dictionary."""
    word = word.lower()
    return dictionary.get(word, f"The meaning of '{word}' is not found in the dictionary.")

def display_dictionary(dictionary):
    """Displays the dictionary in a formatted way."""
    print("\nDictionary:")
    for word, meaning in dictionary.items():
        print(f"{word.capitalize()}: {meaning}")

def main():
    """Main function to run the dictionary program."""
    dictionary_filename = "dictionary.json"
    dictionary = load_dictionary(dictionary_filename)

    # Example usage (you can add more functionality here)
    add_word(dictionary, "apple", "A round fruit with red or green skin and a white flesh.")
    add_word(dictionary, "banana", "A long curved fruit with yellow skin and soft sweet flesh.")
    save_dictionary(dictionary, dictionary_filename)

    print(lookup_word(dictionary, "apple"))
    print(lookup_word(dictionary, "grape"))  # Example of a word not found

    display_dictionary(dictionary)

if __name__ == "__main__":
    main()
