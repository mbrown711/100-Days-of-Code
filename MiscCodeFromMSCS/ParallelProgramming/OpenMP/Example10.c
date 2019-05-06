// this example doesn't produce the correct answer every time (may for a long time, but no guarantee)
// can fix by making factor private (see example 11)

#include <stdio.h>
#include <math.h>
#include <omp.h>

int main() {
    long long n = 10, k;
    int thread_count = 2;
    double sum = 0.0, factor;

    #pragma omp parallel for num_threads(thread_count) reduction(+: sum)

        for (k = 0; k < n; k++) {
            factor = (k % 2 == 0) ? 1 : -1;
            sum += factor / (2 * k + 1);
        }

        sum = 4.0 * sum;
        printf("With n = %11d terms and %d threads,\n", n, thread_count);
        printf("    Our estimate of pi = %.14f\n", 4.0 * atan(1.0));
        return 0;
}