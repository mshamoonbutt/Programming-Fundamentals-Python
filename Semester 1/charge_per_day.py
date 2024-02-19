def charge(days):
    if days<=5:
        return 2
    elif days>=6 and days<=10:
        return 3
    elif days>=11 and days<=15:
        return 4
    elif days>15:
        return 5
    else:
        print("Invalid Input")
days=int(input("Enter number of days: "))  
sum=charge(days)*days    
print(f"Total charges till {days} days are Rs {sum} as Rs {charge(days)} per day")        
  
charge(days)