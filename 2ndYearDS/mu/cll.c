#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};
struct node *head;

void insert_end(){
    int item;
    struct node *ptr;
    ptr = (struct node *)malloc(sizeof(struct node));
    scanf("%d",&item);
    ptr -> data = item;
    if(head==NULL){
        ptr -> next = head;
        head = ptr;
    }
    else{
        ptr -> next =head;
        head = ptr;
    }
}

void delete_first(){
    struct node *ptr;
    if(head!=NULL){
        ptr = head;
        head = head ->next;
        free(ptr);
    }
    else{
        ptr = head;
        free(ptr);
        head = NULL;
    }
}

void count_even(){
    struct node *ptr;
    ptr = head;
    while(ptr != head){
        
    }
}

void display(){

}

void main(){
    int ch = 1;
    while(ch!=5){
        printf("\n1.insert at end 2.delete first 3.count even 4.display 5.exit\nEnter choice: ");
        scanf("%d",&ch);
        switch(ch){
            case 1:
                insert_end();
                break;
            case 2:
                delete_first();
                break;
            case 3:
                count_even();
                break;
            case 4:
                display();
                break;
            case 5:
                exit(0);
        }
    }
}