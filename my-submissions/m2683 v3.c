bool doesValidArrayExist(int* derived, int derivedSize) {
    bool out = true;
    while (derivedSize > 0) {
        out ^= *derived;
        derivedSize -= 1;
        derived += 1;
    }
    return out;
}