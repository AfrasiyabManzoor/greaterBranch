
def solution(arr):
    EMPTY_STRING = ""
    length = len(arr)
    if(length < 2):
        return EMPTY_STRING
    
    totalDiff = 0
    i=1
    
    while pow(2,i)<length:
        totalDiff += diffOfLevel(arr,i)
        i+=1
    
    if(totalDiff < 0):
        return "Right"
    if(totalDiff > 0):
        return "Left"
    return EMPTY_STRING
        
    

def diffOfLevel(arr, level=1): #left - right #minimum level = 1
    totalNodes = pow(2,level)
    index = totalNodes-1
    
    leftSum = 0
    rightSum = 0
    i=index
    
    while i<index+totalNodes/2 and i<len(arr):
        if arr[i] != -1:
            leftSum += arr[i]
        i+=1
    
    i=index+int(totalNodes/2)
    while i<index+totalNodes and i<len(arr):
        if arr[i] != -1:
            rightSum += arr[i]
        i+=1
    
    return leftSum - rightSum
               
    
    
        
        
    
    
