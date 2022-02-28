
def countN(n):
    result = 0
    
    for i in range(n+1):
        result += str(i).count('1')
        
    return result

print(countN(1000))
        
