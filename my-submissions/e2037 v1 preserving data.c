int compareHelper(const void* one, const void* two) {
    if (*((int *) one) == *((int *) two)) {
        return 0;
    }
    if (*((int *) one) < *((int *) two)) {
        return -1;
    }
    return 1;
}

int minMovesToSeat(int* seats, int seatsSize, int* students, int studentsSize) {
    int* cpySeats = malloc(sizeof(int) * seatsSize);
    int* cpyStds = malloc(sizeof(int) * studentsSize);

    memcpy(cpySeats, seats, seatsSize * sizeof(*cpySeats)); 
    memcpy(cpyStds, students, studentsSize * sizeof(*cpyStds)); 

    qsort(cpySeats, seatsSize, sizeof(int), compareHelper);
    qsort(cpyStds, studentsSize, sizeof(int), compareHelper);

    int sumCounter = 0;
    for (int i = 0; i < studentsSize; i++) {
        sumCounter += abs(cpyStds[i] - cpySeats[i]);
    }

    free(cpySeats);
    free(cpyStds);

    return sumCounter;
}