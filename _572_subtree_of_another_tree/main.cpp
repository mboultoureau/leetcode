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
    // SOLUTION 1
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

    // SOLUTION 2 (with NeetCode)
    // bool isSameSubtree(TreeNode* root, TreeNode* subRoot)
    // {
    //     if (subRoot == NULL && root == NULL)
    //     {
    //         return true;
    //     }

    //     if (subRoot == NULL || root == NULL)
    //     {
    //         return false;
    //     }

    //     if (subRoot->val != root->val)
    //     {
    //         return false;
    //     }

    //     return isSameSubtree(root->left, subRoot->left) && isSameSubtree(root->right, subRoot->right);
    // }

    // bool isSubtree(TreeNode* root, TreeNode* subRoot) {
    //     if (root == NULL)
    //     {
    //         return false;
    //     }

    //     if (isSameSubtree(root, subRoot))
    //     {
    //         return true;
    //     }

    //     return isSubtree(root->left, subRoot) || isSubtree(root->right, subRoot);
    // }
};