#include<iostream>
#include<new>

/*
A Binary search tree implementation in C++. Although not an efficient one. There 
is significant overhead in traversing as the left and right pointers are made private 
just to be in sync with the object oriented philosophy where data is private and methods 
act on it. The stack grows when each node is traversed as the no of function calls 
increase. The good design is making the left and right pointers public as they will be 
heavily used. Or we can use a friend function but it gives access to private data.
*/

using namespace std;

class Node{
private:
  int data;
  static int nodeCount;
  //public:
  class Node *left,*right;
public:
  Node(){
    data=0;
    left=0;
    right=0;
  }
  Node(int x){
    nodeCount++;
    data=x;
    left=0;
    right=0;
  }
  int accessData();
  int returnNodeCount();
  void setData(class Node *Nodeptr,int x);
  Node * getLeftTree();
  Node * getRightTree();
  void makeLeftTree(int x);
  void makeRightTree(int x);
  void displayTree();
};

int Node::nodeCount;

int Node::accessData(){
  return data;
}

int Node::returnNodeCount(){
  return nodeCount;
}

void Node::setData(class Node *Nodeptr,int x){
  Nodeptr->data=x;
  Nodeptr->right=0;
  Nodeptr->left=0;
}
  
Node * Node::getLeftTree(){
  return left;
}

Node * Node::getRightTree(){
  return right;
}

void Node::makeLeftTree(int x){
  Node *nodePtr=new Node(x);
  left=nodePtr;
}

void Node:: makeRightTree(int x){
  Node *nodePtr=new Node(x);
  right=nodePtr;
}

void Node::displayTree(){
  if(this!=NULL){
    this->getLeftTree()->displayTree();
    cout<<this->accessData()<<"\t";
    this->getRightTree()->displayTree();
  }
}
    

Node * maketree(class Node *root,int x){
  Node *temp;
  Node *p,*q;
  if(root==0){
    temp=new Node (x);
    return temp;
  }
  
  p=q=root;
  while(x != p->accessData() && q!=0){
    p=q;
    if(x < p->accessData())
      q=p->getLeftTree();
    else
      q=p->getRightTree();
  }
  if(p->accessData()==x)
    cout<<"Duplicate"<<x<<endl;
  else if(x < p->accessData())
    p->makeLeftTree(x);
  else
    p->makeRightTree(x);
 
  return root;
}

// void displayTreeInorder(Node *root){
//   if(root==0)
//     return;
//   displayTreeInorder(root->left);
//   cout<<root->accessData()<<"\t";
//   displayTreeInorder(root->right);
// }

int main(){
  int a[]={14,15,4,9,7,18,3,5,16,4,20,17,9,14,5};
  int idx=0;
  int length=sizeof(a)/sizeof(a[0]);
  Node *root=0;

  for(idx=0;idx<length;idx++)
    root=maketree(root,a[idx]);

  root->displayTree();

  cout<<endl<<"No of nodes ="<<root->returnNodeCount()<<endl;
  return 0;
}
