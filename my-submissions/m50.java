class Solution {
    public double myPow(double x, int n) {
        return myPow(x, (long) n);

    }
    private double myPow(double x, long n) {
        if (n == 0) 
            return 1.;

        if (n < 0)
            return 1 / myPow(x, n * -1);
        
        if (n == 1)
            return x;

        double half = myPow(x, n / 2);
        long remainder = n % 2;

        if (remainder == 1)
            return half * half * x;
        return half * half;
    }
}