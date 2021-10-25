#include "Node.hpp"
#include <string>
#include <iostream>

class LinkedList
{
public:
    int size;
    Node *head;
    Node *tail;

    LinkedList();
    void push(int data);
    int pop();
    int peek();
    void show();

    friend std::ostream &operator<<(std::ostream &os, const LinkedList &list);
};
