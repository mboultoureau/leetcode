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
    int goodNodes(TreeNode* root) {
        return explore(root, INT_MIN);
    }

    int explore(TreeNode* root, int maximum) {
        if (root == NULL) {
            return 0;
        }

        int count = 0;
        if (root->val >= maximum) {
            count = 1;
        }

        return count + explore(root->left, max(root->val, maximum)) +  explore(root->right, max(root->val, maximum));
    }
};