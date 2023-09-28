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
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        ListNode* l1Head = l1;
        ListNode* l1Prev = NULL;
        int reminder = 0;
        
        do {
            int a = 0;
            int b = 0;

            if (l1 != NULL)
            {
                a = l1->val;
            }

            if (l2 != NULL)
            {
                b = l2->val;
            }

            int value = (a + b + reminder) % 10;
            reminder = (a + b + reminder) > 9 ? 1 : 0;

            if (l1 != NULL)
            {
                l1->val = value;
                l1Prev = l1;
                l1 = l1->next;
            }
            else
            {
                ListNode* newNode = new ListNode(value);
                l1Prev->next = newNode;
                l1Prev = newNode;
                l1 = NULL;
            }

            if (l2 != NULL)
            {
                l2 = l2->next;
            }
        } while (l1 != NULL || l2 != NULL);

        if (reminder)
        {
            ListNode* newNode = new ListNode(1);
            l1Prev->next = newNode;
        }

        return l1Head;
    }
};