s = " practice   makes   perfect"
def rearrageSpaces(): 
    t= []
    for i in range(len(s)):
        if not 95<ord(s[i])<123: t.append(s[i])
    s =s.split()
    spacesToAdd = len(t)//len(s)
    x= len(t)-2
    for i in range(len(s)):
        if i%2 !=0: s.insert(i,"  ")

    print(s)
    print(len(t))
    print(spacesToAdd)


def rearSpace(s):
    spaces=[]

    for i in range(len(s)):
        if not 95<ord(s[i])<123: spaces.append(s[i])
    s=s.split() 

    spacesToAdd = len(spaces)
    inBetn = spacesToAdd//(len(s)-1)
    rest = spacesToAdd%(len(s)-1)

    op=''

    for i in range(len(s)-1):
        op+=s[i]
        op+=" "*inBetn
    op+=s[len(s)-1]
    op+=(" "*rest)
    print(op)

def rearSpace2(s):

    spacesToAdd = 0
    for i in range(len(s)):
        if not 95<ord(s[i])<123: spacesToAdd+=1
    s=s.split() 

    inBetn = spacesToAdd//(len(s)-1)
    rest = spacesToAdd%(len(s)-1)

    op=''

    for i in range(len(s)-1):
        op+=s[i]
        op+=" "*inBetn
    op+=s[len(s)-1]
    op+=(" "*rest)
    print(op)

rearSpace2(s)


def reSpace(text): 
    text = text.split()
    spaceCount = text.count(' ')
    n = len(text)
    if n==1: 
        return text[0]+ " "*spaceCount

    inBetn= " "*(spaceCount//(n-1))

    return inBetn.join(text)+" "*(spaceCount%(n-1))


print(reSpace(" hello"))

