/* Non-homogeneous singly-linked list demonstration in C. */

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

struct Node {
	void* val;
	struct Node* next;
	void (*show)();
	void (*deallocate)();
};

struct Node* node_init(void* val, void (*show)(), void (*deallocate)()) {
	struct Node* new_node = malloc(sizeof(struct Node));
	new_node->val = val;
	new_node->show = show;
	new_node->deallocate = deallocate;
	new_node->next = 0;
	return new_node;
}

void list_deallocate(struct Node* list) {
	if (!list)
		return;
	list->deallocate(list->val);
	list_deallocate(list->next);
	free(list);
}

void append(struct Node* list, struct Node* new_node) {
	while (list->next) {
		list = list->next;
	} 
	list->next = new_node;	
}

void int_show(void* val) {
	int* int_val = (int*)val;
	printf("%d", *int_val);
}

void int_deallocate(void* val) {
	int* int_val = (int*)val;
	free(int_val);
}

void str_show(void* val) {
	char* str_val = (char*)val;
	printf("%s", str_val);
}

void str_deallocate(void* val) {
	free(val);
}

void list_show(struct Node* list) {
	printf("{");
	while (list) {
		list->show(list->val);
		list = list->next;
		if (list) {
			printf(" ");
		}
	}
	printf("}\n");
}

int main() {
	int* first_num = malloc(sizeof(int));
	char* second_string = malloc(sizeof(char) * 10);
	*first_num = 20;
	strncpy(second_string, "wagwan", 7);
	struct Node* list = node_init(first_num, int_show, int_deallocate);
	struct Node* second = node_init(second_string, str_show, str_deallocate);
	append(list, second);
	list_show(list);
	list_deallocate(list);	
	return 0;
}
