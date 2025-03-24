import os


# with open("Sample.txt","w") as file:
#     file.write("Hello, How are you? I hope that you are doing wellllll");



is_present = os.path.exists("Sample.txt");

if is_present:

    with open("Sample.txt","r") as file:
        text = file.read();
        print(text);
else:
    print("File does not exist");


# with open("Sample.txt","a") as file:
#     file.write(".I am fasting today");


# is_present = os.path.exists("Sample.txt");
# if is_present == True:
#     os.remove("Sample.txt");
# else:
#     print("File is not present :(");

# is_present = os.path.exists("Car.py");
# print(is_present);