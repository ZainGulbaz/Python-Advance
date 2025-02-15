

class Car:
    
    color=None;
    model=None;
    
    def set_color(self,color):
        self.color=color;
        
    def get_color(self):
        return self.color;
    
    def set_model(self,model):
        self.model=model;
    
    def get_model(self):
        return self.model;


class ElectricCar(Car):
    battery=None;
    
    def set_battery(self,battery):
        self.battery=battery;
        
    def get_battery(self):
        return self.battery;
    

tesla= ElectricCar(); 

tesla.set_color("White");

tesla.set_model("TS 400");

tesla.set_battery("LI 565");

print(tesla);



# Class 
# Attributes
# Objects
# Methods
# Getters
# Setters
# Inheritance