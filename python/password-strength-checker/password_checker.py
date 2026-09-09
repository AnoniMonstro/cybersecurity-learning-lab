import re

print(" Password Strength Checker ")

password = input("Enter a password to analyze: ")

score = 0

if len(password) >= 8:
    score += 1

if re.search(r"[a-z]", password):
    score += 1

if re.search(r"[A-Z]", password):
    score += 1

if re.search(r"\d", password):
    score += 1

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    score += 1


print("\n Password Analysis")

if score <= 2:
    print(" Weak password")
elif score <= 4:
    print(" Medium password")
else:
    print(" Strong password")
