#quote generator
import random

# Function to get a random quote from a file
def get_random_quote_from_file(file_path):
    with open(file_path, "r") as file:
        quotes = file.readlines()
    return random.choice(quotes).strip()
# Generate a random quote
while True:
    user_input = input("Do you want to read a hadith? (yes/no): ").strip().lower()
    if user_input == "yes":
        quote = get_random_quote_from_file("quotes.txt")
        print("\nHere's your quote:")
        print(quote)
        print()
    elif user_input == "no":
        print("Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")

