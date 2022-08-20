#include<iostream>
#include<stdlib.h>
using namespace std;

typedef struct Node
{
    int data;
    struct Node *next;
}node;

node *front,*rear;

void initail(){
    front = rear = 0;
}

void enqueue(int val){
    node *newNode;
    newNode = new node;
    newNode->data = val;
    newNode->next = 0;
    if(front == 0 && rear == 0){
        front = rear = newNode;
    }else{
        rear->next = newNode;
        rear = rear->next;
    }
}

void display(){
    node *temp = front;

    while (temp!= 0)
    {
        cout<<temp->data << " ";
        temp = temp->next;
    }
    
}

int dequeue(){
    int data = front->data;
    node *temp = front;

    front = front->next;
    free(temp);

    return data;
}

int main(){
   initail();
   enqueue(10);
   enqueue(20);
   enqueue(30);
   display();
   cout<<"\n Front Data "<<dequeue()<<endl;
   display();

    return 0;
}