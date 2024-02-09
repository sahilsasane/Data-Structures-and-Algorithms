#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#define n 100
int stack[n],top=-1,item;
void push(int ele){
    if(top>=n-1)
        printf("Overflow");
    else{
        stack[++top]=ele;
    }
}
int pop(){
    if(top<0)
        printf("Underflow");
    else{
        item = stack[top];
        top=top-1;
        return item;
    }
}
void eval(char pfix[]){
    int i=0,a,b,val;
    char ch;
    for(i=0;pfix[i]!=')';i++){
        ch=pfix[i];
        if(isdigit(ch))
            push(ch-'0');
        else if(ch=='+'||ch=='-'||ch=='/'||ch=='*'){
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
    printf("Result: %d",pop());
}
void main(){
    char pfix[n];int i;
    printf("Exp: ");
    for(i=0;i<n-1;i++){
        scanf("%c",&pfix[i]);
        if (pfix[i]==')')
            break;
    }
    eval(pfix);
}