#include <stdio.h>
#include <stdlib.h>
void writeMode();
// void readMode();

void main()
{
  char mode;

start: // loop if mode is invalid
  printf("\t***********Mode**********\n\tSelect mode:");
  scanf("%c", &mode);
  // mode pick
  if (mode == "W")
  { // mode write
    writeMode();
  }
  else if (mode == "R")
  { // mode read
    readMode();
  }
  else
  {
    printf("invalid input!!!");
    goto start;
  }
} // end main

void writeMode()
{ // writeMode use to write to file.
  char name[10], type[10];
  int id =1, quatity=1, idAmount;
  float uPrice=1;
 printf("\n\tWrite MOD"); // welcome txt
printf("Amount of Food to Enter :"); // welcome txt
scanf("%d",&idAmount);
for(int i = 0 ; i < idAmount ; i++)
{
printf("Food ID :");
scanf("%d", &id);
 printf("Food Name :");
 scanf("%s",&name);
 printf("Food Type :");
 scanf("%s",&type);
 printf("Unite Price :");
 scanf("%f",&uPrice);
 printf("Quatity :");
 scanf("%d",&quatity);
 printf("Amount :");
 FILE* food;
    food = fopen("food.txt", "w+");
    fprintf(food, "%d %s %s %f %d %f", id, name, type, uPrice, quatity , uPrice*quatity);
    fclose(food);
 }
}



// void readMode()
// { // read mode use to read from file.
//   char mode[5];
//   printf("\tRead MOD");
//       printf("\tID or al  \nsearch :");
//   scanf("%c", &mode);
//   if (mode)
//   { // detect weather it string or int and choose MOD
//   }
//   else if(mode)
//     {
//     }
//   else
//   {

//   }
// }