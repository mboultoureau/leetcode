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
    // Second solution: worst
    // int maxDepth(TreeNode* root) {
    //     if (root == NULL)
    //     {
    //         return 0;
    //     }

    //     return 1 + max(maxDepth(root->left), maxDepth(root->right));
    // }

    // First solution
    int maxDepth(TreeNode* root) {
        return depth(root, 0);
    }

    int depth(TreeNode* root, int n)
    {
        if (root == NULL)
        {
            return n;
        }

        return max(depth(root->left, n + 1), depth(root->right, n + 1));
    }
};