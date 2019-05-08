#include <stdio.h>
#include <stdlib.h>
#include <omp.h>

float randomNo() {
	return -1 + 2 * ((float)rand()) / RAND_MAX;
}

int main() {

    int numberOfTosses, thread_count; // number of tosses - how many times thru for loop
    int toss, numberInCircle = 0;
	float piEstimate;
    float hitX, hitY, distanceSquared;

    printf("How many tosses (Enter > 1000)? ");
    scanf("%d", &numberOfTosses);
    printf("How many threads? ");
    scanf("%d", &thread_count);
	

	#pragma omp parallel num_threads(thread_count) reduction(+:numberInCircle) private(hitX, hitY, toss, distanceSquared)
		
		for (toss = 0; toss < numberOfTosses; toss++)	{
			
            hitX = randomNo();	// random x hit
			hitY = randomNo();	// random y hit
			
            distanceSquared = ((hitX * hitX) + (hitY * hitY));	// makes sure the hit is inside the circle
			
            if (distanceSquared <= 1) {
				numberInCircle++;
			}		
		}
	 
	piEstimate = 4.0 * ((float)numberInCircle / (float)(numberOfTosses * thread_count));
	printf("Our estimation of pi is: %.14f\n", piEstimate);
	return 0;
}