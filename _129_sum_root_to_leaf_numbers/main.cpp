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
    int number_ { 0 };

public:
    int sumNumbers(TreeNode* root) {
        number_ = number_ * 10 + root->val;

        if (!root->left && !root->right) {
            return number_;
        }

        int n = number_;
        int sum_ = 0;

        if (root->left) {
            sum_ += sumNumbers(root->left);
        }

        number_ = n;

        if (root->right) {
            sum_ += sumNumbers(root->right);
        }

        return sum_;
    }
};