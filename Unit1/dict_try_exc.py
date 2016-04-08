phone_book = {
    "Sarah Hughes": "01234 567890",
    "Tim Taylor": "02345 678901",
    "Sam Smith":  "03456 789012"
}

user = input("Enter a person's name from the phone book.")

try:
    print(phone_book[user])
except KeyError:
    print("Could not find user.")