#algorithm responsible for interpreting the hints

def sasta_ai(data:dict):
    c=[]
    vals=[i[1] for i in data.values()]
    for index,j in data.items():
        val=j[1]
        
        if j[0]=="slate":
            test=False
            for k in data.values():
                if k[1]==val and k[0]!="slate":
                    test=True
                    break
            if test==False:
                c.append(f"x.count('{val}')==0")
        if j[0]=="slate":
            c.append(f"x[{index}]!='{val}'")
        elif j[0]=="yellow":
            c.append(f"x[{index}]!='{val}'")
            count=0
            for k in data.values():
                if j[1]==k[1] and k[0]!="slate":
                    count+=1
            c.append(f"x.count('{val}')=={count}")
        elif j[0]=="green":
            c.append(f"x[{index}]=='{val}'")
        
    return ' and '+' and '.join(c)

if __name__=="__main__":
    #test
    print(sasta_ai({0:["yellow","1"],1:["slate","2"],2:["slate","+"],3:["slate","4"],4:["green","3"],5:["green","2"]}))

