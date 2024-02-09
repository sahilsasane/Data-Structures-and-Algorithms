#include<stdio.h>
#include<stdlib.h>
struct node{
    int vertex;
    struct node *next;
};
struct node* createnode(int v);
struct Graph{
    int numvertices;
    int* visited;
    struct node** adjuncy_list;
};
void DFS(struct Graph* graph,int vertex){
    
}