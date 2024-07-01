bool isAnagram(char* s, char* t) {
    int letters[26] = {0};

    while (*s) {
        letters[*s - 'a']++;
        s++;
    }

    while (*t) {
        letters[*t - 'a']--;
        t++;
    }

    for (int i = 0; i < 26; i++) {
        if (letters[i]) {
            return false;
        }
    }
    return true;
}