#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *next;
};
struct node *front;
struct node *rear;

void enqueue(){
    int item;
    struct node *ptr;
    ptr = (struct node *)malloc(sizeof(struct node));
    scanf("%d",&item);
    ptr->data = item;
    ptr->next = NULL;
    if((front ==NULL) && (rear ==NULL)){
        front=rear=ptr;
        rear->next = front;
    }
    else{
        rear ->next =ptr;
        rear = ptr;
        ptr ->next = front;
    }
}
void dequeue(){
    struct node *ptr;
    ptr = front;
    if(front==NULL && rear == NULL)
        printf("Underflow");
    else if(front==rear){
        front=rear= NULL;
        free(ptr);
    }
    else{
        front=front->next;
        rear ->next = front;    
        free(ptr);
        
    }
}
void display(){
    struct node *ptr;
    ptr=front;
    do{
        printf("%d ",ptr->data);
        ptr = ptr->next;
    }
    while(ptr!=front);
    
}
void main(){
    int ch=1;
    while(ch!=4){
        printf("\n1.insert 2.delete 3.print 4.exit");
        scanf("%d",&ch);
        if(ch==1)
            enqueue();
        else if(ch==2)
            dequeue();
        else if(ch==3)
            display();
        else
            printf("appropriate");
    }
}