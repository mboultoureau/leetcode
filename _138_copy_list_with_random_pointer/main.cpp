/*
// Definition for a Node.
class Node {
public:
    int val;
    Node* next;
    Node* random;
    
    Node(int _val) {
        val = _val;
        next = NULL;
        random = NULL;
    }
};
*/

class Solution {
public:
    Node* copyRandomList(Node* head) {
        if (head == NULL)
        {
            return NULL;
        }

        unordered_map<Node*, Node*> associations;

        // First loop
        Node* newHead = new Node(head->val);
        newHead->random = head->random;
        associations.insert({head, newHead});
        Node* previous = newHead;
        Node* current = head->next;
        while (current != NULL)
        {
            Node* newNode = new Node(current->val);
            previous->next = newNode;
            newNode->random = current->random;

            associations.insert({current, newNode});

            previous = newNode;
            current = current->next;
        }

        // Second loop
        current = newHead;
        while (current != NULL)
        {
            current->random = associations[current->random];
            current = current->next;
        }

        return newHead;
    }
};