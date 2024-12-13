#Defining a menu

menu = {
    'Pizza':40,
    'Pasta':50,
    'Burger':70,
    'Salad':10,
    'Coffee':5
}

#Greet
print("Welcome to our Restaurant")
print("Here id our menu : \n\nPizza : RS 40\nPasta : RS 50\nBurger :70\nSalad :10\nCoffee :5")

order_total=0

item_1=input("Enter the name of item you want to ordeer : ")

if item_1 in menu:
    order_total = order_total + menu[item_1]
    print(f"Your item {item_1} has be added to your order ! ")
else:
    print(f"Ordered item {item_1} is not available yet ! ")

while(True):
    another_order=input("Do you want to order another item ? (yes/no) : ")

    if(another_order=="yes"):
        item_2=input("Enter the name of item you want to order : ")

        if item_2 in menu:
            order_total=order_total+menu[item_2]
            print(f"Item {item_2} has been added to your order ! ")
        else:
            print(f"Ordered item {item_2} is not available yet ! ")

    elif(another_order=="no"):
        print("Thank You For Ordering ! ! ! ")
        break        

print(f"The total amount for items to pay is : {order_total}")

