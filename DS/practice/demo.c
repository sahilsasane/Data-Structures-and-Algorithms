#include<stdio.h>
#include<conio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *left,*right;
};

struct node *newnode(int item){
    struct node *ptr = (struct node *)malloc(sizeof(struct node));
    ptr->data = item;
    ptr->left = NULL;
    ptr->right = NULL;
};

void inorder(struct node *root){
    if(root!=NULL){
        inorder(root->left);
        printf("%d ->",root->data);
        inorder(root->right);
    }
}

struct node *insert(struct node *node,int item){
    if(node==NULL)
        return newnode(item);
    else if(item<node->data)
        node->left = insert(node->left,item);
    else
        node->right = insert(node->right,item);
    return node;
}

struct node *minvalue(struct node *node){
    struct node *current = node;
    while(current && current->left != NULL)
        current = current->left;
    return current;
}

struct node *delete(struct node *node, int item){
    if(node==NULL)
        return node;
    else if(item<node->data)
        node-> left = delete(node->left , item);
    else if(item>node->data)
        node-> right = delete(node->right , item);
    else{
        if(node->left == NULL){
            struct node *temp = node->right;
            free(node);
            return temp;
        }
        else if(node->right == NULL){
            struct node *temp = node->left;
            free(node);
            return temp;
        }
        struct node *temp = minvalue(node->right);
        node->data = temp->data;
        node->right = delete(node->right,temp->data);
    }
    return node;
}
void main(){
    struct node *root = NULL;
    root = insert(root,3);
    root = insert(root,2);
    root = insert(root,7);
    root = insert(root,9);
    root = insert(root,1);
    root = insert(root,4);
    root = insert(root,6);
    root = insert(root,8);
    root = insert(root,5);
    inorder(root);
    root = delete(root,7);
    printf("\nAfter deleting node 7\n");
    inorder(root);
}

