
username = input("Enter your username: ")
email = input("Enter your email: ")
age = input("Enter your age: ")
password = input("Enter your password: ")

errors = {}

username_errors = []
if len(username) < 5:
    username_errors.append('username must be at least 5 characters long')
if username and username[0].isdigit():
    username_errors.append('username must not start with a digit')
if " " in username:
    username_errors.append('username must not contain spaces')
if username_errors:
    errors['username'] = username_errors

email_errors = []
if email.count('@') != 1:
    email_errors.append(f'email must contain one @, but found: {email.count("@")} ')
if email_errors:
    errors['email'] = email_errors

age_errors = []

if not age.isdigit():
    age_errors.append('age must be an integer')
if age.isdigit() and int(age) < 16:
    age_errors.append('age must be at least 16 years old')
if age_errors:
    errors['age'] = age_errors

password_errors = []
if len(password) < 8:
    password_errors.append('password must be at least 8 characters long')
if " " in password:
    password_errors.append('password must not contain spaces')
if password and len(set(password)) == 1:
    password_errors.append('password cannot consist of the same character')
if password_errors:
    errors['password'] = password_errors

if errors:
    print("Invalid data.")
    for field, faults in errors.items():
        for fault in faults:
            print(f"{field}: {fault}")
else:
    print("Valid data.")