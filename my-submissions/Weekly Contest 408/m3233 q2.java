class Solution {
    public int nonSpecialCount(int l, int r) {
        int smallestVal = (int) Math.ceil(Math.sqrt(l));
        int largestVal = (int) Math.floor(Math.sqrt(r));
        int leftIndx = 0;

        // # 2 isn't prime but is needed in this list unfort
        ArrayList<Integer> primes = new ArrayList<Integer>();
        primes.add(2);
        primes.add(3);
        primes.add(5);

        int offset = 2;
        int lastInt = primes.get(primes.size() - 1);
        while (lastInt * lastInt <= r) {
            int nextPrime = lastInt + offset;
            boolean isPrime = true;
            for (int prime : primes) {
                if (prime * prime > nextPrime) {
                    break;
                }
                if (nextPrime % prime == 0) {
                    isPrime = false;
                    break;
                }
            }
            
            if (isPrime) {
                offset = 2;
                primes.add(nextPrime);
                lastInt = nextPrime;
            }
            else
                offset += 2;
        }

        double rooted = Math.sqrt((double) l);
        int firstRoot = (int) Math.ceil(rooted);
        int starterIndx = (firstRoot == 1) ? 0 : Collections.binarySearch(primes, firstRoot);

        if (starterIndx <= -1) {
            starterIndx = -1 - starterIndx;
        }

        while (!primes.isEmpty() && primes.get(primes.size() - 1) * primes.get(primes.size() - 1) > r) {
            primes.remove(primes.size() - 1);
        }
        
        return r - l + 1 - (primes.size() - starterIndx);
    }
}