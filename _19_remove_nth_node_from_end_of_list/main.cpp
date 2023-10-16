/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        // With NeetCode video

        // If only one node
        if (head->next == NULL)
        {
            return NULL;
        }

        ListNode* fast = head;
        ListNode* slow = head;

        // Move fast by n
        while (n > 0)
        {
            fast = fast->next;
            n--;
        }

        // If the first element is deleted
        if (fast == NULL)
        {
            return head->next;
        }

        // Advance slow and fast until reach the end
        while (fast->next != NULL)
        {
            fast = fast->next;
            slow = slow->next;
        }

        // Remove the node
        slow->next = slow->next->next;

        return head;


        // My solution
        // // Count number of nodes
        // int count = 0;
        // ListNode* current = head;
        // while (current != NULL)
        // {
        //     count++;
        //     current = current->next;
        // }

        // cout << "count: " << count << endl;

        // // Find the node
        // n = count - n - 1;
        // count = 0;
        // current = head;

        // // If is the first node
        // if (n == -1)
        // {
        //     return current->next;
        // }

        // while (count != n)
        // {
        //     current = current->next;
        //     count++;
        // }

        // // Remove the node
        // current->next = current->next->next;

        // return head;
    }
};