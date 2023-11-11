class Solution {
    public String longestPalindrome(String s) {
    	String submax="",subtemp;
    	if (s.length()==1) {return s;}
        for (int i = 0; i< s.length(); ++i) {
        	subtemp="";
        	for (int j = 0;(j<=i)&&(j<(s.length()-i));++j) {
        		if (s.charAt(i-j)!=(s.charAt(i+j))){
        			break;
        		}
        		subtemp = s.substring(i-j, i+j+1);
        	}
        	if (subtemp.length() > submax.length()) {
        		submax = subtemp;
        	}
        }
        for (int i = 0; i< s.length(); ++i) {
        	subtemp="";
        	for (int j = 0;(j<=i)&&(j<(s.length()-i-1));++j) {
        		if (s.charAt(i-j)!=(s.charAt(i+j+1))){
        			break;
        		}
        		subtemp = s.substring(i-j,i+j+2);
        	}
        	if (subtemp.length() > submax.length()) {
        		submax = subtemp;
        	}
        }
        return submax;
    }
}