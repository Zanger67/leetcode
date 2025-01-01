int maxScore(char* s) {
    int left_zeros = 0, right_ones = 0;
    
    char* curr = s;
    while (*curr) {
        if (*curr == '1') {
            right_ones += 1;
        }
        curr += 1;
    }

    curr = s;
    int maxx = 0;

    while (*curr && *(curr + 1)) {
        if (*curr == '1') {
            right_ones -= 1;
        } else {
            left_zeros += 1;
        }
        
        if (left_zeros + right_ones > maxx) {
            maxx = left_zeros + right_ones;
        }
        curr += 1;
    }

    return maxx;
}
