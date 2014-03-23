#include<iostream>
#include<new>

using namespace std;

class Node{
private:
  int data;
public:
  class Node *left,*right;
public:
  Node(){
    data=0;
    left=0;
    right=0;
  }
  Node(int x){
    data=x;
    left=0;
    right=0;
  }
    int accessData(){
      return data;
    }
    void setData(class Node *Nodeptr,int x){
      Nodeptr->data=x;
      Nodeptr->right=0;
      Nodeptr->left=0;
    }
  Node * getLeftTree(){
    return left;
  }
  Node * getRightTree(){
    return right;
  }
  void makeLeftTree(int x){
    Node *nodePtr=new Node(x);
    left=nodePtr;
  }
  void makeRightTree(int x){
    Node *nodePtr=new Node(x);
    right=nodePtr;
  }
};

Node * maketree(class Node *root,int x){
  Node *temp;//=new Node(x);
  Node *p,*q;
  if(root==0){
    temp=new Node (x);
    return temp;
  }
  //return temp;
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

void displayTreeInorder(Node *root){
  if(root==0)
    return;
  displayTreeInorder(root->left);
  cout<<root->accessData()<<"\t";
  displayTreeInorder(root->right);
}

int main(){
  int a[]={14,15,4,9,7,18,3,5,16,4,20,17,9,14,5};
  int i=0;
  int length=sizeof(a)/sizeof(a[0]);
  Node *root=0;

  for(i=0;i<length;i++)
    root=maketree(root,a[i]);

  displayTreeInorder(root);
  return 0;
}
