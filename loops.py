# loops -> while,  for

# count=5
# while(count>0):
#     print("hello")
#     count=count-1

# element=[1,2,8,6,4]
# count=len(element)-1
# key=8
# flag=0
# # count=element.__len__()
# while(count>0):
#     if(element[count]==key):
#         print("Key :",count)
#         flag=flag+1

#     count=count-1
        
# if(flag==0):
#     print("not found the element")


# print(element.index(8))

# for loops--------------------------------------
# Traversing


# list=[1,6,3,9,2]

# # for(i=0;i<arr.length.i++){arr[i]}

# for el in list:
#     print(el,end=" ")
#     # print(el)
# else:
#     print("end of list")


# list=[1,4,9,16,25]
# el=9
# flag=0
# for i in list:
#     if i==el:
#         print("Present")
#         flag=flag+1
#         break
# else:
#     if(flag==0):
#         print("Not Present")

# for -> range
# range(start?,stop,step?)


# for el in range(5):
#     print("Jai Shree Ram")

# for el in range(2,5):
#     print(el)

# for el in range(1,20,2):
#     print(el,end=" ")

num=5
fact=1
for i in range(1,num+1):
    fact=fact*i
print(fact)


