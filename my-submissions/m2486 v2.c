int appendCharacters(char* s, char* t) {
    int tPoint = 0;
    int sPoint = 0;

    while (s[sPoint]) {
        if (t[tPoint] == s[sPoint]) {
            tPoint++;
        }
        sPoint++;
    }

    int counter = 0;
    while (t[tPoint]) {
        counter++;
        tPoint++;
    }

    return counter;

}