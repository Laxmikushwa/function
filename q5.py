def num():
    list = [8, 6, 4, 8, 4, 50, 2, 7]
    index=0
    min=list[0]
    while index<len(list):
        if list[index] <min:
            min=list[index]
        index=index+1
    print(min)
num()