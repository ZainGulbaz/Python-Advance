arr=[1,2,3,4,5,6,7]

def binary_search(arr,target,previous_mid_index):

    if(len(arr)==0):
        print("Not Found");
        return;
        
    mid_index= int(len(arr)/2)
    mid_element=arr[mid_index]
    
    previous_mid_index=len(arr)+previous_mid_index;
    
    if target < mid_element:
        binary_search(arr[0:mid_index],target,previous_mid_index);
    elif target > mid_element:
        binary_search(arr[mid_index+1:len(arr)],target,previous_mid_index);
    elif target==mid_element:
        print("Element Found",previous_mid_index);



binary_search(arr,7,0);