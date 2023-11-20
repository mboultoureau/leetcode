/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* lowestCommonAncestor(TreeNode* root, TreeNode* p, TreeNode* q) {
        if (min(p->val, q->val) <= root->val && max(p->val, q->val) >= root->val)
        {
            return root;
        }

        if (min(p->val, q->val) < root->val && root->left != NULL)
        {
            return lowestCommonAncestor(root->left, p, q);
        }
        else if (min(p->val, q->val) > root->val and root->right != NULL)
        {
            return lowestCommonAncestor(root->right, p, q);
        }
        else
        {
            return root;
        }
    }
};