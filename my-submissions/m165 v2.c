int compareVersion(char* version1, char* version2) {
    int one = 0;
    int two = 0;

    while (true) {
        int oneRight = one + 1;
        int twoRight = two + 1;
        while (version1[oneRight] && version1[oneRight] != '.') {
            oneRight++;
        }
        while (version2[twoRight] && version2[twoRight] != '.') {
            twoRight++;
        }

        int oneVal = 0;
        int twoVal = 0;
        for (int i = one; i < oneRight; i++) {
            oneVal = 10 * oneVal + (version1[i] - '0');
        }
        for (int i = two; i < twoRight; i++) {
            twoVal = 10 * twoVal+ (version2[i] - '0');
        }

        if (oneVal < twoVal) {
            return -1;
        }
        if (oneVal > twoVal) {
            return 1;
        }

        one = oneRight;
        two = twoRight;

        if (!version1[oneRight] && !version2[twoRight]) {
            break;
        }
        if (!version1[oneRight]) {
            two++;
            break;
        }
        if (!version2[twoRight]) {
            one++;
            break;
        }
        one++;
        two++;
    }

    // Finish off one
    while (version1[one]) {
        int oneRight = one + 1;
        while (version1[oneRight] && version1[oneRight] != '.') {
            oneRight++;
        }

        int oneVal = 0;
        for (int i = one; i < oneRight; i++) {
            oneVal = 10 * oneVal + (version1[i] - '0');
        }

        if (oneVal < 0) {
            return -1;
        }
        if (oneVal > 0) {
            return 1;
        }
        if (!version1[oneRight]) {
            break;
        }

        one = oneRight + 1;
    }


    // Finish off two
    while (version2[two]) {
        int twoRight = two + 1;
        while (version2[twoRight] && version2[twoRight] != '.') {
            twoRight++;
        }
        int twoVal = 0;
        for (int i = two; i < twoRight; i++) {
            twoVal = 10 * twoVal + (version2[i] - '0');
        }

        if (twoVal > 0) {
            return -1;
        }
        if (twoVal < 0) {
            return 1;
        }
        if (!version2[twoRight]) {
            break;
        }

        two = twoRight + 1;
    }

    return 0;
}