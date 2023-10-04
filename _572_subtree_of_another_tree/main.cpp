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
    bool isSubtreeLevel(TreeNode* root, TreeNode* subRoot, int level) {
        if (subRoot == NULL && root == NULL)
        {
            return true;
        }

        if (subRoot == NULL || root == NULL)
        {
            return false;
        }

        if (
            root->val == subRoot->val &&
            isSubtreeLevel(root->left, subRoot->left, level + 1) &&
            isSubtreeLevel(root->right, subRoot->right, level + 1)
        )
        {
            return true;
        }
        
        if (level == 0 && (isSubtreeLevel(root->left, subRoot, 0) || isSubtreeLevel(root->right, subRoot, 0)))
        {
            return true;
        }

        return false;
    }
    
    bool isSubtree(TreeNode* root, TreeNode* subRoot) {
        return isSubtreeLevel(root, subRoot, 0);
    }
};