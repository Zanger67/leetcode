/** 
 * Definition of commonSetBits API.
 * int commonSetBits(int num);
 */

int findNumber(){
	int x = 1; // I'm assuming that this iteration of C is 32-bit ints
    int output = 0;

    for (int i = 0; i < 30; i++) {
        if (commonSetBits(x)) {
            output += x;
        }
        x = x << 2;
    }
    return output;
}