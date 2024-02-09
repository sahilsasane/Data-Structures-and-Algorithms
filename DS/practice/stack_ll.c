#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};

struct node *top;
struct node *start;
void push(){
    int n;
    printf("Enter data: ");
    scanf("%d",&n);
    struct node *ptr;
    ptr = (struct node *)malloc(sizeof(struct node));
    if(top==NULL){
        ptr->data = n;
        ptr->next = NULL;
        top = ptr;
        start = ptr;
    }
    else{
        ptr->data = n;
        ptr->next = NULL;
        top->next = ptr;
        top = ptr;
    }
}

void pop(){
    if(top == NULL)
        printf("Underflow");
    else{
        free(top);
        
    }
}

void display(){
    struct node *ptr;
    ptr = start;
    while(ptr!=NULL){
        printf("%d ",ptr->data);
        ptr = ptr->next;
    }
    printf("\nTop: %d",top->data);
}

void main(){
    int ch = 1;
    while(ch!=4){
        printf("\n1.Push 2.Pop 3.Display 4.Exit\nEnter choice: ");
        scanf("%d",&ch);
        switch(ch){
            case 1:
                push();
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
        }
    }
}