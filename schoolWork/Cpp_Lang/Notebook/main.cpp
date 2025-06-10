#include <iostream>
#include <fstream>
#include <vector>
#include <string>

using namespace std;

vector<string> notes;
const string filename = "note.txt";

void loadNotes() {
    ifstream file(filename);
    string line;
    while (getline(file, line)) {
        notes.push_back(line);
    }
    file.close();
}

void saveNotes() {
    ofstream file(filename);
    for (const string& note : notes) {
        file << note << endl;
    }
    file.close();
}

void showMenu() {
    cout << "\n--- Notebook Menu ---" << endl;
    cout << "1. Add a Note" << endl;
    cout << "2. View Notes" << endl;
    cout << "3. Delete a Note" << endl;
    cout << "4. Exit" << endl;
    cout << "Enter your choice: ";
}

void addNote() {
    cout << "Enter your note: ";
    cin.ignore(); // Clear input buffer
    string note;
    getline(cin, note);
    notes.push_back(note);
    saveNotes();
    cout << "Note added and saved successfully!" << endl;
}

void viewNotes() {
    if (notes.empty()) {
        cout << "No notes to display!" << endl;
        return;
    }
    cout << "\n--- Your Notes ---" << endl;
    for (int i = 0; i < notes.size(); i++) {
        cout << i + 1 << ". " << notes[i] << endl;
    }
}

void deleteNote() {
    if (notes.empty()) {
        cout << "No notes to delete!" << endl;
        return;
    }
    viewNotes();
    cout << "Enter the note number to delete: ";
    int index;
    cin >> index;
    if (index < 1 || index > notes.size()) {
        cout << "Invalid note number!" << endl;
    } else {
        notes.erase(notes.begin() + index - 1);
        saveNotes();
        cout << "Note deleted and file updated!" << endl;
    }
}

int main() {
    loadNotes(); // Load notes at the start
    int choice;

    while (true) {
        showMenu();
        cin >> choice;

        switch (choice) {
            case 1:
                addNote();
                break;
            case 2:
                viewNotes();
                break;
            case 3:
                deleteNote();
                break;
            case 4:
                cout << "Exiting notebook... Goodbye!" << endl;
                return 0;
            default:
                cout << "Invalid choice! Please try again." << endl;
        }
    }

    return 0;
}
