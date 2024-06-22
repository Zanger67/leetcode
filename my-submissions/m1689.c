int minPartitions(char* n) {
    int output = 0;
    
    while (*n) {
        output = *n - '0' < output ? output : (*n - '0');
        n++;
    }

    return output;
}