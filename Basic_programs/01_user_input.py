def greeting_user():
    user_name = input("Enter your name: ")
    while len(user_name) < 3:
        print("name should be at least 3 letters")
        user_name = input("Enter your name: ")
        print(f"hello {user_name} How are you?")

greeting_user()

# a = input("Enter your name")
# print("Hello", a, "How are you")