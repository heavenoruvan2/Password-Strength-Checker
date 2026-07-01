from password_checker import check_password

print("=" * 40)
print("      PASSWORD STRENGTH CHECKER")
print("=" * 40)

while True:
    password = input("\nEnter Password: ")

    result = check_password(password)

    print("\nStrength :", result["strength"])
    print("Score    :", result["score"], "/5")

    print("\nSuggestions:")
    if result["tips"]:
        for tip in result["tips"]:
            print("-", tip)
    else:
        print("Excellent Password!")

    choice = input("\nCheck another password? (y/n): ")

    if choice.lower() != "y":
        print("Thank you!")
        break
