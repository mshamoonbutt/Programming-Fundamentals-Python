#Ques No 1

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


#Ques No 2


def remove_elements_at_odd_indexes(input_list):
    return [input_list[i] for i in range(len(input_list)) if i % 2 == 0]

animal_list = ["Cat", "Dog", "Cow", "Bird", "Sparrow"]

result_list = remove_elements_at_odd_indexes(animal_list)

print(result_list)

        

#Ques No 3


def remove_duplicates(input_list):
    result_list = []
    for num in input_list:
        if num not in result_list:
            result_list.append(num)
    return result_list

input_list = [1, 2, 1, 3, 2, 3, 4]

result_list = remove_duplicates(input_list)

print(result_list)


#Ques No 4



def are_lists_equal(list1, list2):

    for i in range(len(list1)):
        if int(list1[i]) != int(list2[i]):
            return False

    return True

L1 = [1, 2, 3, 4.4]
L2 = [1, 2, 3, 4]

if are_lists_equal(L1, L2):
    print("Sample Output 1: Equal")
else:
    print("Sample Output 1: Not equal")

L1 = [1, 2, 3, 4, 4]
L2 = [1, 2, 4, 3, 4]

if are_lists_equal(L1, L2):
    print("Sample Output 2: Equal")
else:
    print("Sample Output 2: Not equal")




#Ques No 5


def shift_right(list, num):
    n = len(list)
    num = num % n

    return list[-num:] + list[:-num]

num = int(input("Enter the number of positions to shift: "))
my_list = [1, 5, 2, 6, 7]

result = shift_right(my_list, num)

print("Sample Output:", result)




