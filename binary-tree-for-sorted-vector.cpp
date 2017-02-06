//leetcode 108


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
    TreeNode *sortedArrayToBST(vector<int> &nums) {
        if (nums.empty()){
            return NULL;
        }
        if (nums.size() == 1){
            return new TreeNode(nums[0]);
        }
        
        int mid = (nums.size()/2);
        TreeNode* root = new TreeNode(nums[mid]);
        
        vector<int> leftTree(nums.begin(), nums.begin()+mid);
        vector<int> rightTree(nums.begin()+mid+1, nums.end());
        
        root->left = sortedArrayToBST(leftTree);
        root->right = sortedArrayToBST(rightTree);
        
        return root;
    }
};