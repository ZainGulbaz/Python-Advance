class Node:
    def __init__(self,data):
        self.data=data;
        self.left=None;
        self.right=None;



class Tree:
    
    # def __init__(self,root):
    #     self.root=root;
    
    def add_node(self,root,data):
        
        if data > root.data:
            if root.left is not None:
                self.add_node(root.left,data);
            else:
                root.left= Node(data);    
        else:
            if root.right is not None:
                self.add_node(root.right,data);
            else:
                root.right=Node(data);
    
    def pre_order_traversal(self,root):
        if root is not None:
            print(root.data);
            self.pre_order_traversal(root.left);
            self.pre_order_traversal(root.right);
    
    def post_order_traversal(self,root):
        if root is not None:
            self.post_order_traversal(root.left);
            self.post_order_traversal(root.right);
            print(root.data);
            
    def in_order_traversal(self,root):
        if root is not None:
            self.in_order_traversal(root.left);
            print(root.data);
            self.in_order_traversal(root.right);


root= Node(12);

tree= Tree();

tree.add_node(root,14);
tree.add_node(root,13);
tree.add_node(root,10);
tree.add_node(root,9);

# tree.pre_order_traversal(root);
# tree.post_order_traversal(root);
tree.in_order_traversal(root);

"""
      12
    14   10
      13   9
      
    pre order--> 12 -> 14 -> 13 -> 10 -> 9
    post order --> 13 -> 14 -> 9 -> 10 -> 12

"""


