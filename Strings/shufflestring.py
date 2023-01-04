indices = [4,5,6,7,0,2,1,3]
s = "codeleet"

#desired output: shuffeled string

def restoreString(s,indices): 
    t = [] 
    for i in range(len(indices)): #n
        x=[]
        x.append(indices[i])
        x.append(s[i])
        t.append(x)
    print(t)
    t.sort() #nlogn
    print(t)

    output= ""
    for i in t: #n
        output+=i[1]

    print(output)
    return output


restoreString(s,indices)
