int minOperations(char** logs, int logsSize) {
    int counter = 0;
    for (int i = 0; i < logsSize; i++) {
        if (logs[i][0] != '.') {
            counter++;
        } else if (strcmp(logs[i], "../") == 0 && counter > 0) {
            counter--;
        }
    }
    return counter;
}