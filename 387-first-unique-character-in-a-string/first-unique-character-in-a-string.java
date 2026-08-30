class Solution {
    public int firstUniqChar(String s) {
        int[] f = new int[26];
        for(char c:s.toCharArray()){
            f[c - 'a']++;
        }
        char uc;
        for (int i=0;i<s.length();i++){
            char cur = s.charAt(i);
            if(f[cur - 'a'] == 1){
                return i;
            }
        }

        return -1 ;
    }
}