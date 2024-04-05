










'''import json
import tkinter as tk
from tkinter import messagebox

# File paths
USER_DATA_FILE = 'user_data.json'
MOVIE_DATA_FILE = 'movie_data.json'

# Sample data structures
user_data = {}
movie_data = {}

# Load data from files on program start
def load_data():
    global user_data, movie_data
    try:
        with open(USER_DATA_FILE, 'r') as user_file:
            user_data = json.load(user_file)
    except FileNotFoundError:
        pass

    try:
        with open(MOVIE_DATA_FILE, 'r') as movie_file:
            movie_data = json.load(movie_file)
    except FileNotFoundError:
        pass

# Save data to files
def save_data():
    with open(USER_DATA_FILE, 'w') as user_file:
        json.dump(user_data, user_file, indent=2)

    with open(MOVIE_DATA_FILE, 'w') as movie_file:
        json.dump(movie_data, movie_file, indent=2)

# User authentication
def register_user(username, password):
    if username not in user_data:
        user_data[username] = {'password': password, 'role': 'regular'}
        save_data()
        messagebox.showinfo("Registration", f"User '{username}' registered successfully.")
    else:
        messagebox.showerror("Registration Error", f"User '{username}' already exists.")

# Movie management
def add_movie(title, release_year, genre, director, cast):
    movie_id = len(movie_data) + 1
    movie_data[movie_id] = {
        'title': title,
        'release_year': release_year,
        'genre': genre,
        'director': director,
        'cast': cast,
        'ratings': [],
        'reviews': []
    }
    save_data()
    messagebox.showinfo("Movie Added", f"Movie '{title}' added successfully.")

# Tkinter GUI
class MovieManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Movie Management System")

        # Create widgets
        self.label_username = tk.Label(master, text="Username:")
        self.entry_username = tk.Entry(master)
        self.label_password = tk.Label(master, text="Password:")
        self.entry_password = tk.Entry(master, show="*")
        self.button_register = tk.Button(master, text="Register", command=self.register_user)

        self.label_title = tk.Label(master, text="Title:")
        self.entry_title = tk.Entry(master)
        self.label_year = tk.Label(master, text="Release Year:")
        self.entry_year = tk.Entry(master)
        self.label_genre = tk.Label(master, text="Genre:")
        self.entry_genre = tk.Entry(master)
        self.label_director = tk.Label(master, text="Director:")
        self.entry_director = tk.Entry(master)
        self.label_cast = tk.Label(master, text="Cast:")
        self.entry_cast = tk.Entry(master)
        self.button_add_movie = tk.Button(master, text="Add Movie", command=self.add_movie)

        # Grid layout
        self.label_username.grid(row=0, column=0, padx=10, pady=5)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)
        self.label_password.grid(row=1, column=0, padx=10, pady=5)
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)
        self.button_register.grid(row=2, column=0, columnspan=2, pady=10)

        self.label_title.grid(row=3, column=0, padx=10, pady=5)
        self.entry_title.grid(row=3, column=1, padx=10, pady=5)
        self.label_year.grid(row=4, column=0, padx=10, pady=5)
        self.entry_year.grid(row=4, column=1, padx=10, pady=5)
        self.label_genre.grid(row=5, column=0, padx=10, pady=5)
        self.entry_genre.grid(row=5, column=1, padx=10, pady=5)
        self.label_director.grid(row=6, column=0, padx=10, pady=5)
        self.entry_director.grid(row=6, column=1, padx=10, pady=5)
        self.label_cast.grid(row=7, column=0, padx=10, pady=5)
        self.entry_cast.grid(row=7, column=1, padx=10, pady=5)
        self.button_add_movie.grid(row=8, column=0, columnspan=2, pady=10)

    def register_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        register_user(username, password)

    def add_movie(self):
        title = self.entry_title.get()
        release_year = self.entry_year.get()
        genre = self.entry_genre.get()
        director = self.entry_director.get()
        cast = self.entry_cast.get().split(',')
        add_movie(title, release_year, genre, director, cast)

if __name__ == "__main__":
    load_data()
    root = tk.Tk()
    app = MovieManagementApp(root)
    root.mainloop()
'''

'''import json
import tkinter as tk
from tkinter import messagebox

# File paths
USER_DATA_FILE = 'user_data.json'
MOVIE_DATA_FILE = 'movie_data.json'

# Sample data structures
user_data = {}
movie_data = {}

# Load data from files on program start
def load_data():
    global user_data, movie_data
    try:
        with open(USER_DATA_FILE, 'r') as user_file:
            user_data = json.load(user_file)
    except FileNotFoundError:
        pass

    try:
        with open(MOVIE_DATA_FILE, 'r') as movie_file:
            movie_data = json.load(movie_file)
    except FileNotFoundError:
        pass

# Save data to files
def save_data():
    with open(USER_DATA_FILE, 'w') as user_file:
        json.dump(user_data, user_file, indent=2)

    with open(MOVIE_DATA_FILE, 'w') as movie_file:
        json.dump(movie_data, movie_file, indent=2)

# User authentication
def register_user(username, password):
    if username not in user_data:
        user_data[username] = {'password': password, 'role': 'regular', 'watchlist': []}
        save_data()
        messagebox.showinfo("Registration", f"User '{username}' registered successfully.")
    else:
        messagebox.showerror("Registration Error", f"User '{username}' already exists.")

def login(username, password):
    if username in user_data and user_data[username]['password'] == password:
        messagebox.showinfo("Login", f"Welcome, {username}!")
        return True
    else:
        messagebox.showerror("Login Error", "Invalid username or password.")
        return False

# Movie management
def add_movie(title, release_year, genre, director, cast):
    movie_id = len(movie_data) + 1
    movie_data[movie_id] = {
        'title': title,
        'release_year': release_year,
        'genre': genre,
        'director': director,
        'cast': cast,
        'ratings': [],
        'reviews': []
    }
    save_data()
    messagebox.showinfo("Movie Added", f"Movie '{title}' added successfully.")

def search_movies(criteria, value):
    results = []
    for movie_id, movie_info in movie_data.items():
        if str(movie_info[criteria]).lower() == value.lower():
            results.append(f"{movie_info['title']} ({movie_info['release_year']})")
    return results

# Tkinter GUI
class MovieManagementApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Movie Management System")

        # Create widgets
        self.label_username = tk.Label(master, text="Username:")
        self.entry_username = tk.Entry(master)
        self.label_password = tk.Label(master, text="Password:")
        self.entry_password = tk.Entry(master, show="*")
        self.button_register = tk.Button(master, text="Register", command=self.register_user)
        self.button_login = tk.Button(master, text="Login", command=self.login_user)

        self.label_title = tk.Label(master, text="Title:")
        self.entry_title = tk.Entry(master)
        self.label_search_criteria = tk.Label(master, text="Search Criteria:")
        self.entry_search_criteria = tk.Entry(master)
        self.button_search = tk.Button(master, text="Search Movies", command=self.search_movies)

        # Grid layout
        self.label_username.grid(row=0, column=0, padx=10, pady=5)
        self.entry_username.grid(row=0, column=1, padx=10, pady=5)
        self.label_password.grid(row=1, column=0, padx=10, pady=5)
        self.entry_password.grid(row=1, column=1, padx=10, pady=5)
        self.button_register.grid(row=2, column=0, pady=10)
        self.button_login.grid(row=2, column=1, pady=10)

        self.label_title.grid(row=3, column=0, padx=10, pady=5)
        self.entry_title.grid(row=3, column=1, padx=10, pady=5)
        self.label_search_criteria.grid(row=4, column=0, padx=10, pady=5)
        self.entry_search_criteria.grid(row=4, column=1, padx=10, pady=5)
        self.button_search.grid(row=5, column=0, columnspan=2, pady=10)

    def register_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        register_user(username, password)

    def login_user(self):
        username = self.entry_username.get()
        password = self.entry_password.get()
        if login(username, password):
            # Additional functionalities for logged-in users can be added here
            pass

    def search_movies(self):
        criteria = self.entry_search_criteria.get()
        value = self.entry_title.get()
        results = search_movies(criteria, value)
        if results:
            messagebox.showinfo("Search Results", "\n".join(results))
        else:
            messagebox.showinfo("Search Results", "No movies found.")

if __name__ == "__main__":
    load_data()
    root = tk.Tk()
    app = MovieManagementApp(root)
    root.mainloop()'''


'''def calculate_cash(file_path, start_cash):
    # Initialize cash variables
    current_cash = start_cash

    # Read transactions from the file
    with open(file_path, 'r') as file:
        for line in file:
            invoice, amount, transaction_type = line.split()
            amount = float(amount)

            # Update cash based on transaction type
            if transaction_type == 'P':
                current_cash += amount
            elif transaction_type == 'R':
                current_cash -= amount

    return current_cash

if __name__ == "__main__":
    # Get user input
    start_cash = float(input("Enter the amount of cash at the beginning of the day: "))
    end_cash = float(input("Enter the expected amount of cash at the end of the day: "))
    file_path = input("Enter the name of the file with transactions: ")

    # Calculate actual amount of cash at the end of the day
    actual_end_cash = calculate_cash(file_path, start_cash)

    # Check if the actual amount matches the expected amount
    if actual_end_cash == end_cash:
        print("The actual amount of cash matches the expected amount.")
    else:
        print("The actual amount of cash does not match the expected amount.")'''

        
        
# Python program to illustrate 
# functions 
'''def hello(): 
	print("hello") 
	print("hello again") 
hello() 

# calling function 
hello()'''

# Python program to illustrate 
# function with main 
'''def getInteger(): 
	result = int(input("Enter integer: ")) 
	return result 

def Main(): 
	print("Started") 

	# calling the getInteger function and 
	# storing its returned value in the output variable 
	output = getInteger()	 
	print(output) 

# now we are required to tell Python 
# for 'Main' function existence 
if __name__=="__main__": 
	Main() 
'''

'''import keyword

# printing all keywords at once using "kwlist()"
print("The list of keywords is : ")
print(keyword.kwlist)
'''
'''print(False )
print(True )

print(True + True + True)
print(True + False + False)

print(None == 0)
print(None == [])'''

'''print(True or False)
print(False and True)
print(not True)
if 's' in 'geeksforgeeks':
	print("s is part of geeksforgeeks")
else:
	print("s is not part of geeksforgeeks")
for i in 'geeksforgeeks':
	print(i, end=" ")

print("\r")
print(' ' is ' ')
print({} is {})
'''

'''x=int(input("Enter value: "))
x=str(x)
for i in (x):
    print(i,end=" ")'''
    
'''for i in range(10):

	print(i, end=" ")
	if i == 6:
		break

print()
i = 0
while i < 10:
	if i == 6:
		i += 1
		continue
	else:
		print(i, end=" ")

	i += 1'''
 
'''# Lambda keyword
g = lambda x: x*x*x

print(g(7))
'''

'''a = 15
b = 10
def add():
	c = a + b
	print(c)
add()
def fun():
	var1 = 10

	def gun():
		nonlocal var1
		
		var1 = var1 + 10
		print(var1)

	gun()
fun()'''


'''import time

count_seconds = 3
for i in reversed(range(count_seconds + 1)):
	if i > 0:
		print(i, end='>>>')
		time.sleep(1)
	else:
		print('Start')'''

'''result=0  
for i in range(0,11):
    result+=i
print(result)'''

'''result=1  
for i in range(1,11):
    result*=i
print(result)'''

'''balance=1000
for i in range(1,4):
    balance=balance+(balance*(5/100))
    print(balance)'''
    
'''def print_name_in_box(name):
    border_length = len(name) + 4
    print("+" + "-" * (border_length - 2) + "+")
    print("| " + name + " |")
    print("+" + "-" * (border_length - 2) + "+")
print_name_in_box("Dave")'''

'''def print_large_letters(name):
    patterns = {
        'D': ["**** ", "*   *", "*   *", "*   *", "**** "],
        'A': ["  *  ", " * * ", "*****", "*   *", "*   *"],
        'V': ["*   *", "*   *", " * * ", " * * ", "  *  "],
        'E': ["*****", "*    ", "**** ", "*    ", "*****"]
    }

    for i in range(5):
        line = ""
        for char in name:
            if char in patterns:
                line += patterns[char][i] + "  "
            else:
                line += "     "  # Space for unknown characters
        print(line)

# Print the name "DAVE" in large letters
print_large_letters("DAVE")'''

'''def print_face():
    # Top of the head
    print("  /////  ")
    # Forehead
    print(" +\"\"\"\"\"+ ")
    # Eyes
    print("(| 0 0 |)")
    # Nose
    print(" |  ^  | ")
    # Mouth
    print(" | '-' | ")
    # Bottom of the head
    print(" +-----+ ")

print_face()'''

'''def calculate_repair_cost(n):
    cost_in_year_1 = 100
    cost_in_year_10 = 1500
    yearly_increase = (cost_in_year_10 - cost_in_year_1) / (10 - 1)

    if n == 1:
        return cost_in_year_1
    else:
        cost_in_year_n = cost_in_year_1 + (n - 1) * yearly_increase
        return cost_in_year_n

repair_cost_year_3 = calculate_repair_cost(3)
print(repair_cost_year_3)'''

import math

'''def calculate_bottle_volume(r1, h1, r2, h2, h3):
    volume_cylinder1 = math.pi * r1**2 * h1
    volume_cylinder2 = math.pi * r2**2 * h2
    volume_cone = (1/3) * math.pi * h3 * (r1**2 + r1*r2 + r2**2)
    total_volume = volume_cylinder1 + volume_cylinder2 + volume_cone   
    return total_volume

r1 = 2 
h1 = 4
r2 = 1.5
h2 = 3
h3 = 2 

volume = calculate_bottle_volume(r1, h1, r2, h2, h3)
print(volume)'''


'''name="Harry"
print(f"{name[0]} {name[len(name)-1]} {name[len(name)//2]}")   '''

'''name=input("Enter Your Name: ")
print(f"{name[0]} {name[len(name)-1]} {name[len(name)//2]}") '''

'''x='12345'
for i in range(len(x)+1):
    print(i,end=" ")'''
    
'''x='Mississippi'
print(f"{x[0:3]}...{x[-3::]}") '''   

#page 200
'''print(" Su M  T  W  Th F Sa")
def print_pattern(max_num):
    num = 1
    while num <= max_num:
        for i in range(7):
            if num > max_num:
                break
            print(f"{num:2}", end=" ")
            num += 1
        print()

print_pattern(31)'''
'''
print("Celsius | Fahrenheit")
print("--------+-----------")
x=0
y=(" ")*(7-(len(str(x))))
for i in range(11):
    print(f"{x}{y}|   {(x*9//5)+32}")
    x+=10
    '''
    
'''s = 0
for i in range(1, 10) :
    s = s + i    
print(s) 

s=0
i=0
while i<10:
    s+=i
    i+=1
print(s)  '''


    
 


    
                 
    