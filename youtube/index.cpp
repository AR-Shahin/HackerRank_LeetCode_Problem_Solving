#include<iostream>
using namespace std;

typedef struct Node{
    int data;
    struct Node *next;
    struct Node *prev;
}node;
int count = 0;
node *head,*tail;

void initial(){
    head = NULL;
}

void insertFirst(int val){
    node *newNode;
    newNode = new node;
    newNode->data = val;
    newNode->next = NULL;
    newNode->prev = NULL;

    if (head == NULL)
    {
        head = tail = newNode;
    }else{
        tail->next = newNode;
        newNode->prev = tail;
        tail = newNode;
    }
    count ++;
}
void insertLast(int val){
    if(head == NULL){
        insertFirst(val);
    }else{
        node *newNode;
        newNode = new node;

        newNode->data = val;
        head->prev = newNode;
        newNode->next = head;
        head = newNode;
    count ++;
    }
}

int lengthOfList(){
    return count;
}
void display(){
    node *temp;
    temp = head;

    while (temp != NULL)
    {
        cout<<temp->data << " ";
        temp = temp->next;
    }
    
}
void display_reverse(){
    node *temp;
    temp = tail;

    while (temp != NULL)
    {
        cout<<temp->data << " ";
        temp = temp->prev;
    }
    
}

void deleteFirst(){
    node *temp;
    temp = head;
    head = head->next;
    free(temp);
    head->prev = NULL;
    count --;
}
void deleteLast(){
    if(head == NULL){
        deleteFirst();
    }else{
        node *temp;
        temp = tail;
        tail = tail->prev;
        tail->next = NULL;
        free(temp);
        count --;
    }
}

void insertAtPostion(int pos,int val){
    if(pos > lengthOfList() || pos <= 0){
        cout<<"\nInvalid Position\n";
    }
    if(pos == 1){
        insertLast(val);
    }
    if(pos == lengthOfList()){
        insertFirst(val);
    }

    int index = 1;
    node *temp = head;
    while (index < pos -1)
    {
        temp = temp->next;
        index ++;
    }

    node *newNode;
    newNode = new node;
    newNode->data = val;

    newNode->prev = temp;
    newNode->next = temp->next;
    temp->next = newNode;
    newNode->next->prev = newNode;

    count ++; 
}

void deleteAtPostion(int pos){
    
    if(pos == 1){
        deleteFirst();
    }
    if(pos == lengthOfList()){
        deleteFirst();
    }

    int index = 1;
    node *temp = head;
    while (index < pos)
    {
        temp = temp->next;
        index ++;
    }

    temp->prev->next = temp->next;
    temp->next->prev = temp->prev;
    free(temp);
    count --;
}
int main(){
    initial();
    insertFirst(10);
    insertFirst(20);
    insertFirst(30);
    insertFirst(40);
    display();
    deleteAtPostion(3);
    cout<<endl;
    display();


    return 0;
}