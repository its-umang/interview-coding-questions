// Manchar Algorithm
// For Dynamic Programming see: Leetcode/5_Longest_Palindromic_Substring.java

class LongestPalindromicSubstring {
  public static void main(String[] args) {
    String s1 = "racecar";
    String s2 = "abba";
    String s3 = "abcbd";
    System.out.println(longPalSS(s1));
    System.out.println(longPalSS(s2));
    System.out.println(longPalSS(s3));
  }

  public static String longPalSS(String s) {
    if(s==null || s.length() < 1) return "";

    int start = 0, end = 0;
    for(int i=0; i<s.length(); i++) {
      int len1 = expandCenter(s, i, i);
      int len2 = expandCenter(s, i, i+1);
      int len = Math.max(len1, len2);
      if(len > end - start) {
        start = i - ((len-1)/2);
        end = i + (len/2);
      }
    }

    return s.substring(start, end+1);
  }

  public static int expandCenter(String s, int left, int right) {
    if(s == null || left > right) return 0;
    while(left >= 0 && right < s.length() && s.charAt(left) == s.charAt(right)) {
      left--;
      right++;
    }
    return right-left-1;
  }
}