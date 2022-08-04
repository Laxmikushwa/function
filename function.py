# Write a Python function to find the Max of three numbers.
# def fun(a):
#     m=0
#     if a>m:
#         m=a
#     return m

# list1=[7,5,8]
# i=0
# for i in list1:
    
#     b= fun(i)
# print(b)  

# Write a Python function to sum all the numbers in a list. 
# Sample List : (8, 2, 3, 0, 7)
# def fun(a):
#     global c
#     c+=a
#     return c 


# list1=[8, 2, 3, 0, 7,5,4,3,2,1]
# c=0
# for i in list1:
#     b= fun(i)
# print(b)


# Write a Python function to multiply all the numbers in a list. Go to the editor
# Sample List : (8, 2, 3, -1, 7)


# def fun(a):
#     global c
#     c*=a
#     return c
# list=[8,2,3,-1,7]
# c=1
# for i in list:
#     b=fun(i)
# print(b)

# Write a Python program to reverse a string. 
# Sample String : "1234abcd"
# Expected Output : "dcba4321"




# def fun(a):
#     global str2
#     str2+=a
#     return str2
# str1="1234abcd"
# str2=" "
# b=len(str1)
# i=-1
# while i>=-b:
#     a=fun(str1[i])
#     i-=1
# print(a)


# def fun(a):
#     global str2
#     str2+=a
#     return str2
# str1="1234abcd"
# str2=""
# b=len(str1)
# i=-1
# while i>=-b:
#     a=fun(str1[i])
#     i-=1
# print(a)

# a=AA,BB,CC,DD,BB
# O/P=["A","B","C","D","B"]

# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.

# def fun( ):
#     n=int(input("enter the number="))
#     i=1
#     while n>0:
#         i=i*n
#         n=n-1
#     print(i)
# fun( )

# Write a Python function to check whether a number falls in a given range.

# def range(n):
#     if n in range(3,9):
#         print( " %s is in the range"%str(n))
#     else :
#         print("The number is outside the given range.")
# range(4)

# def test_range(n):
#     s = int(input ("enter the starting point:-"))
#     e = int(input ("enter the ending point:-"))
#     if n >= s or n <= e :
#         return "number in the range "
#     else:
#         return "number not in given range "
# print(test_range(int(input("enter the number  :- "))))

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. Go to the editor
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12

# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("No. of Upper case characters : ", d["UPPER_CASE"])
#     print ("No. of Lower case Characters : ", d["LOWER_CASE"])

# string_test('The quick Brown Fox')

# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters. 
# Sample String : 'The quick Brow Fox'
# Expected Output :
# No. of Upper case characters : 3
# No. of Lower case Characters : 12


# def fun(str1):
#     a=0
#     b=0
#     for i in str1:
#         if i.isupper()==True: 
#             a+=1
#         if i.islower()==True:
#             b+=1
#         else:
#             continue
#     print("No. of Upper case characters :",a)
#     print("No. of Lower case Characters :",b)
    
# (fun (input(" enter any sentence= ")))


#  Write a Python function that takes a list and returns a new list with unique elements of the first list. 
# Sample List : [1,2,3,3,3,3,4,5]
# Unique List : [1, 2, 3, 4, 5]

# def fun():
#     list1=[1,2,3,3,3,3,4,5]
#     list2=[]
#     for i in list1:
#         if i not in list2:

#             list2.append(i)
#     return list2
    
# print(fun())

# Write a Python function that takes a number as a parameter and check the number is prime or not. Go to the editor
# Note : A prime number (or a prime) is a natural number greater than 1 and that has no positive divisors other than 1 and itself.

# def fun(c):
#     count=0
#     i=1
#     while i<=c:
#         if c%i==0 :
#            count+=1
#         i+=1
#     if count==2:
#         return "prime number" 
#     else:
#         return "not prime number"
# print(fun(int(input("enter the number="))))

# Write a Python program to print the even numbers from a given list. Go to the editor
# Sample List : [1, 2, 3, 4, 5, 6, 7, 8, 9]
# Expected Result : [2, 4, 6, 8]
# def fun(c):
#     list1=[]
#     for i in c:
#         if i%2==0:
#             list1.append(i)
#     return list1
# lis=[1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(fun(lis))
    
#  Write a Python function to check whether a number is perfect or not.
# def fun():
#     p=int(input("enter number here___: "))
#     sum=0
#     for i in range(1,p):
#         if p%i==0:
#             sum+=i
#     if sum==p:
#         print(f"{p} is perfect number")
#     else:
#         print(f"{p} is not perfect number ")
# fun( )

# Write a Python function that checks whether a passed string is palindrome or not. Go to the editor
# Note: A palindrome is a word, phrase, or sequence that reads the same backward as forward, e.g., madam or nurses run.

# def fun():
#     str1=input("enter any word=")
#     str2=""
#     i=-1
#     while i>=-len(str1):
#         str2+=(str1[i])
#         i-=1
#     if str1==str2:
#         return "palindrome"
#     else:
#         return "not palindrome"
# print(fun())

# Write a Python function that prints out the first n rows of Pascal's triangle. Go to the editor
# Note : Pascal's triangle is an arithmetic and geometric figure first imagined by Blaise Pascal.

# Sample Pascal's triangle :

# Pascal's triangle
# Each number is the two numbers above it added together 

# def lis(list1):
#     # count=0
#     l=[]
#     for i in list1:
#         if len(i) == 4:
#             l.append(i)
#     return l
# l1=["chhotu","niraj","saurabh","sonu","tinku"]
# print (lis(l1))

# n=int(input("Enter an integer :- "))
# a=n
# prime_count = 0
# sum=0
# i=1
# while True:
#         count=0
#         for j in range(1,i+1):
#             if i%j==0:
#                     count+=1
#         if count==2 :
#             prime_count+=1
#             sum+=i 
#         if prime_count==a:
#             break 
#         i+=1
# print(sum)

a=5
b=6
c=7
a=d=5
c=a=7
b=c=6
d=b=5
print("\n",b,"\n",c,"\n",a,)