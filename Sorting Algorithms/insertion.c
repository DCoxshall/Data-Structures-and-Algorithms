#include <stdio.h>

void insertion_sort(int* arr, int n) {
    int sorted = 0;
    while (sorted < n) {
        int j = sorted;
        while (arr[j] < arr[j - 1] && j > 0) {
            int temp = arr[j];
            arr[j] = arr[j - 1];
            arr[j - 1] = temp;
            j--;
        }
        sorted++;
    }
}

int main() {
    int test[] = {5, 4, 3, 2, 1};
    insertion_sort(test, 5);
    for (int i = 0; i < 5; i++) {
        printf("%d ", test[i]);
    }
} 

