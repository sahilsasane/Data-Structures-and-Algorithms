#include<stdio.h>
#include<stdlib.h>
 
int graph[10][10];int n;int visited[100];
struct queue
{
    int size;
    int f;
    int r;
    int* arr;
};


int isEmpty(struct queue *q){
    if(q->r==q->f){
        return 1;
    }
    return 0;
}
 
int isFull(struct queue *q){
    if(q->r==q->size-1){
        return 1;
    }
    return 0;
}
 
void enqueue(struct queue *q, int val){
    if(isFull(q)){
        printf("This Queue is full\n");
    }
    else{
        q->r++;
        q->arr[q->r] = val;
        // printf("Enqued element: %d\n", val);
    }
}
 
int dequeue(struct queue *q){
    int a = -1;
    if(isEmpty(q)){
        printf("This Queue is empty\n");
    }
    else{
        q->f++;
        a = q->arr[q->f]; 
    }
    return a;
}

void DFS(int a[][n],int k)
{
    int j;
    printf("%d ", k);
    visited[k]=1;

    for(j=0; j<n; j++) {
        //printf("%d ", j);
        if(graph[k][j]==1 && visited[j]==0) {
            //printf("%d ",j);
            DFS(a,j);
        }
    }
}


int main(){
   // int n,e,k;
    struct queue q;
    q.size=100;
    q.f=q.r=-1;
    q.arr=(int *)malloc(sizeof(q.size*sizeof(int)));
    int k;
    printf("Enter no. of nodes:\n");
    scanf("%d",&n);
    
    for(int i=0;i<n;i++){
        visited[i]=0;
    }
   
   // int graph[n][n];
    for(int i=0;i<n;i++){
        for(int j=0;j<n;j++){
            scanf("%d",&graph[i][j]);
        }
    }
    
    //int visited[n];
    for(int i=0;i<n;i++){
        visited[i]=0;
    }
    
    printf("Enter value of starting node from 0 to %d\n",n-1);
    scanf("%d",&k);
    //BFS implementation
    printf("%d ",k);
    visited[k]=1;
    enqueue(&q,k);
    while(!isEmpty(&q)){
        int x=dequeue(&q);
        for(int j=0;j<n;j++){
            if(graph[x][j]==1 && visited[j]==0){
                printf("%d ",j);
                visited[j]=1;
                enqueue(&q,j);
            }
        }
    }
    printf("\n");
    printf("DFS implementation: \n");
    for(int i=0;i<n;i++){
        visited[i]=0;
    }
    DFS(graph,k);
    return 0;
}