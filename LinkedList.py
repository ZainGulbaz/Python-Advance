

class Node:
    
    def __init__(self,data):
        self.data=data;
        self.next=None;
        

class LinkedList:
    
    def __init__(self):
        self.header=None;
    
    def add_node(self,data):
        
        new_node=Node(data);
        
        #User is adding node for the first time
        
        if self.header is None:
            self.header=new_node;
        else:
            temp_node=self.header;

            # traversing untill we get to tail -> node.next=None;
            while temp_node.next:
                temp_node=temp_node.next;

            temp_node.next=new_node;
            
    def print_list(self):
        temp_node=self.header;

        while temp_node:
            print(temp_node.data);
            temp_node=temp_node.next;
            
    def delete_node(self,data):
        
        temp_node=self.header;
        
        # targeted node is header
        if(temp_node.data==data):
            self.header=temp_node.next;
            print("We are add header");
        else:
            while temp_node.next:
                
                if temp_node.next.data==data:
                    temp_node.next=temp_node.next.next;
                
                temp_node=temp_node.next;
            

ll = LinkedList();

ll.add_node(5);

ll.add_node(6);

ll.add_node(7);

# 5 -> 6 > 7 -> None

ll.print_list();


print("Deleting the node");
# ll.delete_node(6);
ll.delete_node(5);


ll.print_list();