from time import ctime
import random
import string

#rotate key=mins
#junk len=hours
#junk only after finish of tuple
#"," =obify
def encry(l):
    print(l)
    encry=""
    keyNjunk=ctime()[11:16]
    junk,key=map(int,keyNjunk.split(":"))
    key=key-(key%5)

    for x in range(len(l)):
        first=chr(l[x][0]+key+x+32)#after char b/w 32 and 254 are readable
        second=chr(l[x][1]+key+x+32)

        junkdata=""
        for _ in range(junk):
            junkdata+=str(random.choices(string.ascii_letters))[2]

        term=first+"ob"+second
        encry+=term+junkdata
        # print(term)
        # print(junkdata)
        
    print(encry)
    return encry

if __name__ == "__main__":    
    encry([(1,2),(3,4)])