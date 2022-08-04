def num():
    num= ["Z", "A", "A", "B", "E", "M", "A", "R", "D"]
    i=1
    c=[]
    while i<=len(num):
        c.append(num[-i])
        i+=1
    print(c)
num()