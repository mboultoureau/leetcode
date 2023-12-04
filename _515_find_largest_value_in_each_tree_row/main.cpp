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
    vector<int> largestValues(TreeNode* root) {
        if (root == NULL) {
            return vector<int>();
        }

        vector<int> result;
        deque<TreeNode*> queue;
        queue.push_back(root);

        while (!queue.empty()) {
            int maximum = INT_MIN;
            int length = queue.size();

            for (int i = 0; i < length; i++) {
                TreeNode* node = queue.front();
                queue.pop_front();
                if (node->left != NULL) {
                    queue.push_back(node->left);
                }

                if (node->right != NULL) {
                    queue.push_back(node->right);
                }

                maximum = max(node->val, maximum);
            }

            result.push_back(maximum);
        }

        return result;
    }
};