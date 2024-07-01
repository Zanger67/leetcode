// CAUSE WHY NOT
// It's slower though than the alternative unfortunately :l

class Solution {
    public List<String> fizzBuzz(int n) {
        HashMap<Integer, String> vals = new HashMap<>();
        vals.put(0, "FizzBuzz");
        vals.put(10, "Buzz");
        vals.put(5, "Buzz");
        vals.put(3, "Fizz");
        vals.put(6, "Fizz");
        vals.put(9, "Fizz");
        vals.put(12, "Fizz");

        ArrayList<String> output = new ArrayList<>();
        for (int i = 1; i <= n; i++) {
            output.add(vals.getOrDefault(i % 15, "" + i));
        }
        
        return output;
    }
}