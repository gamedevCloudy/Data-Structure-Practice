def romanToInt(s):
    num=0

    for i in range(0,len(s)):

        #for 1:8
        if 'V' in s:
            if(s[i]=='V'):
                if s[i-1]=='I': 
                    num+=4
                    print("Step: ", num)
                else: 
                    num+=5
                    print("Step: ", num)
                    for j in range(i+1,len(s)): 
                        num+=1
                        print("Step: ", num)
                    
                    return num
        elif s[i]=='I':
            if s[i+1] !='X':
                for j in range(i,len(s)):
                    num+=1
                    print("Step: ",i, num)
                return num
        
        #for 9or10
        if s[i]=='X':
            #next isn't 100 or 50
            if s[i+1]!='C' and s[i+1]!='L': 
                if s[i-1]=='I' and i-1 >=0: 
                    num+=9
                    print("Step: ", num)
                else: 
                    num+=10
        
        #for 40or50
        if s[i]=='L':
           
            if s[i-1]=='X' and i-1 >=0: 
                num+=40
                print("Step: ", num)
            else: 
                num+=50
                print("Step: ", num)
        
        #for 90or100
        if s[i]=='C':
        
            if s[i+1]!='D' and s[i+1]!='M': 
    
                if s[i-1]=='X' and (i-1) >= 0: 
                    num+=90
                    print("Step: ", num)
                    
                else: 
                    num+=100
                    print("Step: ", num)

        #for 400or500
        if s[i]=='D':

            if s[i-1]=='C' and i-1 >=0: 
                num+=400
                print("Step: ", num)
            else: 
                num+=500
                print("Step: ", num)

        #for 1000
        if s[i]=='M':
        
            if s[i-1]=='C' and (i-1) >=0: 
                num+=900
                print("Step: ", num)
            else: 
                num+=1000
            
             

    return num


x = romanToInt("IX")
print(x)

