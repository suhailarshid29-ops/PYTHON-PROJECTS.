password = input("Enter password: ")

strength = 0

if len(password) >= 8:
    strength += 1

if any(char.isupper() for char in password):
    strength += 1

if any(char.islower() for char in password):
    strength += 1

if any(char.isdigit() for char in password):
    strength += 1

if strength <= 1:
    print("Password Strength: Weak")
elif strength == 2:
    print("Password Strength: Medium")
elif strength == 3:
    print("Password Strength: Good")
else:
    print("Password Strength: Strong")