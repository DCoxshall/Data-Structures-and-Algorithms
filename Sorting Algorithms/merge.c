#include <stdio.h>
#include <stdlib.h>
#include <time.h>

void mergesort(int* arr, int n);
void mergesort_run(int* arr, int left, int right);
void merge(int* arr, int left, int mid, int right);

void mergesort(int* arr, int n) {
	mergesort_run(arr, 0, n - 1);
}

void mergesort_run(int* arr, int left, int right) {
	if (left < right) {
		int mid = (left + right) / 2;
		mergesort_run(arr, left, mid);
		mergesort_run(arr, mid + 1, right);
		merge(arr, left, mid, right);
	}
}

void merge(int* arr, int left, int mid, int right) {
	int* arr_b = malloc(sizeof(int) * (right - left + 1));
	int bcount = 0;
	int lcount = left;
	int rcount = mid + 1;
	while (lcount <= mid && rcount <= right) {
		if (arr[lcount] <= arr[rcount]) {
			arr_b[bcount++] = arr[lcount++];
		} else {
			arr_b[bcount++] = arr[rcount++];
		}
	}

	if (lcount > mid) {
		while (rcount <= right) {
			arr_b[bcount++] = arr[rcount++];
		}
	} else {
		while (lcount <= mid) {
			arr_b[bcount++] = arr[lcount++];
		}
	}

	for (bcount = 0; bcount < right - left + 1; bcount++) {
		arr[left + bcount] = arr_b[bcount];
	}
	free(arr_b);
}

int main() {
	srand(time(NULL));

	const int TEST_SIZE = 1000;

	int* test = malloc(sizeof(int) * TEST_SIZE);

	for (int i = 0; i < TEST_SIZE; i++) {
		test[i] = rand() % 100;
	}

	mergesort(test, TEST_SIZE);
	for (int i = 0; i < TEST_SIZE; i++) {
		printf("%d ", test[i]);
	}
}
