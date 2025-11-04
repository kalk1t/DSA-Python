def factorial(n):
    if n==0 or n==1:
        return 1
    else:
        return n*factorial(n-1)

def sum(arr):
    if arr==[]:
        return 0
    else:
        return arr[0]+sum(arr[1:])

def count_in_list(arr):
    if arr==[]:
        return 0
    else:
        return 1+count_in_list(arr[1:])

def max_in_list(arr):
    if len(arr)==1:
        return arr[0]
    else:
        if arr[0]>max_in_list(arr[1:]):
            return arr[0]
        else:
             return max_in_list(arr[1:])

def quicksort(arr):
    
    if len(arr)<2:
        return arr
    else:
        pivot=arr[0]
        less=[i for i in arr[1:] if i<=pivot]
        greater=[i for i in arr[1:] if i>pivot]
        return quicksort(less)+[pivot]+quicksort(greater)

def multiplication_table(arr):
    if len(arr)==0:
        return []
    
    array=[]
    for j in range(len(arr)):
        row=[]
        for i in range(len(arr)):
            row.append(arr[j]*arr[i])
        array.append(row)
    return array

array=[2,3,7,8,10]
print(multiplication_table(array))