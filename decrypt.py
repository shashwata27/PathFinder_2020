from time import ctime

#rotate key=mins
#junk len=hours

def decrypt(stri):
    print(stri)
    decry=[]

    keyNjunk=ctime()[11:16]
    junk,key=map(int,keyNjunk.split(":"))
    key=key-(key%5)
    lst=[]
    for x in range(0,len(stri),4+junk):
        lst.append(stri[x:x+4])
    lst=[list(map(ord,(x.split("ob")))) for x in lst]

    for x in range(len(lst)):
        temp=tuple((y-key-x-32) for y in lst[x])
        decry.append(temp)

    print(decry)
    return decry


if __name__ == "__main__":
    decrypt("0ob1AqUphjiVEqTITTVRAauNBPi3ob4YLXkTAeYuWcQdWWtlLxVYgC")