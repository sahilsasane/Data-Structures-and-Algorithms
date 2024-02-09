#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>

#define n 100
int stack[n],top=-1,item=0;

void push(int ele){
    if(top>=n-1)
        printf("Overflow");
    else{
        top++;
        stack[top]=ele;
    }
}

int pop(){
    if(top<=0)
        printf("Underflow");
    else{
        item=stack[top];
        top--;
        return item;
    }
}

void evalpostfix(char pfix[]){
    int i=0,a,b,val;
    char ch;
    for(i=0;pfix[i]!=')';i++){
        ch=pfix[i];
        if(isdigit(ch)){
            push(ch-'0');
        }
        else if(ch=='+' || ch=='-' || ch=='/' || ch=='*'){
            a=pop();
            b=pop();
            switch(ch){
                case '+':
                    val=b+a;
                    break;
                case '-':
                    val=b-a;
                    break;
                case '/':
                    val=b/a;
                    break;
                case '*':
                    val=b*a;
                    break;
            }
            push(val);
        }
    }
    printf("\nResult= %d",pop());
}


void main(){
    int i;
    char pfix[n];
    printf("Enter expression: ");
    for(i=0;i<n-1;i++){
        scanf("%c",&pfix[i]);
        if(pfix[i]==')')
            break;
    }
    evalpostfix(pfix);
}   