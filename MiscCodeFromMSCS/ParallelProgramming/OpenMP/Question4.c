#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <omp.h>

double random(double min, double max){
   return min + rand() / (RAND_MAX / (max - min + 1) + 1);
}

int main() {

long long int numberOfTosses;
long long int hitsInCircle;
long long int toss;
int coordinateX, coordinateY;
int distanceSquared;
float piEstimate = 0;

printf("How many tosses (Enter a Number > 10000): ");
scanf("%d", &numberOfTosses);

#pragma omp parallel for num_threads(thread_count) reduction(+: piEstimate) private(hitsInCircle)

//random number generator (Monte Carlo method):
for (toss = 0; toss < numberOfTosses; toss++) {
    coordinateX = random(-1.0, 1.0);
    coordinateY = random(-1.0, 1.0);

    distanceSquared = coordinateX * coordinateX + coordinateY + coordinateY

    if (distanceSquared <= 1) {
        hitsInCircle++;
    }
}

piEstimate = 4 * hitsInCircle / ((double)numberOfTosses);

//print the outputs here:

}