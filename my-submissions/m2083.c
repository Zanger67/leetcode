long long numberOfSubstrings(char* s) {
    long numChars[26] = {0};

    char* temp = s;
    while (*temp) {
        numChars[*temp - 'a']++;
        temp++;
    }
    
    long long output = 0;
    for (int i = 0; i < 26; i++) {
        output += (numChars[i] * (numChars[i] + 1)) / 2;
    }

    return output;
}