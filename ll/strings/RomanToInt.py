s = 'XL'
def StrToArr(string):
    values = []
    for i in string: 
        values.append(i)
    return (values)


def RomanToInt(values): 
    num = 0
    if('V' in values): 
        num+=5
        vLoc = values.index('V')
        # print(vLoc)

        if(vLoc+1<len(values) and values[vLoc+1] == 'I' ): num+=1
        if( vLoc+2<len(values) and values[vLoc+2] == 'I' ): num+=1
        if( vLoc+3<len(values) and values[vLoc+3] == 'I'): num+=1
            
        if(values[vLoc-1] == 'I'):
            for i in (vLoc,0):
                if(values[i]) == 'I': num-=1
        
    if('X' in values): 
        xLoc = values.index('X')
        if(values[xLoc+1] != 'L'):
            num+=10
            if(values[xLoc-1] == 'I'): num-=1
    
    if('L' in values): 
        lLoc = values.index('L')
        if(values[lLoc+1]<len(values) and values[lLoc+1]!= 'C'): 
            num+=50
            if(values[lLoc-1] == 'X'): num-=10
        
    if('C' in values): 
        num+=100
    
    if('D' in values): 
        num+=500
    
    if('M' in values): 
        num += 1000
    

    print(num)
    
values = StrToArr(s)
print(values)
print(type(values[0]))

RomanToInt(values)