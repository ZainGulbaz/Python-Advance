arr=[2,5,1,4,9,3]

for i in range(0,len(arr)):
    for j in range(0,len(arr)-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j];
            
print(arr);