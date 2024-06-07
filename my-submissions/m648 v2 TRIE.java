// https://leetcode.com/problems/replace-words/description/?envType=daily-question&envId=2024-06-07


// This could be better optimized by just having an array of 26 elements instead of a hashmap
// HashMap creation results in major cost time-wise and complexity (space) wise
// Since it's mapped to 26 lowercase chars, it's simpler that way since the spots will just be null
// when undeclared /shrug

class Solution {
    public String replaceWords(List<String> dictionary, String sentence) {
        helper trie = new helper();
        for (String s : dictionary) {
            helper currentNode = trie;
            for (Character c : s.toCharArray()) {
                if (currentNode.end) { // unnecessary to continue since exists a prefix that's shorter 
                    break;
                }

                if (currentNode.vals.containsKey(c)) {
                    currentNode = currentNode.vals.get(c);
                } else {
                    currentNode = currentNode.addCase(c);
                }
            }
            currentNode.end = true;
        }

        StringBuilder output = new StringBuilder();
        for (String word : sentence.split(" ")) {
            helper currentNode = trie;
            for (Character c : word.toCharArray()) {
                output.append(c);
                if (currentNode == null) {
                    continue;
                }

                if (currentNode.end) {
                    output.deleteCharAt(output.length() - 1);
                    break;
                }
                
                currentNode = currentNode.vals.getOrDefault(c, null);
            }
            output.append(" ");
        }

        output.deleteCharAt(output.length() - 1);
        return output.toString();
    }

    class helper {
        private HashMap<Character, helper> vals;
        private boolean end = false;
        
        public helper() {
            this.vals = new HashMap<>();
        }

        public helper addCase(Character c) {
            if (end) {
                return null;
            }

            vals.put(c, new helper());
            return vals.get(c);
        }
    }
}