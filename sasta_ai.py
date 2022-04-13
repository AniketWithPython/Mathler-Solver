#algorithm responsible for interpreting the hints

def sasta_ai(data:dict):
    c=[]
    vals=[i[1] for i in data.values()]
    for i,j in data.items():
        index=i
        val=j[1]
        counts=vals.count(val)
        if j[0]=="slate" and counts==1:
            c.append(f"x.count('{val}')==0")
        elif j[0]=="slate":
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
        
    return ' and '.join(c)

if __name__=="__main__":
    #test
    print(sasta_ai({0:["yellow","1"],1:["slate","2"],2:["slate","+"],3:["slate","4"],4:["green","3"],5:["green","2"]}))

