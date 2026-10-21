class Solution {
    public List<Integer> inorderTraversal(TreeNode root) {
        List<Integer> trav = new ArrayList<>();
        recur(root, trav);
        return trav;
    }
    public void recur(TreeNode root, List<Integer> trav) {
        if(root==null) {
            return;
        }
        recur(root.left, trav);
        trav.add(root.val);
        recur(root.right, trav);
    }
}