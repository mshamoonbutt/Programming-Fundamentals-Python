'''movies = []
START = "\n=========== Movie Management System ===========\n\n\nEnter 1 to Add Movies, \nEnter 2 to Display Movies \nEnter 3 to Search a Movie by Title \nEnter 4 to Quit Application \n"


def add_movie():
    title = input("Enter title of the film: ")
    director = input("Enter director of the film: ")
    year = input("Enter year of the film: ")
    genre = input("Enter genre of the film: ")
    movies.append({
        'title': title,
        'year': year,
        'director': director,
        'genre': genre
    })


def list_movies():
    quantity = len(movies)
    titles = [movie['title'] for movie in movies]
    titles = '\n'.join(titles)

    if quantity:
        print(f'\nList of movies that have in your collection: \n{titles}. \nIn total you have {quantity} {"movie" if quantity == 1 else "movies"}.')
    else:
        print('There are no movies in your collection.')


def print_movie_info(movie):
    print('Here is information about requested title')
    print(f'Title: {movie["title"]},')
    print(f'Director: {movie["director"]},')
    print(f'Year: {movie["year"]},')
    print(f'Genre: {movie["genre"]}.')


def find_title():
    search_title = input('Enter title you are looking for: ')
    for movie in movies:
        if movie['title'] == search_title:
            print_movie_info(movie)
        else:
            print('Requested title was not found in the collection.')


user_selection = {
    '1': add_movie,
    '2': list_movies,
    '3': find_title
}


def menu():
    selection = input(START)
    while selection != '4':
        if selection in user_selection:
            selected_action = user_selection[selection]
            selected_action()
        else:
            print("Unknown command. Please choose within available options: 1, 2, 3 or 4 to close the app.")
        selection = input(START)
    print('Thank you for using the app. See you next time!')


if __name__ == '__main__':
    menu()
'''

'''import re  # Import regular expression module
import random  # Import the random module for generating recovery codes

class UserAuthenticationSystem:
    def __init__(self):
        self.users = {}  # Dictionary to store user data
        self.recovery_emails = {}  # Dictionary to store recovery emails

    def is_strong_password(self, password):
        # Check if the password is strong
        return (
            len(password) >= 8 and
            any(char.isupper() for char in password) and
            any(char.islower() for char in password) and
            any(char.isdigit() for char in password) and
            any(char in "!@#$%^&*()-_+=<>{}[]|;:,." for char in password)
        )

    def register(self, username, password, recovery_email):
        # Check if the username is already taken
        if username in self.users:
            print("Username already taken. Please choose a different one.")
        else:
            # Check if the password is strong
            if self.is_strong_password(password):
                # Register the user
                self.users[username] = password
                self.recovery_emails[username] = recovery_email
                print("Registration successful. You can now log in.")
            else:
                print("Weak password. Make sure it has at least 8 characters, "
                      "including uppercase, lowercase, numbers, and special characters.")

    def login(self, username, password):
        # Check if the username exists and the password is correct
        if username in self.users and self.users[username] == password:
            print(f"Welcome, {username}! You are now logged in.")
        else:
            print("Invalid username or password. Please try again.")

    def logout(self, username):
        # Check if the user is logged in
        if username in self.users:
            print(f"Goodbye, {username}! You are now logged out.")
        else:
            print("You are not currently logged in.")

    def recover_password(self, username, recovery_email):
        # Check if the username exists and the recovery email matches
        if username in self.users and self.recovery_emails.get(username) == recovery_email:
            # Generate a random recovery code (for demonstration purposes)
            recovery_code = ''.join(random.choices('0123456789', k=6))
            print(f"Recovery code sent to {recovery_email}: {recovery_code}")
        else:
            print("Invalid username or recovery email. Please try again.")

# Example usage
if __name__ == "__main__":
    auth_system = UserAuthenticationSystem()

    while True:
        print("\n1. Register\n2. Login\n3. Logout\n4. Recover Password\n5. Exit")
        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == "1":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            recovery_email = input("Enter your recovery email: ")
            auth_system.register(username, password, recovery_email)

        elif choice == "2":
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            auth_system.login(username, password)

        elif choice == "3":
            username = input("Enter your username: ")
            auth_system.logout(username)

        elif choice == "4":
            username = input("Enter your username: ")
            recovery_email = input("Enter your recovery email: ")
            auth_system.recover_password(username, recovery_email)

        elif choice == "5":
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please try again.")
'''


