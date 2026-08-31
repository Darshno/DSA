class Solution {
    public boolean isAnagram(String s, String t) {
        if (s.length() != t.length()){
            return false;
        }
        Map<Character,Integer> f = new HashMap <>();
        for (char c:s.toCharArray()){
            f.put(c,f.getOrDefault(c,0)+1);
        }
        for (char c:t.toCharArray()){
            f.put(c,f.getOrDefault(c,0)-1);
        }
        for(int x:f.values()){
            if (x!= 0){
                return false;
            }
        }
        return true;
    }
}