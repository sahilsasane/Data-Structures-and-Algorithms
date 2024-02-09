#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

int queue[20];
int n,ch,e,front=-1,rear=-1,i;

void enqueue(){
    if(front==-1 && rear==-1){
        front++;
        rear++;
        printf("Enter element: ");
        scanf("%d",&e);
        queue[rear]=e;
    }
    else if(rear!=n-1){
        printf("Enter element: ");
        scanf("%d",&e);
        queue[++rear]=e;
    }
    else{
        printf("Overflow.");
    }
}
void dequeue(){
    if(front!=n-1)
        front++;
    else
        printf("Underflow.");
}
void display(){
    if(front!=n-1){
        for(i=front;i<=rear;i++)
            printf("\n%d",queue[i]);
    }
    else
        printf("Queue is empty.");
}

void main(){
    printf("Enter size: ");
    scanf("%d",&n);
    printf("\n1.enqueue 2.dequeue 3.display 4.exit");
    do{
        printf("\nEnter choice: ");
        scanf("%d",&ch);
        switch(ch){
            case 1:
                enqueue();
                break;
            case 2:
                dequeue();
                break;
            case 3:
                display();
                break;
        }
    }
    while(ch!=4);
}