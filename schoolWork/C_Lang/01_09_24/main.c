#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define MAX_FOODS 100
#define MAX_NAME_LEN 50

typedef struct {
    char id[5];
    char name[MAX_NAME_LEN];
    char type[10];
    float unitPrice;
    int quantity;
    float totalPrice;
    int serialNumber;
} Food;

void writeMode();
void readMode();
void searchID(Food foodItems[], int count);
void readAll(Food foodItems[], int count);
void readFoods(Food foods[], int *count);
void bubbleSortById(Food foods[], int count);
void bubbleSortByName(Food foods[], int count);
void printFoods(Food foods[], int count);

int main() {
    char mode;

start:
    printf("********************************************************\n\n\t\t\tPick-Mode\n\n********************************************************\n\t\tr to Read || w to Write\n\tSelect mode : ");
    scanf(" %c", &mode);

    if (mode == 'w') {
        writeMode();
    } else if (mode == 'r') {
        readMode();
    } else {
        printf("\nInvalid input!!!");
        goto start;
    }
    return 0;
}

void writeMode() {
    system("clear");
    char switchMode;

    do {
        int idAmount;
        int totalQuantity = 0;
        float totalAmount = 0;

        printf("********************************************************\n\n\t\t\tWrite-Mode\n\n********************************************************\n");
        printf("\tAmount of Food to Enter : ");
        scanf("%d", &idAmount);

        Food foodItems[idAmount];

        FILE *food;
        food = fopen("food.txt", "a+");

        for (int i = 0; i < idAmount; i++) {
            printf("\nFood ID : ");
            scanf("%s", foodItems[i].id);
            printf("Food Name : ");
            scanf("%s", foodItems[i].name);
            printf("Food Type : ");
            scanf("%s", foodItems[i].type);
            printf("Unit Price : ");
            scanf("%f", &foodItems[i].unitPrice);
            printf("Quantity : ");
            scanf("%d", &foodItems[i].quantity);
            printf("Serial Number : ");
            scanf("%d", &foodItems[i].serialNumber);

            foodItems[i].totalPrice = foodItems[i].unitPrice * foodItems[i].quantity;
            totalAmount += foodItems[i].totalPrice;
            totalQuantity += foodItems[i].quantity;

            fprintf(food, "%s %s %s %.2f %d %.2f %d\n", foodItems[i].id, foodItems[i].name, foodItems[i].type, foodItems[i].unitPrice, foodItems[i].quantity, foodItems[i].totalPrice, foodItems[i].serialNumber);
        }

        fprintf(food, "\tTotal Quantity : %d\n\tTotal Amount : %.2f\n", totalQuantity, totalAmount);
        fclose(food);
        system("clear");

        printf("\n\tr to Read food || s to Stop\n\tOption : ");
        scanf(" %c", &switchMode);
        if (switchMode == 'r') {
            readMode();
            break;
        }
    } while (switchMode != 's');
}

void readMode() {
   system("clear");
    char mode;
    printf("********************************************************\n\n\t\t\tRead-Mode\n\n********************************************************\n");
    printf("\t\ti to Search ID || a to Print all  \n\tSearch : ");
    scanf(" %c", &mode);  // Space before %c to consume newline

    // Open the file and count the number of records
    FILE *food = fopen("food.txt", "r");
    if (food == NULL) {
        printf("Could not open file food.txt\n");
        return;
    }

    int count = 0;
    char line[256];
    while (fgets(line, sizeof(line), food)) {
        count++;
    }
    rewind(food); // Rewind the file pointer to the beginning

    // Allocate memory for foodItems array
    Food foodItems[count];
    int i = 0;
    while (fgets(line, sizeof(line), food) && i < count) {
        sscanf(line, "%*d %s %s %s %f %d", foodItems[i].id, foodItems[i].name, foodItems[i].type, &foodItems[i].unitPrice, &foodItems[i].quantity);
        i++;
    }
    fclose(food);

    if (mode == 'a') {
        readAll(foodItems, count);
    } else if (mode == 'i') {
        searchID(foodItems, count);
    } else {
        printf("\n\tinvalid input!!!\n");
        readMode();  // Recursive call instead of goto
    }
}

void searchID(Food foodItems[], int count) {
    system("clear");
    printf("********************************************************\n\n\t\t\tSearch_ID\n\n********************************************************\n");
    printf("\tPlease Input FoodID that you want to Know : ");
    char id_to_search[5];
    int found = 0;
    scanf(" %s", id_to_search);

    for (int i = 0; i < count; i++) {
        if (strcmp(foodItems[i].id, id_to_search) == 0) {
            printf("\n\tID %s found: \n\n*NO****FOODID****FOODNAME*******TYPE******UNITPRICE******QUANTITY*****AMOUNT\n", id_to_search);
            printf("%d     %s      %s          %s        %.2f             %d         %.2f\n", i, foodItems[i].id, foodItems[i].name, foodItems[i].type, foodItems[i].unitPrice, foodItems[i].quantity, foodItems[i].unitPrice * foodItems[i].quantity);
            found = 1;
            break;
        }
    }

    if (!found) {
        printf("ID %s not found in the records.\n", id_to_search);
    }

    char option;
start:
    printf("\na to List All || w to Write to file\n\tOption : ");
    scanf(" %c", &option);  // Space before %c to consume newline

    if (option == 'a') {
        readAll(foodItems, count);
    } else if (option == 'w') {
        writeMode();
    } else {
        printf("\n\tinvalid input!!!\n");
        goto start;
    }
}

void readAll(Food foodItems[], int count) {
    system("clear");
    printf("********************************************************\n\n\t\t\tLIST_OF_FOOD\n\n********************************************************\n");

    int choice;
    printf("Choose sorting option:\n1. Sort by ID\n2. Sort by Name\nEnter your choice: ");
    scanf("%d", &choice);
    system("clear");

    if (choice == 1) {
        bubbleSortById(foodItems, count);
        printf("Sorted by ID:\n");
    } else if (choice == 2) {
        bubbleSortByName(foodItems, count);
        printf("Sorted by Name (Alphabetically):\n");
    } else {
        printf("Invalid choice!\n");
        return;
    }

    printf("*ID****FOODNAME******TYPE****UNITPRICE******QUANTITY****AMOUNT****SERIAL\n");
    printFoods(foodItems, count);

    char option;
start:
    printf("\ni to Search ID || w to Write to file\n\tOption : ");
    scanf(" %c", &option);

    if (option == 'i') {
        searchID(foodItems, count);
    } else if (option == 'w') {
        writeMode();
    } else {
        printf("\n\tInvalid input!!!\n");
        goto start;
    }
}

void readFoods(Food foods[], int *count) {
    FILE *file = fopen("food.txt", "r");
    if (file == NULL) {
        perror("Error opening file");
        exit(1);
    }

    while (fscanf(file, "%s %s %s %f %d %f %d", foods[*count].id, foods[*count].name, foods[*count].type,
                  &foods[*count].unitPrice, &foods[*count].quantity, &foods[*count].totalPrice, &foods[*count].serialNumber) == 7) {
        (*count)++;
        if (*count >= MAX_FOODS) {
            break;
        }
    }
    fclose(file);
}

void bubbleSortById(Food foods[], int count) {
    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - i - 1; j++) {
            if (strcmp(foods[j].id, foods[j + 1].id) > 0) {
                Food temp = foods[j];
                foods[j] = foods[j + 1];
                foods[j + 1] = temp;
            }
        }
    }
}

void bubbleSortByName(Food foods[], int count) {
    for (int i = 0; i < count - 1; i++) {
        for (int j = 0; j < count - i - 1; j++) {
            if (strcmp(foods[j].name, foods[j + 1].name) > 0) {
                Food temp = foods[j];
                foods[j] = foods[j + 1];
                foods[j + 1] = temp;
            }
        }
    }
}

void printFoods(Food foods[], int count) {
    for (int i = 0; i < count; i++) {
        printf("%s    %s       %s       %.2f        %d         %.2f     %d\n", foods[i].id, foods[i].name, foods[i].type, foods[i].unitPrice, foods[i].quantity, foods[i].totalPrice, foods[i].serialNumber);
    }
}
