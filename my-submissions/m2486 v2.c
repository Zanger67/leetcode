// https://leetcode.com/problems/append-characters-to-string-to-make-subsequence/?envType=daily-question&envId=2024-06-03

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