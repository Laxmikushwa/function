# def num():
#     num = [6, 8, 4, 3, 9, 56, 0, 34, 7, 15]
#     i=0
#     c=[]
#     while i<len(num):
#         c.append(num[i])
#         i+=1
#     print(sorted(c))
# num()
        
# 
n=int(input("enter the ...."))
max=0
i=0
while i<=10:
    if (n[i]>max):
        max=n[i]
    i+=1
    j=0
    min=n[0]
    while j<len(n):
        if n[j]<min:
            min=n[i]
        j+=1
print(max)
print(min)