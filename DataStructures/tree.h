#ifndef __TREE_H__
#define __TREE_H__


typedef struct tree{
  int x;
  struct tree *right;
  struct tree *left;
} tree_node_t;

//static tree_node_t nodeCount;

tree_node_t * maketree(int );

void preorder(tree_node_t *);

void inorder(tree_node_t *);

void postorder(tree_node_t *);

tree_node_t * buildTree(int [],int n);

tree_node_t * delete_smallest(tree_node_t *);

#endif
