# sets -> is the collection of unordered items
# sets -> each and every element in the set must be unique and immuatble
# sets -> they don't have any properties of indices -> random access

# num1={1,2,3,4,5}
# num2={1,2,2,3,4,3}

# print(type(num1))

# print(num1)
# print(num2)

# val={1,"vijay"}
# print(type(val))

# num2.add(8)
# print(num2)
# num2.remove(4)
# num2.clear()
# print(num2)

# num1={1,2,3,4,5}
# num2={1,2,2,3,4,3,9}

# print(num2.union(num1))

# print(num2.intersection(num1))



def create_dictionary():

    user_dict = {}
    
    num_items = int(input("Enter the number of items you want to add to the dictionary: "))
  
    for _ in range(num_items):
        key = input("Enter the key: ")
        value = input("Enter the value: ")
        user_dict[key] = value
    
    return user_dict

user_dictionary = create_dictionary()

print("The dictionary you created is:")
print(user_dictionary)

