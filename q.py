# def add():
#     x=10
#     y=20
#     c=x+y
#     print(c)
# add()

# def add(y):
#     x=10
#     c=x+y
#     print(c)
# add(20)


# def max():
#     a=10
#     b=20
#     c=30
#     if a>b and a>c:
#         print(a,"is max number")
#     elif b>a and b>c:
#         print(b,"is max number")
#     elif c>a and c>b:
#         print(c,"is max number")
#     else:
#         print("nothing is max number")
# max()



# def add():
#     x=10
#     y=20
#     c=x+y
#     return (c)
# a=add()
# print (a)
# def sub():
#     d=a-20
#     return d
# print (sub())


# def add():
#     x=10
#     y=20
#     c=x+y
#     return (c)
# a=add()
# print (a)
# def sub(c):
#     d=c-20
#     return d
# print (sub(a))


# def (function ko define kiya)  add (function name)():(starting function)
    # x=10(local variable)
    # y=20 (local variable)
    # c=x+y(statements)
    # return (c)statements
# a=add()(calling a function)
# print (a)print function
# def sub(c):
#     d=c-20
#     return d
# print (sub(a))

# for i in range (4):
#     for j in range (4):
#         if i ==j:
#             print ("1",end=" ")
#         else:
#             print("0",end=" ") 
#     print()

i=1
while i<=3:
    j=1
    while j<=3:
        if i==j:
            print("1",end=" ")
        else:
            print("0",end=" ")
        j+=1
    print()
    i+=1