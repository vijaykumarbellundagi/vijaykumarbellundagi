weight = float(input("Enter your weight in kilograms : "))
height = float(input("Enter your height in m : "))

bmi=weight/(height*height)

if(bmi<18.5):
    print("Underweight")
elif(bmi>=18.5 and bmi<25):
    print("Normal")
else:
    print("OverWeight")


