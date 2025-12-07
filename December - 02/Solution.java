import java.util.*;
public class Solution {
    public static void main(String[] args)
    {
        Scanner scan = new Scanner(System.in);
        int n = scan.nextInt();
         int width = Integer.toBinaryString(n).length();
        for(int i=1;i<=n;i++){
           String dec = String.valueOf(i);
           String oct = Integer.toOctalString(i);
            String hex =Integer.toHexString(i).toUpperCase();
            String binary = Integer.toBinaryString(i);
            System.out.printf("%"+width+"s %"+width+"s %"+width+"s %"+width+"s\n",dec,oct,hex,binary);
        }
    }
}
