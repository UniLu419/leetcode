class Solution {
    public String convert(String s, int numRows) {
        String ans="";
        if (numRows == 1) {return s;}
        int cons=2*numRows-2;
    	for (int i = 0; i< numRows; i++) {
        	for (int j = i; j<s.length(); j= j+cons) {
        		ans = ans+s.charAt(j);
        		if ((i != 0)&&(i != numRows-1)&&(j- i*2+cons <s.length())){
        			ans = ans+s.charAt(j- i*2+cons);
        		}
        	}
        }
    	return ans;
    }
}