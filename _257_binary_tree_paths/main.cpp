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
    vector<string> paths_;

public:
    vector<string> binaryTreePaths(TreeNode* root) {
        explore(root, to_string(root->val));
        return paths_;
    }

    void explore(TreeNode* root, string current) {
        if (!root->left && !root->right) {
            paths_.push_back(current);
            return;   
        }

        if (root->left) {
            explore(root->left, current + "->" + to_string(root->left->val));
        }

        if (root->right) {
            explore(root->right, current + "->" + to_string(root->right->val));
        }
    }
};