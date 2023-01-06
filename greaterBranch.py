
def solution(arr):
    EMPTY_STRING = ""
    length = len(arr)
    if(length < 2):
        return EMPTY_STRING
    
    total_diff = 0
    i=1
    
    while pow(2,i)<length:
        total_diff += diffOfLevel(arr,i)
        i+=1
    
    if(total_diff < 0):
        return "Right"
    if(total_diff > 0):
        return "Left"
    return EMPTY_STRING
        
    

def diffOfLevel(arr, level=1): #left - right #minimum level = 1
    total_nodes = pow(2,level)
    index = total_nodes-1
    
    left_sum = 0
    right_sum = 0
    i=index
    
    while i<index+total_nodes/2 and i<len(arr):
        if arr[i] != -1:
            left_sum += arr[i]
        i+=1
    
    i=index+int(total_nodes/2)
    while i<index+total_nodes and i<len(arr):
        if arr[i] != -1:
            right_sum += arr[i]
        i+=1
    
    return left_sum - right_sum
               
    
    
        
        
    
    
