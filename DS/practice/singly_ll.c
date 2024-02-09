#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};
struct node *head=NULL;

void insert_front(){
    int item;
    struct node *ptr;
    ptr=(struct node *)malloc(sizeof(struct node));
    if(ptr==NULL)
        printf("Overflow");
    else{
        scanf("%d",&item);
        ptr->data=item;
        ptr->next=head;
        head=ptr;

    }
}
void print_list(){
    struct node *ptr;
    ptr=head;
    while(ptr!=NULL){
        printf("\n%d",ptr->data);
        ptr=ptr->next;
    }
}
void main(){
    int ch=1;
    while(ch!=3){
        printf("\n1.insert 2.print 3.exit");
        scanf("%d",&ch);
        if(ch==1)
            insert_front();
        else if(ch==2)
            print_list();
        else
            printf("appropriate");
    }
}