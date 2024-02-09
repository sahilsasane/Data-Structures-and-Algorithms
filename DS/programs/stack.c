#include<stdio.h>
#include<conio.h>
int n,ch,e,top=-1,i;
int stack[100];

void push(){
    if(top>=n-1)
        printf("Overflow.");
    else{
        printf("Enter Element: ");
        scanf("%d",&e);
        top++;
        stack[top]=e;
    }
}
void pop(){
    if(top==-1)
        printf("Underflow.");
    else{
        top--;
    }
}
void display(){
    if(top==-1)
        printf("Stack is empty.");
    else{
        for(i=top;i>=0;i--){
            printf("%d\n",stack[i]);
        }
    }

}
void main(){
    printf("Enter Size: ");
    scanf("%d",&n);
    printf("\n1.Push\t2.Pop\t3.Display\t4.Exit");
    do{
        printf("\nEnter choice: ");
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
                break;
        }
    }
    while(ch!=4);
}