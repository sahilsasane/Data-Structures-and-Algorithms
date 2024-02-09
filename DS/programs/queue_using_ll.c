#include<stdio.h>
#include<stdlib.h>
struct node{
	int data;
	struct node* next;
};
struct node *f = NULL;
struct node *r = NULL;
void enqueue(int d){
	struct node* n;
	n = (struct node*)malloc(sizeof(struct node));
	n->data = d;
	n->next = NULL;
	if((r==NULL)&&(f==NULL)){
		f = r = n;
		r->next = f;
	}
	else{
		r->next = n;
		r = n;
		n->next = f;
	}
} 
void dequeue(){
	struct node* t;
	t = f;
	if((f==NULL)&&(r==NULL))
		printf("\nQueue is Empty");
	else if(f == r){
		f = r = NULL;
		free(t);
	}
	else{
		f = f->next;
		r->next = f;
		free(t);
	}
	
	
}
void display(){ 
	struct node* t;
	t = f;
	if((f==NULL)&&(r==NULL))
		printf("\nQueue is Empty");
	else{
		do{
			printf("\n%d",t->data);
			t = t->next;
		}while(t != f);
	}
}
void main(){
	int opt,n,i,data;
	printf("Enter Your Choice:-");
	do{
		printf("\n1.Enqueue  2.Dequeue  3.Display  4.Exit\n");
		scanf("%d",&opt);
		switch(opt){
			case 1:
				printf("\nEnter your data");
					scanf("%d",&data);
					enqueue(data);
				break;
			case 2:
				dequeue();
				break;
			case 3:
                 display();
				break;
			case 4:
				break;
			default:
				printf("\nIncorrect Choice");
			
		}
	}while(opt!=4);
}