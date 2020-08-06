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
        int carry=0, t1, t2, sum;
        ListNode temp = new ListNode(0);
        ListNode p=l1, q=l2, curr=temp;
        while(p!=null || q!=null || carry>0) {
            t1= p!=null?p.val:0;
            t2= q!=null?q.val:0;
            sum=t1+t2+carry;
            carry=sum/10;
            sum=sum%10;
            curr.next = new ListNode(sum);
            if(p!=null) p=p.next;
            if(q!=null) q=q.next;
            curr=curr.next;
        }
        return temp.next;
        // curr=temp;
        // return curr.next;
    }
}