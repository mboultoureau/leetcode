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
    bool isValidBST(TreeNode* root) {
        return exploreSubtree(root, LONG_MIN, LONG_MAX);
    }

    bool exploreSubtree(TreeNode* root, long minimum, long maximum)
    {
        if (root == NULL)
        {
            return true;
        }

        if (root->val <= minimum || root->val >= maximum)
        {
            return false;
        }

        return exploreSubtree(root->left, minimum, root->val) && exploreSubtree(root->right, root->val, maximum);
    }
};