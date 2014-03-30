#include<stdio.h>
#include<stdlib.h>

#include"tree.h"

/*
A bare bone version of binary tree without duplicates in C. 
*/

tree_node_t * maketree(int num){
	tree_node_t *head;
	head=malloc(sizeof(struct tree));
	//head->nodeCount++;
	head->x=num;
	head->right=NULL;
	head->left=NULL;
	return head;
}

void preorder(tree_node_t *head){
	if(head==NULL)
		return ;
	printf("%d\t",head->x);
	preorder(head->left);
	preorder(head->right);
}

void inorder(tree_node_t *head){
	if(head==NULL)
		return;
	inorder(head->left);
	printf("%d\t",head->x);
	inorder(head->right);
}

void postorder(tree_node_t *head){
	if(head==NULL)
		return;
	postorder(head->left);
	postorder(head->right);
	printf("%d\t",head->x);
}

tree_node_t * buildTree(int a[],int n){
  int idx;
  tree_node_t *p=NULL,*q=NULL;
  tree_node_t *root=NULL;
  
  if(root==NULL && n!=0)
    root=maketree(a[0]);

  p=q=root;
  
  for(idx=1;idx<n;idx++){
    
    p=q=root;
    while(a[idx]!= p->x && q!=NULL){
      p=q;
      if(a[idx] < p->x)
	q=p->left;
      else
	q=p->right;
    }
    if(p->x == a[idx])
      printf("Duplicate %d\n",a[idx]);
    else if(a[idx] < p->x)
      p->left=maketree(a[idx]);
    else
      p->right=maketree(a[idx]);
  }

  return root;
}

//The iterative way to delete the smallest node from a BST
tree_node_t * delete_smallest(tree_node_t *head){
  tree_node_t *temp,*root;
  temp=root=head;
  if(head->left==NULL){
    temp=head->right;
    free(head);
    return head->right;
  }

  while(head->left != NULL){
    temp=head;
    head=head->left;
  }

  printf("Smallest no is %d\n",head->x);
  free(head);
  temp->left=NULL;
  return root;
}


int main(){
	int a[]={14,15,4,9,7,18,3,5,16,4,20,17,9,14,5};
	tree_node_t *root=NULL;

	root=buildTree(a,sizeof(a)/sizeof(int));

	preorder(root);
	printf("\n");
	inorder(root);
	printf("\n");
	postorder(root);
	printf("\n");

	root=delete_smallest(root);
	inorder(root);
}

