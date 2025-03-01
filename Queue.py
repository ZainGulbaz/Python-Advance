class Queue:
    
    def __init__(self):
        self.queue=[];
        
    def enqueue(self,data):
        self.queue.append(data);
        
    def dequeue(self):        
        if(len(self.queue)==0):
            print("Queue is Empty");
            return;
        
        return self.queue.pop(0);
    
    def print_queue(self):
            temp_queue=self.queue;
            temp_queue.reverse();
            print("-> ".join(temp_queue));
    
    def seek(self):
        print(self.queue[0]);
        

queue=Queue();
queue.enqueue("Black");
queue.enqueue("Red");
queue.enqueue("Pink");

queue.dequeue();
queue.dequeue();
queue.dequeue();
queue.dequeue();
queue.dequeue();

queue.print_queue();            
            