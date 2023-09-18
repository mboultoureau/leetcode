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
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        if (list1 == NULL && list2 == NULL)
        {
            return NULL;
        }

        if (list1 == NULL)
        {
            return list2;
        }

        if (list2 == NULL)
        {
            return list1;
        }

        ListNode* newList = new ListNode();
        ListNode* current = newList;
        while (list1 != NULL && list2 != NULL)
        {
            if (list1->val <= list2->val)
            {
                current->next = list1;
                list1 = list1->next;
            }
            else
            {
                current->next = list2;
                list2 = list2->next;
            }

            current = current->next;
        }

        if (list1 != NULL)
        {
            current->next = list1;
        }
        else
        {
            current->next = list2;
        }

        return newList->next;
    }
};