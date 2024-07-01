int clumsy(int n) {
    switch (n) {
        case 4 :
            return 7;
        case 3 :
            return 6;
        case 2 :
        case 1 :
        case 0 :
            return n;
        default :
            break;
    }

    switch (n % 4) {
        case 3 :
            return n - 1;
        case 2 :
        case 1 :
            return n + 2;
        default :
            return n + 1;
    }
}