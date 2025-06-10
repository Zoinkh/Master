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
	string id[5],
	       name[10],
	       sex[5],
	       adres[10],
	       userInput;
	int age, phone;
	float salary;
	 string toString() {
        return id + " " + name + " " + sex + " " + to_string(age) + " " + address + " " + to_string(phone) + " " + to_string(salary);
    }
};
//------------------------------------------------------------


//------------------------menu()------------------------------
class Menu : public Func
{
public:
	Staffdata Staff;
	int run()
	{
		do
		{
			cout << "*************************Menu:**************************\n\tr to Read\n\tw to Write\n\tx to Exit" << endl;
			cin >> Staff.userInput;

			if (Staff.userInput == "w") {
				do
				{
					cout << "**************************Menu:*************************\n\tn to New\n\te to Filen\n\td to Delete" << endl;
					cin >> Staff.userInput;
                       system("clear");
					if (Staff.userInput == "n") {
                        system("clear");
						cout << "**************************New_File Menu:*************************\n\tFile Name : ";
						cin >> Staff.userInput;
						Func.newFile(Staff.userInput);
						fillForm();
						Func.writeToFile(Staff.userInput, Staff.id, Staff.name, Staff.sex, Staff.age, Staff.adres, Staff.phone, Staff.salary);
					}

					else if (Staff.userInput == "e") {
                        system("clear");
						cout << "**************************Edit_File Menu:*************************\n\tList Files";
						list directory Func.listDir();
						cout << "File Name : ";
						cin >> Staff.userInput;
						Func.editFile(Staff.userInput);
					}
					else if (Staff.userInput == "d") {
                           system("clear");
						cout << "**************************Delete_File Menu:*************************\n\tFile Name : ";
						cin >> Staff.userInput;
						cout << "File Deleted: " << Staff.userInput << endl;
						Func.deleteFile(Staff.userInput);
					}else if(Staff.userInput== "x"){
                        cout << "\nClosing!!!" << endl;
					}else {
						cout << "\nInvalid Input!!!" << endl;
					}
				} while (Staff.userInput!="x");
			}
			else if (Staff.userInput == "r") {
				do
				{
					cout << "**************************Read_Mode Menu:*************************\n\ta to List all Files\n\ts to Search\n\tx to Exit" << endl;
					cin >> Staff.userInput;

					if (Staff.userInput == "a") {
                        system("clear");
						cout << "**************************List_All_Files*************************\n";
						Func.listDir();
						cout << "File Name : ";
						cin >> Staff.userInput;
						Func.readFile(Staff.userInput);
					}
					else if (Staff.userInput == "s") {
                        system("clear");
						cout << "**************************Search_File Menu:*************************\n\tFile Name : ";
						cin >> Staff.userInput;
						cout << "\tStaff ID:";
						string tmp[10];
						cin >> tmp;
						Func.searchData(Staff.userInput, tmp);
					}
					}else if(Staff.userInput=="x"){
                        cout << "\nClosing!!!" << endl;
					}else {
						cout << "\nInvalid Input!!!" << endl;
					}
				} while (Staff.userInput!="x");
			}
			else if(Staff.userInput=="x"){
				cout << "\nClosing!!!" << endl;
			}else {
				cout << "\nInvalid Input!!!" << endl;
			}
		}while (Staff.userInput!="x");

		return 0;
	}
void fileForm(){
cout << "**************************Fill_Form:*************************\n";
cout << "STAFFID :";
cin >> Staff.id;
cout << "STAFFNAME :";
cin >> Staff.name;
cout << "SEX :"
cin >> Staff.sex;
cout << "AGE :"
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
class Func : public Sort
{
public:

void newFile(string filename)
{
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

   ofstream MyFile("%s.txt", filename);
    MyFile.close();
}

void editFile(string filename)
{
    ifstream infile(filename);
    if (!infile.is_open()) {
        cerr << "Could not open the file for reading!" << endl;
        return 1;
    }
    string content;
    string line;
    while (getline(infile, line)) {
        content += line + "\n";
    }
    infile.close();
    string oldText = "oldText";
    string newText = "newText";
    size_t pos = content.find(oldText);
    if (pos != string::npos) {
        content.replace(pos, oldText.length(), newText);
    }
    ofstream outfile(filename);
    if (!outfile.is_open()) {
        cerr << "Could not open the file for writing!" << endl;
        return 1;
    }
    outfile << content;
    outfile.close();
    cout << "File updated successfully." << endl;
}

void deleteFile(string filename)
{
    int status = remove("%s.txt",filename);
    if (status != 0) {
        perror("Error deleting file");
    }
    else {
        cout << "File successfully deleted" << endl;
    }
}

void readFile(string filename)
{
    ifstream inputFile("%s.txt", filename);
    if (!inputFile.is_open()) {
        cerr << "Error opening the file!" << endl;
        return 1;
    }
    string line;
    cout << "File Content: " << endl;
    while (getline(inputFile, line)) {
        cout << line << endl;
    }
    inputFile.close();
}

void searchData(string filename, string searchID)
{
    string line;
    bool found = false;
    cout << "Enter the ID to search: ";
    cin >> searchID;

    ifstream file(filename);
    if (!file.is_open()) {
        cerr << "Error opening file: " << filename << endl;
        return 1;
    }

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

void listDir()
{
    string path = "/Staff";
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

void writeToFile(string filename, string id, string name, string sex, int age, string address, int phone, float salary ){
     string line;
     int note=0;
    ofstream file;
    file.open(filename);
      while (getline(file, line)) {
      note+=1;
    }
    if (file.eof()) {
       file << "%d-%s-%s-%s-%d-%s-%d-%f", note, id, name, sex, age, address, phone, salary << endl;
    } else {
        cerr << "Error reading file!" << endl;
    }
    file.close();
    cout << "write to " << filename << " successfully." << endl;
}
};
//-----------------------------------------------------------

//----------------------sort_engine--------------------------
class Sort
{
public:

    vector<string> split(const string &str) {
    vector<string> result;
    string word = "";
    for (char ch : str) {
        if (ch == ' ') {
            result.push_back(word);
            word = "";
        } else {
            word += ch;
        }
    }
    result.push_back(word);
    return result;
}

// Function to read records from a file
vector<Staffdata> readFromFile(const string &filename) {
    vector<Staffdata> staffList;
    ifstream inputFile(filename);

    if (!inputFile) {
        cerr << "Could not open the file!" << endl;
        return staffList;
    }

    string line;
    while (getline(inputFile, line)) {
        vector<string> data = split(line);
        if (data.size() < 7) continue; // Ensure there's enough data in the line

        Staffdata staff;
        staff.id = data[0];
        staff.name = data[1];
        staff.sex = data[2];
        staff.age = stoi(data[3]);
        staff.address = data[4];
        staff.phone = stoi(data[5]);
        staff.salary = stof(data[6]);

        staffList.push_back(staff);
    }

    inputFile.close();
    return staffList;
}

// Function to write records to a file
void writeToFile(const string &filename, const vector<Staffdata> &staffList) {
    ofstream outputFile(filename);

    if (!outputFile) {
        cerr << "Could not open the file!" << endl;
        return;
    }

    for (const auto &staff : staffList) {
        outputFile << staff.toString() << endl;
    }

    outputFile.close();
}


void bubbleSort(vector<Staffdata> &staffList) {
    int n = staffList.size();
    for (int i = 0; i < n - 1; i++) {
        for (int j = 0; j < n - i - 1; j++) {
            if (staffList[j].id > staffList[j + 1].id) {
                swap(staffList[j], staffList[j + 1]);
            }
        }
    }
}

int main() {
    string filename = "staff_records.txt";


    vector<Staffdata> staffList = readFromFile(filename);


    cout << "Before sorting:\n";
    for (const auto &staff : staffList) {
        cout << staff.toString() << endl;
    }

    bubbleSort(staffList);
    cout << "\nAfter sorting:\n";
    for (const auto &staff : staffList) {
        cout << staff.toString() << endl;
    }
    writeToFile("sorted_" + filename, staffList);

};
//-----------------------------------------------------------

//-------------------------Main Block-------------------------
int main()
{
	Menu menu;
	menu.run();
	return 0;
}
//------------------------------------------------------------
