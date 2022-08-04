def max():
    list=[3,2,5,7,9,1,6]
    index=0  
    max=0
    while index<len(list):
        if list[index] >max:
            max=list[index]
        index=index+1
    print(max)
max()    

