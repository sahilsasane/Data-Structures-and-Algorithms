#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>

char stack[100],x;
int top=-1;

void push(int e){
        stack[++top] = e;
}

char pop(){
    if(top==-1)
        return (printf("Underflow"));
    else
        return  stack[top--];
}

int priority(char x){
    if(x=='(')
        return 0;
    if(x=='/' || x=='*')
        return 2;
    if(x=='+' || x=='-')
        return 1;
    else    
        return 0;
}

void main(){
    char exp[100];
    char *e;
    printf("Enter expression: ");
    scanf("%s",&exp);
    e=exp;
    while(*e!='\0'){
        if(isalnum(*e))
            printf("%c",*e);
        else if(*e == '(')
            push(*e);
        else if(*e==')'){
                while((x = pop())!='(')
                    printf("%c",x);
        }
        else{
            while(priority(stack[top])>=priority(*e))
                printf("%c",pop());
            push(*e);
        }
        e++; 
    }
    while(top!=-1)
        printf("%c",pop());


}