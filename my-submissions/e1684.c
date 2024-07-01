// Pure brute force
int countConsistentStrings(char * allowed, char ** words, int wordsSize){
    int output = 0;

    for (int i = 0; i < wordsSize; i++) {
        char* word = words[i];
        
        bool failed = true;
        while (*word) {
            failed = true;
            char* allowedPtr = allowed;
            while (*allowedPtr) {
                if (*allowedPtr == *word) {
                    failed = false;
                    break;
                }
                allowedPtr++;
            }
            if (failed) {
                break;
            }
            word++;
        }
        if (!failed) {
            output++;
        }
    }

    return output;
}