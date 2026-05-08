# Definition for Node
class Node:
    def __init__(self, x):
        self.data = x
        self.left = None
        self.right = None

class Solution:
    
    def isIdentical(self,root1,root2):
        
        if root1 is None and root2 is None:
            return True
        
        if root1 is None or root2 is None:
            return False 
            
        return(root1.data==root2.data and self.isIdentical(root1.left, root2.left) and self.isIdentical(root1.right, root2.right))
    
    def isSubTree(self, root1, root2):
        
        if root2 is None:
            return True 
            
        if root1 is None:
            return False 
            
        if self.isIdentical(root1,root2):
            return True
        
        return(self.isSubTree(root1.left,root2) or self.isSubTree(root1.right,root2))
