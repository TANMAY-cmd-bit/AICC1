correct_password = "Admin@123"
attempts = 3
while attempts > 0:
    user_password = input("Enter your password: ")
    if user_password == correct_password:
        print("Login successful!")
        break
    else:
        attempts -= 1
        print("Incorrect password! Attempts left:", attempts)
if attempts == 0:
    print("Access denied!")