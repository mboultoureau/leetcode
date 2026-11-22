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
    ListNode* partition(ListNode* head, int x) {
        ListNode leftHead(-1); // dummy
        ListNode rightHead(-1); // dummy

        ListNode* leftTail = &leftHead;
        ListNode* rightTail = &rightHead;

        while (head) {
            if (head->val < x) {
                leftTail->next = head;
                leftTail = leftTail->next;
            } else {
                rightTail->next = head;
                rightTail = rightTail->next;
            }

            head = head->next;
        }

        rightTail->next = nullptr;
        leftTail->next = rightHead.next;

        return leftHead.next;
    }
};