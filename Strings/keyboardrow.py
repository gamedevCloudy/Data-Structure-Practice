
def findLetter(word, row):
    print("\tCurrent: ",word)
    for i in word:
        if i not in row: 
            return False
    return True

def findWords(words):
    x= " ".join(words).lower().split()
    print("Words are: ", words,"\t",x)

    r1="qwertyuiop"
    r2="asdfghjkl"
    r3="zxcvbnm"
    r=[]

    for i in range(0,len(x)): 
        print(i)
        if findLetter(x[i],r1): 

            r.append(words[i])
        elif findLetter(x[i],r2): 
            r.append(words[i])
        elif findLetter(x[i],r3): 
            r.append(words[i])


    return r

print("\nResult: ","\t",findWords(["adsdf","sfd"]))
