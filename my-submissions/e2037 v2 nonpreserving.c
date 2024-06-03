// https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/


// Faster version where you don't copy and free
// "Destroys" the original data in the sense that it's reordered

// Performance difference isn't that significant or noteworthy but still evident

int compareHelper(const void* one, const void* two) {
    return *((int *) one) - *((int *) two);
}

int minMovesToSeat(int* seats, int seatsSize, int* students, int studentsSize) {
    qsort(seats, seatsSize, sizeof(int), compareHelper);
    qsort(students, studentsSize, sizeof(int), compareHelper);

    int sumCounter = 0;
    for (int i = 0; i < studentsSize; i++) {
        sumCounter += abs(students[i] - seats[i]);
    }


    return sumCounter;
}