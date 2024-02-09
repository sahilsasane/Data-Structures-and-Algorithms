#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<ctype.h>

int n,ch,top=-1,i;
char stack[100];

void push(int ea){
    stack[++top]=ea;
    
}
char pop(){
    return stack[top--];
}
int priority(char x){
    if(x=='(')
        return 0;
    else if(x=='+'||x=='-')
        return 1;
    else if(x=='*'||x=='/')
        return 2;
    else
        return 0;
}
void main(){
    char exp[100];
    char *e,x;
    printf("Enter expression: ");
    scanf("%s",&exp);
    e=exp;
    while(*e!='\0'){
        if(isalnum(*e))
            printf("%c",*e);
        else if(*e=='(')
            push(*e);
        else if(*e==')'){
            while((x=pop())!='(')
                printf("%c",x);
        }
        else{
            while(priority(stack[top])>=priority(*e))
                printf("%c",pop());
            push(*e);
        }
        e++;
    }
    while(top!=-1){
        printf("%c",pop());
    }
}