#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct node{
    int data;
    struct node *next;
    struct node *prev;

};
struct node *head;
void in_begin();
void in_end();
void del_begin();
void del_end();
void display();

void main(){
    int ch=0;
    while(ch!=6){
        printf("\n1.in_begin 2.in_end 3.del_begin 4.del_end 5.display 6.Exit");
        printf("\nEnter choice: ");
        scanf("%d",&ch);
        switch(ch){
            case 1:
                in_begin();
                break;
            case 2:
                in_end();
                break;
            case 3:
                del_begin();
                break;
            case 4:
                del_end();
                break;
            case 5:
                display();
                break;
            case 6:
                exit(0);
                break;
        }

    }
}

void in_begin(){
    struct node *ptr;
    int item;
    ptr=(struct node *)malloc(sizeof(struct node));
    if(ptr==NULL)
        printf("\nOverflow");
    else{
        printf("\nEnter value: ");
        scanf("%d",&item);
        if(head==NULL){
            ptr->next = NULL;
            ptr->prev = NULL;
            ptr->data = item;
            head = ptr; 
        }
        else{
            ptr->data = item;
            ptr->prev = NULL;
            ptr->next = head;
            head->prev = NULL;
            head = ptr;
        }
        printf("Node inserted");
    }
}

void in_end(){
    struct node *ptr,*temp;
    int item;
    ptr=(struct node *)malloc(sizeof(struct node));
    if(ptr==NULL)
        printf("\nOverflow");
    else{
        printf("\nEnter value: ");
        scanf("%d",&item);
        if(head==NULL){
            ptr->data = item;
            ptr->next = NULL;
            ptr->prev = NULL;
            head = ptr;
        }
        else{
            temp = head;
            while(temp->next !=NULL)
                temp = temp ->next;
            temp->next = ptr;
            ptr->prev = temp;
            ptr->data = item;
            ptr->next = NULL;
        }
        printf("Node inserted");
    }
}

void del_begin(){
    struct node *ptr;
    if(head==NULL)
        printf("\nUnderflow");
    else if(head->next == NULL){
        head = NULL;
        free(head);
        printf("\nNode deleted");
    }    
    else{
        ptr=head;
        head = head->next;
        head->prev = NULL;
        free(ptr);
        printf("Node deleted");
    }
}

void del_end(){
    struct node *ptr;
    if(head==NULL)
        printf("\nUnderflow");
    else if(head->next == NULL){
        head = NULL;
        free(head);
        printf("Node deleted");
    }
    else{
        ptr = head;
        if(ptr!=NULL)
            ptr = ptr->next;
        ptr->prev->next = NULL;
        free(ptr);
        printf("\nNode deleted");
    }
}

void display(){
    struct node *ptr;
    ptr = head;
    while(ptr !=NULL){
        printf("%d ",ptr->data);
        ptr = ptr->next;
    }
}



