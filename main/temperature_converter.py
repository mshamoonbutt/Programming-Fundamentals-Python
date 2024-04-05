def convert_temperature(temp, scale) :
    if scale=='F':
        print("Fahrenheit to Celsius")
        print((temp*9/5)+32)
    elif scale=='C':    
        print("Celsius to Fahrenheit") 
        print((temp-32)*5/9)
    else:
        print("invalid")
temp=eval(input("Enter your value of temperature: "))
scale=(input("F or C: "))
convert_temperature(temp, scale)