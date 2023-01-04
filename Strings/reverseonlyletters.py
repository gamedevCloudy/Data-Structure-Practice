def reverseOnlyLetters(s): 
    re= []
    for i in s:
        x =ord(i)
        if 64<x<91 or 96<x<122:
            re.append(i)
    print(re)
    re=re[::-1]

    ct = 0
    op=""
    for i in range(len(s)): 
        x=ord(s[i])
        if 64<x<91 or 96<x<122:
            op+=re[ct]
            ct+=1
        else: op+=s[i]
    
    print(op)

def re2(s): 
    opr=[""]*len(s)
    backLtr=len(s)-1
    for i in range(len(s)): 
        x=ord(s[i])
        if not (64<x<91 or 96<x<123):
            opr[i]=s[i]
    for i in range(len(s)): 
        x=ord(s[i])
        if (64<x<91) or (96<x<123): 
            while(opr[backLtr]!=""):
                backLtr-=1
            opr[backLtr]=s[i]
            backLtr-=1
    print(opr)


def re3(s):
    opr=[""]*len(s)
    backLtr=len(s)-1
    for i in range(len(s)): 
        x=ord(s[i])
        if not (64<x<91 or 96<x<123):
            opr[i]=s[i]
        if (64<x<91) or (96<x<123): 
            while(opr[backLtr]!=""):
                backLtr-=1
            opr[backLtr]=s[i]
            backLtr-=1
            

    print(opr)






s = "Test1ng-Leet=code-Q!"
# s = "z<*zj"
re2(s)
