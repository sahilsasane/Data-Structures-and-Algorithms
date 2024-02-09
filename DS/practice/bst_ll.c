#include<stdio.h>
#include<stdlib.h>

struct node{
    int data;
    struct node *left,*right;
};
struct node *newnode(int item){
    struct node *ptr;
    ptr = (struct node*)malloc(sizeof(struct node));
    ptr->data = item;
    ptr->right = ptr->left =NULL;
    return ptr;
}

void inorder(struct node *root){
    if(root!=NULL){
        inorder(root->left);
        printf("%d -> ",root->data);
        inorder(root->right);
    }
}
struct node *insert(struct node *node,int item){
    if(node==NULL)
        return newnode(item);
    if(item<node->data)
        node->left = insert(node->left,item);
    else
        node->right = insert(node->right,item);
    return node;
}
struct node *minvaluenode(struct node *node){
    struct node *current = node;
    while(current &&current->left!=NULL)
        current = current ->left;
    return current;
}
struct node *deletenode(struct node *root, int item){
    if(root==NULL)
        return root;
    if(item<root->data)
        root->left = deletenode(root->left,item);
    else if (item>root->data)
        root->right = deletenode(root->right,item);
    else{
        if(root->left ==NULL){
            struct node *temp = root->right;
            free(root);
            return temp;
        }
        else if(root->right ==NULL){
            struct node *temp = root->left;
            free (root);
            return temp;
        }
        struct node *temp = minvaluenode(root->right);
        root->data = temp->data;
        root->right = deletenode(root->right,temp->data);
    }
    return root;
}

void main(){
    struct node *root =NULL;
    root = insert(root,8);
    root = insert(root, 3);
    root = insert(root, 1);
    root = insert(root, 6);
    root = insert(root, 7);
    root = insert(root, 10);
    root = insert(root, 14);
    root = insert(root, 4);
    printf("Inorder traversal: ");
    inorder(root);

    printf("\nAfter deleting 10\n");
    root = deletenode(root, 7);
    printf("Inorder traversal: ");
    inorder(root);
}
