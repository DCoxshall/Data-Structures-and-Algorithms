#include <stdio.h>


void bubblesort(int* arr, int n);

void bubblesort(int* arr, int n) {
    int sorted = 0;
    while (sorted == 0) {
        sorted = 1;
        for (int i = 0; i < n - 1; i++) {
            if (arr[i] > arr[i + 1]) {
                int temp = arr[i];
                arr[i] = arr[i + 1];
                arr[i + 1] = temp;
                sorted = 0;        
            }
        }
    }
}

int main() {
    int a[] = {5, 4, 3, 2, 1};
    bubblesort(a, 5);
    for (int i = 0; i < 5; i++) {
        printf("%d ", a[i]);
    }
} 
    
