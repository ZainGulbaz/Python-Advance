class Car:
    model=None;
    color=None;
    __engineNo=None;
    
    
    def set_model(self,model):
        self.model=model;
        
    def set_color(self,color):
        self.color=color;
        
    def get_engineNo(self):
        print(self.__engineNo);    
        
    def set_engineNo(self,engineNo):
        self.__engineNo=engineNo;


bmw = Car();

bmw.set_color("Black");
bmw.set_engineNo("456");
bmw.set_model("BMW");

bmw.color="Red";

bmw.get_engineNo()



# class ElectricCar(Car):
#     batteryNo=None;
    
#     def set_batteryNo(self,batteryNo):
#         self.batteryNo=batteryNo;
        
#     def set_engineNo(self,engineNo):
#         print("Error: Electric Car has no Engine No");
        

