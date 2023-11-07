import java.util.Arrays;

class Solution {
    public int lengthOfLongestSubstring(String s) {
        int lastRepeatPos=-1,res=0;
        int[] arr= new int[256];
        Arrays.fill(arr, -1);
        
        for (int i = 0; i<s.length(); i++) {
        	int index = (int)s.charAt(i);
        	if ((arr[index]!= -1)&&(arr[index]> lastRepeatPos)) {
        		lastRepeatPos = arr[index];
        	}
        	if (i - lastRepeatPos > res) {
        		res = i - lastRepeatPos;
        	}
        	arr[index] = i;
        }
        return res;
    }
}