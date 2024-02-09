#include<stdio.h>
#include<stdlib.h>

#define n 10
int f=-1,r=-1;
int q[n];

void enqueue(int item){
    int item;
    if(f==0 && r==n-1)
        printf("Overflow");
    if(f==-1 && r==-1){
        f++;r++;
        q[r]=item;
    }
    else if(r!=n-1){
        q[++r]=item;
    }
    else if(f!=0 && r==n-1){
        r = (r+1)%n;
        q[r]=item;
    }
}
