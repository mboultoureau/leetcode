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
private:
    int sum_ { 0 };

public:
    TreeNode* convertBST(TreeNode* root) {
        if (!root) {
            return nullptr;
        }

        // Explore right
        convertBST(root->right);

        // Increment
        sum_ += root->val;
        root->val = sum_;

        // Explore left
        convertBST(root->left);

        return root;
    }
};