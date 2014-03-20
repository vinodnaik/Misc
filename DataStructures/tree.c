#include<stdio.h>
#include<stdlib.h>

typedef struct tree{
	int x;
	struct tree *right;
	struct tree *left;
}node;

node * maketree(int num){
	node *head;
	head=malloc(sizeof(struct tree));
	head->x=num;
	head->right=NULL;
	head->left=NULL;
	return head;
}

void preorder(node *head){
	if(head==NULL)
		return ;
	printf("%d\t",head->x);
	preorder(head->left);
	preorder(head->right);
}

void inorder(node *head){
	if(head==NULL)
		return;
	inorder(head->left);
	printf("%d\t",head->x);
	inorder(head->right);
}

void postorder(node *head){
	if(head==NULL)
		return;
	postorder(head->left);
	postorder(head->right);
	printf("%d\t",head->x);
}

int main(){
	int a[]={14,15,4,9,7,18,3,5,16,4,20,17,9,14,5};
	int n,i,num=5;
	node *p=NULL,*q=NULL;
	node *root=NULL;	//maketree(a[0]);
	n=sizeof(a)/sizeof(int);
	p=q=root;
	for(i=0;i<n;i++){
		//num=a[i];
		p=q=root;
		while(p!=NULL){
			if(a[i] == p->x){
				printf("Duplicate %d\n",a[i]);
				break;
			}
			q=p;
			if(a[i] < p->x)
				p=p->left;
			else
				p=p->right;
		}
		if(q==NULL)
			root=maketree(a[i]);
		else 
			if(a[i] < q->x)
				q->left=maketree(a[i]);
			else if(a[i] > q->x)
				q->right=maketree(a[i]);
	}
	preorder(root);
	printf("\n");
	inorder(root);
	printf("\n");
	postorder(root);
	printf("\n");
}

