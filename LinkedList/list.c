/* Non-homogeneous singly-linked list demonstration in C. */

#include <stdio.h>
#include <stdlib.h>

struct Node {
	void* val;
	struct Node* next;
	void (*show)();
};

struct Node* node_init(void* val, void (*show)()) {
	struct Node* new_node = malloc(sizeof(struct Node));
	new_node->val = val;
	new_node->show = show;
	return new_node;
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

void str_show(void* val) {
	char* str_val = (char*)val;
	printf("%s", str_val);
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
	second_string = "wagwan";
	struct Node* list = node_init(first_num, int_show);
	struct Node* second = node_init(second_string, str_show);
	append(list, second);
	list_show(list);
	
	return 0;
}
