def pascalTri(ar, rw, st):
    if(rw>0):
        y = []
        for i in range(0,len(ar)): 
            if(i==0): 
                y.append(1)
            elif(len(ar)>=2): y.append(ar[i]+ar[i-1])
        y.append(1)
        print("\n",y)
        st.append(y)
        pascalTri(y,rw-1, st)

st= []
pascalTri([1],5, st)
print("\n\n\n\n", st)
