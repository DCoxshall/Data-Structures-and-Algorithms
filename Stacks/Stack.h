#ifndef _STACK_H_
#define _STACK_H_

#include <stdio.h>
#include <stdlib.h>

typedef struct Node {
    int data;
    struct Node* next;
} Node;

typedef struct Stack {
    Node* top;
    int size;
} Stack;

Stack* stack_init() {
    Stack* new_stack = (Stack*)malloc(sizeof(Stack));
    new_stack->size = 0;
    new_stack->top = NULL;
    return new_stack;
}

void stack_push(Stack* stack, int data) {
    Node* new_node = (Node*)malloc(sizeof(Node));
    new_node->data = data;
    if (stack->size == 0) {
        new_node->next = NULL;
    } else {
        new_node->next = stack->top;
    }
    stack->top = new_node;
    stack->size++;
}

int stack_pop(Stack* stack) {
    if (stack->size == 0) {
        printf("Stack is empty");
        return -1;
    } else {
        int return_data = stack->top->data;
        Node* temp = stack->top;
        stack->top = stack->top->next;
        free(temp);
        stack->size--;
        return return_data;
    }
}

void stack_show(Stack* stack) {
    printf("[");
    Node* current_node = stack->top;
    while (current_node != NULL) {
        printf("%d", current_node->data);
        current_node = current_node->next;
        if (current_node != NULL) {
            printf(", ");
        }
    }
    printf("]");
}

void stack_delete(Stack* stack) { free(stack); }

#endif