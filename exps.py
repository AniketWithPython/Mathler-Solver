#code used to generate possible expressions (exps.txt)

from itertools import product
CHARS=list("+-*/0123456789")
f=open("./exps.txt",'w')

badops=["++","--","**","//","+-","-+","*+","*-","/+","/-",]

def badexps(x:str):
    global badops
    if x[0] in "+-*/0" or x[-1] in "+-*/" :
        return True
    for i in badops:
        if i in x:
            return True
    try:
        int(x)
        return True
    except:
        pass

for i in product(CHARS,repeat=6):
    exp=''.join(i)
    try:
        eval(exp)
        if badexps(exp)==True:
            continue
        f.write(exp+"\n")
    except:
        pass
    
f.close()
print("done")


