#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#define n 5
int front=-1,rear=-1,ele;
int queue[n];

int isempty(){
    return (front==-1 && rear==-1);
}
int isfull(){
    return (front==0 && rear==n-1);
}

void enqueue(){
    if(isempty()){
        front++;rear++;
        printf("\nEnter element ");
        scanf("%d",&ele);
        queue[rear]=ele;
    }
    else if(rear!=n-1){
        rear++;
        printf("\nEnter element ");
        scanf("%d",&ele);
        queue[rear]=ele;
    }
    else if(!(isfull())){
        rear=(rear+1)%n;
        printf("\nEnter element ");
        scanf("%d",&ele);
        queue[rear]=ele;
    }
    else    
        printf("Overflow!!");
}

void dequeue(){
    if (isempty()){
        printf("Underflow!!");
    }
    else{
        ele=queue[front];
        if(front==rear){
            front=-1;
            rear=-1;
        }
        else
            front=(front+1)%n;
        printf("deleted element is: %d",ele);
        
    } 
    
}
void display(){
    if(isempty())
        printf("Queue is empty");
    else{
        for(int i=front;i<=rear;i++){
            printf("\n%d",queue[i]);
        }
    }
        
}


void main(){
    int ch;
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
            case 4:
                exit(0);
            default:
                printf("Enter appropriate choice!");
                break;
        }
    }
    while(ch!=4);
}