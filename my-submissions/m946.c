bool validateStackSequences(int* pushed, int pushedSize, int* popped, int poppedSize) {
    int stack[pushedSize];
    memset(stack, 0, sizeof(int) * pushedSize);
    int stackIndx = 0;

    int push = 0;
    int pop = 0;
    while (push < pushedSize || pop < poppedSize) {
        if (stackIndx != 0 && popped[pop] == stack[stackIndx - 1]) {
            stackIndx--;
            pop++;
        } else if (push < pushedSize) {
            stack[stackIndx] = pushed[push];
            push++;
            stackIndx++;
        } else {
            return false;
        }

    }

    return true;
}