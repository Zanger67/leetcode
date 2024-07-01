long helper(long orig, long substrLen) {
    return (orig + (substrLen + 1) * substrLen / 2) % (1000000000 + 7);
}

int countHomogenous(char * s){
    int leftIndx = 0;
    int currentIndx = 0;
    char leftChar = *s;
    long output = 0;

    while (*s) {
        if (*s != leftChar) {
            leftChar = *s;
            output = helper(output, (long) (currentIndx - leftIndx));
            leftIndx = currentIndx;
        }

        currentIndx++;
        s++;
    }
    output = helper(output, (long) (currentIndx - leftIndx));

    return output;

}