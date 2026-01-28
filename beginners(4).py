#if condition
height =float(input("Enter height in meters"))
weight=float(input("Enter weight in kilograms"))
BMI=weight/(height ** 2)
print("BMI is",BMI)
if BMI >=30:
    print("Obesity")
elif BMI >=25:
    print("Overweight")
elif BMI >=18.5:
     print("Normal")
else:
    print("Underweight")  


#if the input is like as below:
# Enter height in meters:1.75
# Enter weight in kilograms:70
# Output:"Normal" 

Australia=["Sydney","Melbourne","Brisbane","Perth"]
UAE = ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"] 
India = ["Mumbai", "Bangalore", "Chennai", "Delhi"] 
city=input("Enter the city name")
if city in Australia:
    print("City in Australia")
elif city in UAE:
    print("City in UAE")
elif city in India:
    print("City in India")
else:
    print("No city found")        

#Enter a city name: "Abu Dhabi" 
#Output: "Abu Dhabi is in UAE"    


first_city=input("Enter the first city name")
second_city=input("Enter the second city name")
if first_city in India and second_city in India:
    print("Both cities in India")
elif first_city in Australia and second_city in Australia:
    print("Both the cities are in Australia")
elif first_city in UAE and second_city in UAE:
    print("Both cities are in UAE")
else:
    print("doesnot belong to same country")   

#Enter the second city: "Chennai" 
#Output: "Both cities are in India"          

