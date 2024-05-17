user_list=[]
total=0
while True:
    user_input=input("Enter a number or done to stop: ")
    if user_input.lower()=="done":
        break
    number=float(user_input)
    user_list.append(number)
    total+=number
if user_list:
    count=len(user_list)
    print(f"Sum= {total}")
    average=total/count
    print(f"Average= {average:.2f}")
    
    maximum=user_list[0]    
    minimum=user_list[0]
    for num in user_list[1:]:
        if num>maximum:
            maximum=num
        if num<minimum:
            minimum=num
    print(f"Maximum= {maximum}")  
    print(f"Minimum= {minimum}")
    
else:
    print("List has no input") 