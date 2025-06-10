#include<stdio.h>
#include<stdlib.h>
struct node 
  {
    int data;
    struct node * next;
  };

struct node * node1,*node2,*node3,*node4;
int main()
 {
    //Create Node 1
node1=(struct node*)malloc(sizeof(struct node));
    node1->data=1;
    node1->next=node2;
 node2=(struct node*)malloc(sizeof(struct node));
    node2->data=2;
    node2->next=node3;
 node3=(struct node*)malloc(sizeof(struct node));
    node3->data=3;
    node3->next=node4;
node4=(struct node*)malloc(sizeof(struct node));
    node4->data=4;
    node4->next=NULL;
    return 0;
 }
