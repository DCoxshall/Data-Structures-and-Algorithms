#include "LinkedList.hpp"

LinkedList::LinkedList() {
    size = 0;
    head = 0;
    tail = 0;
}

int LinkedList::peek() {
    return tail->data;
}

int LinkedList::pop() {
    int popData = tail->data;
    tail = tail->prev;
    delete tail->next;
    tail->next = nullptr;
    size--;
    return popData;
}

void LinkedList::push(int data) {
    if (size == 0) {
        Node newNode = Node(data);
        head = &newNode;
        tail = &newNode;
    } else if (size == 1) {
        Node newNode = Node(data);
        tail->next = &newNode;
        newNode.prev = tail;
        tail = &newNode;
        head->next = tail->prev;
    }
    {
        Node newNode = Node(data);
        tail->next = &newNode;
        newNode.prev = tail;
        tail = &newNode;
    }
    size++;
}

std::ostream &operator<<(std::ostream &os, const LinkedList &list) {
    os << "[";
    Node *currentNode = list.head;
    while (currentNode != nullptr) {
        os << currentNode->data;
        currentNode = currentNode->next;

        if (currentNode != nullptr) {
            os << ", ";
        }
    }
    os << "]";

    return os;
}