#ifndef __TREE_H__
#define __TREE_H__


typedef struct tree{
	int x;
	struct tree *right;
	struct tree *left;
} tree_node_t;

tree_node_t * maketree(int num);

void preorder(tree_node_t *head);

void inorder(tree_node_t *head);

void postorder(tree_node_t *head);

#endif
