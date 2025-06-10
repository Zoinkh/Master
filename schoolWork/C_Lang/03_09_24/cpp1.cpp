 #include <iostream>
#include <string>
#include <fstream>
#include <filesystem>
#include <algorithm>
#include <vector>
using namespace std;
namespace fs = filesystem;

//------------------define variable----------------------------
struct Staffdata
{
    string id, name, sex, address;
    int age, phone;
    float salary;

    // toString function to return the staff information as a formatted string
    string toString() {
        return id + " " + name + " " + sex + " " + to_string(age) + " " + address + " " + to_string(phone) + " " + to_string(salary);
    }
};

//------------------------menu()------------------------------
class Func; // Forward declaration

class Menu
{
public:
    Staffdata Staff;
    Func* func; // pointer to Func class

    Menu() {
        func = new Func();
    }

    Menu() {
        delete func;
    }

    int run()
    {
        string userInput;
        do {
            cout << "*************************Menu:**************************\n\tr to Read\n\tw to Write\n\tx to Exit" << endl;
            cin >> userInput;

            if (userInput == "w") {
                do {
                    cout << "**************************Menu:*************************\n\tn to New\n\te to Edit\n\td to Delete\n\tx to Exit" << endl;
                    cin >> userInput;
                    system("clear");

                    if (userInput == "n") {
                        system("clear");
                        cout << "**************************New_File Menu:*************************\n\tFile Name : ";
                        string fileName;
                        cin >> fileName;
                        func->newFile(fileName);
                        fileForm(); // Fill form
                        func->writeToFile(fileName, Staff);
                    } else if (userInput == "e") {
                        system("clear");
                        cout << "**************************Edit_File Menu:*************************\n\tList Files";
                        func->listDir();
                        cout << "File Name : ";
                        string fileName;
                        cin >> fileName;
                        func->editFile(fileName);
                    } else if (userInput == "d") {
                        system("clear");
                        cout << "**************************Delete_File Menu:*************************\n\tFile Name : ";
                        string fileName;
                        cin >> fileName;
                        cout << "File Deleted: " << fileName << endl;
                        func->deleteFile(fileName);
                    }
                } while (userInput != "x");
            } else if (userInput == "r") {
                do {
                    cout << "**************************Read_Mode Menu:*************************\n\ta to List all Files\n\ts to Search\n\tx to Exit" << endl;
                    cin >> userInput;

                    if (userInput == "a") {
                        system("clear");
                        cout << "**************************List_All_Files*************************\n";
                        func->listDir();
                        cout << "File Name : ";
                        string fileName;
                        cin >> fileName;
                        func->readFile(fileName);
                    } else if (userInput == "s") {
                        system("clear");
                        cout << "**************************Search_File Menu:*************************\n\tFile Name : ";
                        string fileName, searchID;
                        cin >> fileName;
                        cout << "\tStaff ID: ";
                        cin >> searchID;
                        func->searchData(fileName, searchID);
                    }
                } while (userInput != "x");
            }

        } while (userInput != "x");

        return 0;
    }

    void fileForm() {
        cout << "**************************Fill_Form:*************************\n";
        cout << "STAFF ID :";
        cin >> Staff.id;
        cout << "STAFF NAME :";
        cin >> Staff.name;
        cout << "SEX :";
        cin >> Staff.sex;
        cout << "AGE :";
        cin >> Staff.age;
        cout << "ADDRESS :";
        cin >> Staff.address;
        cout << "PHONE :";
        cin >> Staff.phone;
        cout << "SALARY :";
        cin >> Staff.salary;
    }
};

//------------------------------------------------------------

//------------------------------MODS--------------------------
class Func
{
public:

    void newFile(const string& filename) {
        string dirPath = "Staff";
        try {
            if (fs::create_directory(dirPath)) {
                cout << "Directory created successfully." << endl;
            } else {
                cout << "Directory already exists or could not be created." << endl;
            }
        } catch (const fs::filesystem_error& e) {
            cerr << "Filesystem error: " << e.what() << endl;
        }

        ofstream MyFile("Staff/" + filename + ".txt");
        MyFile.close();
    }

    void editFile(const string& filename) {
        string path = "Staff/" + filename + ".txt";
        ifstream infile(path);
        if (!infile.is_open()) {
            cerr << "Could not open the file for reading!" << endl;
            return;
        }

        string content;
        string line;
        while (getline(infile, line)) {
            content += line + "\n";
        }
        infile.close();

        string oldText = "oldText"; // Placeholder for actual text you want to replace
        string newText = "newText"; // Placeholder for new text

        size_t pos = content.find(oldText);
        if (pos != string::npos) {
            content.replace(pos, oldText.length(), newText);
        }

        ofstream outfile(path);
        outfile << content;
        outfile.close();
        cout << "File updated successfully." << endl;
    }

    void deleteFile(const string& filename) {
        string path = "Staff/" + filename + ".txt";
        int status = remove(path.c_str());
        if (status != 0) {
            perror("Error deleting file");
        } else {
            cout << "File successfully deleted" << endl;
        }
    }

    void readFile(const string& filename) {
        ifstream inputFile("Staff/" + filename + ".txt");
        if (!inputFile.is_open()) {
            cerr << "Error opening the file!" << endl;
            return;
        }

        string line;
        cout << "File Content: " << endl;
        while (getline(inputFile, line)) {
            cout << line << endl;
        }
        inputFile.close();
    }

    void searchData(const string& filename, const string& searchID) {
        string path = "Staff/" + filename + ".txt";
        ifstream file(path);
        if (!file.is_open()) {
            cerr << "Error opening file: " << filename << endl;
            return;
        }

        string line;
        bool found = false;
        while (getline(file, line)) {
            if (line.find(searchID) != string::npos) {
                cout << "ID found: " << line << endl;
                found = true;
                break;
            }
        }

        if (!found) {
            cout << "ID not found in the file." << endl;
        }
        file.close();
    }

    void listDir() {
        string path = "Staff";
        try {
            if (fs::exists(path) && fs::is_directory(path)) {
                cout << "Listing files in directory: " << path << endl;
                for (const auto& entry : fs::directory_iterator(path)) {
                    cout << entry.path().filename().string() << endl;
                }
            } else {
                cerr << "The specified path is not a valid directory." << endl;
            }
        } catch (const fs::filesystem_error& e) {
            cerr << "Filesystem error: " << e.what() << endl;
        }
    }

    void writeToFile(const string& filename, const Staffdata& staff) {
        ofstream file("Staff/" + filename + ".txt", ios::app); // Open file in append mode
        if (!file) {
            cerr << "Could not open the file!" << endl;
            return;
        }
        file << staff.toString() << endl;
        file.close();
        cout << "Written to " << filename << " successfully." << endl;
    }
};

//-------------------------Main Block-------------------------
int main() {
    Menu menu;
    menu.run();
    return 0;
}
//------------------------------------------------------------

