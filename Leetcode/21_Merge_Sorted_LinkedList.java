/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode(int x) { val = x; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {
        ListNode temp = new ListNode(0);
        ListNode curr = temp, p=l1, q=l2;
        while(p!=null && q!=null)
        {
            int x = (p != null) ? p.val : 0;
            int y = (q != null) ? q.val : 0;
            if(x<y)
            {
                curr.next = new ListNode(x);
                if(p!=null)
                    p=p.next;
            }
            else
            {
                curr.next = new ListNode(y);
                if(q!=null)
                    q=q.next;
            }
            curr = curr.next;
        }
        while(p!=null)
        {
            curr.next = new ListNode(p.val);
            p=p.next;
            curr = curr.next;
        }
        while(q!=null)
        {
            curr.next = new ListNode(q.val);
            q=q.next;
            curr = curr.next;
        }
        return temp.next;
    }
}