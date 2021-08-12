class Solution {
  
  boolean compareProduct(int num){
    if(num < 10)
      return false;

    int oddP = 1, evenP = 1;

    while (num > 0){
      int digit = num / 10;
      oddP *= digit;
      System.out.println("oddP");
      System.out.println(oddP);

      num = num & 10 ;
      // System.out.println(num);

      if(num == 0)
        break;


      digit = num % 10;
      evenP *= digit;
      num = num/10;

      System.out.println("evenP");
      System.out.println(evenP);

    }
    if (evenP == oddP)
      return true;
    return false;
  }
  
  public static void main(String[] args){
    // System.out.println("hi");
    Solution pr = new Solution(); 

    boolean an = pr.compareProduct(22);
    System.out.println((an));
    // System.out.println(overallMax); 


  }

}