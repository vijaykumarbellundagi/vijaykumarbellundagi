# List => It works like array Used to Store the multiple values
# 1. hetrogenous type of data
# 2. it will stroe your data in continious memory allocation
# 3. it will also have random access possible -> indices
# 4. Lists are mutable

# marks=[25,35,45,12,90]

# print(type(marks))

# profile=["Vijay",10000,True,24.2]
# print(type(profile))
# print(profile)
# print(profile[0]) 

# profile[1]=15000
# print(profile)

# List Slicing

# age=[15,21,22,50,11]
# print(age[:3])

# list=[4,1,2,6]

# list.append(5)
# print(list)

# list.sort()
# print(list)

# list.sort(reverse=True)
# print(list)

# list.reverse()
# print(list)

# list.insert(1,8)
# print(list)

# list.remove(2)
# print(list)

a=[3,7,8,1,1,3]
count=0
for a in a:
    if a%2!=0:
        count=count+1

print(count)

