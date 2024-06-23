double myPowLong(double x, long n) {
    if (n == 0) 
        return 1.;

    if (n < 0)
        return 1 / myPowLong(x, n * -1);
    
    if (n == 1)
        return x;

    double half = myPowLong(x, n / 2);
    long remainder = n % 2;

    if (remainder == 1)
        return half * half * x;
    return half * half;
}

double myPow(double x, int n) {
    return myPowLong(x, (long) n);
}
