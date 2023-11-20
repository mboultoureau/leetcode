/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> rightSideView(TreeNode* root) {
        vector<int> result;
        deque<TreeNode*> queue;
        queue.push_back(root);

        while (queue.size() > 0)
        {
            TreeNode* lastNode = NULL;
            TreeNode* node = NULL;
            int size = queue.size();

            for (int i = 0; i < size; i++)
            {
                node = queue.front();
                queue.pop_front();
                if (node != NULL)
                {
                    lastNode = node;
                    queue.push_back(node->left);
                    queue.push_back(node->right);
                }
            }

            if (lastNode != NULL)
            {
                result.push_back(lastNode->val);
            }
        }

        return result;
    }
};