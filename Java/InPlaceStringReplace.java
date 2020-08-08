class InPlaceReverse {
  public static void main(String[] args) {
    // Java Strings are immutable
    String s = "umang";
    System.out.println(reverse(s));
  }

  public static String reverse(String s) {
    char[] str = s.toCharArray();
    for(int i=0; i<str.length/2; i++) {
      char temp = str[i];
      str[i] = str[str.length-i-1];
      str[str.length-i-1] = temp;
    }
    return new String(str);
  }
}