def getSum(a: int, b: int) -> int:
    
    while b!=0:
        carry = (~a) & b
        a = a^b
        b = carry<<1
    return a
    
    
    

def bin(n) :
     
    i = 1 << 31
    while(i > 0) :
     
        if((n & i) != 0) :
         
            print("1", end = "")
         
        else :
            print("0", end = "")
             
        i = i // 2
            
print(getSum(5,2))
# print(getSum(-1,2))

