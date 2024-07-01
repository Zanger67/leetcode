int longestPalindrome(char* s) {
    int* reference = (int*) malloc(sizeof(int) * 52);

    for (int i = 0; i < 52; i++) {
        reference[i] = 0;
    }

    int index = 0;
    while (s[index]) {
        printf("%c", s[index]);
        if (s[index] < 91) { // uppercase
            reference[s[index] - 'A']++;
        } else {
            reference[s[index] - 'a' + 26]++;
        }
        index++;
    }

    int counter = 0;
    bool odd = false;
    for (int i = 0; i < 52; i++) {
        if (reference[i] % 2 == 1) {
            odd = true;
            counter -= 1;
        }
        counter += reference[i];
    }

    free(reference);
    return counter + (odd ? 1 : 0);

}