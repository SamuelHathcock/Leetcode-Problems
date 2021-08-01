class Solution {
    public static String longestCommonPrefix(String[] strs) {
        String prefix = strs[0].substring(0, 2);
        for(String s : strs){
            System.out.printf(s + "\n");
//            if (s.substring(0,2) != prefix){
//                return "";
//            }
        }
        return prefix;
    }


    public static void main(String[] args) {
        String pre = "wahahahah";
        String[] strs = {"bah", "bash", "bahh", "baha"};

        System.out.println(longestCommonPrefix(strs));
    }
}