
def binary_search(arr,item):
    low=0;
    high=len(arr)-1;
    while low<=high:
        mid=(low+high)//2
        guess=arr[mid]
        if guess==item:
            return mid
        elif guess>item:
            high=mid-1
        else:
            low=mid+1
    return None
        

my_list=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33]
print("position :",binary_search(my_list,21)) 