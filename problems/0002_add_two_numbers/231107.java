/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode temp1=l1;
        ListNode temp2=l2;
        ListNode curr = new ListNode(0);
        ListNode res = curr;
    	
    	while ((temp1 != null)||(temp2 != null)){
            if (temp1 == null) {
    			temp1 = new ListNode(0);
    		}
    		if (temp2 == null) {
    			temp2 = new ListNode(0);
    		}
	    	int sum = temp1.val + temp2.val + curr.val;
	        if (sum >= 10) {
	        	sum = sum-10;
	        	curr.next = new ListNode(1);
	        }
	        curr.val = sum;
	        if((temp1.next != null)||(temp2.next != null)) {
	        	if (curr.next == null) {
		        	curr.next = new ListNode(0);
	        	}
	        	curr = curr.next;
	        }
	        temp1 = temp1.next;
	        temp2 = temp2.next;
	        
	    }
	    return res;
    }
}