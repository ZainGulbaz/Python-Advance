class Stack:
    
    def __init__(self):
        self.stack=[];
        self.push("None");

    def push(self,data):
        self.stack.append(data);
    
    def pop(self):
        return self.stack.pop()
    
    def size(self):
        return len(self.stack)
    
    def print(self):
        print("================")
        for element in self.stack:
            print(element);        
        print("=======   =========");
        

stack=Stack();

stack.push("Black");
stack.push("Red");
stack.push("Orange");
stack.push("Pink");

stack.print();

stack.pop();
stack.print();

stack.pop();
stack.print();

stack.pop();
stack.print();


    
    
    
    
    
    
    
    
#pop, push, size , print