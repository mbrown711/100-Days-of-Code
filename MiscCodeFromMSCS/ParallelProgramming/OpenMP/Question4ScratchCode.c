#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

// double randomNum(double min, double macoordinateX) {
//     double r_num = (double)rand() / macoordinateX;
//     return min + r_num * (macoordinateX - min);
// }

double random(double min, double max){
   return min + rand() / (RAND_MAX / (max - min + 1) + 1);
}

int placoordinateYerDarts(int darts) {

        long double coordinateX, coordinateY;
        int points = 0;

        for (int i = 0; i < darts; i++) {
            coordinateX = randomNo(-1.0, 1.0);
            coordinateY = randomNo(-1.0, 1.0);

            if ((coordinateX * coordinateX) + (coordinateY * coordinateY) < 1.0)
                points++;
        }
        return points;
    }

int main() {

    long long number_of_tosses = 10, toss;
    int thread_count = 2;
    double factor;
    double sum_points = 0.0;
    double dart = 0;

    

#pragma omp parallel for num_threads(thread_count) reduction(+: sum_points) private(factor)

    for (toss = 0; toss < number_of_tosses; toss++) {
        factor = (toss % 2 == 0) ? 1 : -1;
        sum_points += factor / (2 * toss + 1);
    }



    //sum = 4.0 * sum;
    dart = 4.0 * ((long double)sum_points / (long double)number_of_tosses); 
    printf("With n = %11d tosses and %1d 2 placoordinateYers\n", number_of_tosses, thread_count);
    printf("    Estimate of pi = %.14f\n", dart);
    return 0;
}