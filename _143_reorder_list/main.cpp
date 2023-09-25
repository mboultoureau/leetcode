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
    void reorderList(ListNode* head) {
        // Find the middle of the list
        ListNode* slow = head;
        ListNode* fast = head->next;

        while (fast != NULL && fast->next != NULL)
        {
            slow = slow->next;
            fast = fast->next->next;
        }

        // Reverse second part of the list
        ListNode* prev = NULL;
        ListNode* next = NULL;
        ListNode* current = slow->next;

        while (current != NULL)
        {
            next = current->next;
            current->next = prev;
            prev = current;
            current = next;
        }

        // Unlink two lists
        slow->next = NULL;

        // Merge two lists
        ListNode* firstList = head;
        ListNode* secondList = prev;
        ListNode* firstListNext = NULL;
        ListNode* secondListNext = NULL;

        while (secondList != NULL)
        {
            firstListNext = firstList->next;
            secondListNext = secondList->next;
            firstList->next = secondList;
            secondList->next = firstListNext;
            firstList = firstListNext;
            secondList = secondListNext;
        }
    }
};