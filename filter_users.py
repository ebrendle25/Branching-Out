import json


def load_users():
    """Load users from the JSON file. Returns an empty list on error."""
    try:
        with open("users.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: 'users.json' was not found.")
        return []
    except json.JSONDecodeError:
        print("Error: 'users.json' is not valid JSON.")
        return []


def print_users(users):
    """Print a list of users, or a message if none were found."""
    if not users:
        print("No users found.")
        return
    for user in users:
        print(user)


def filter_users_by_name(name):
    users = load_users()
    filtered_users = [
        user for user in users
        if user.get("name", "").lower() == name.lower()
    ]
    print_users(filtered_users)


def filter_users_by_age(age):
    users = load_users()
    filtered_users = [user for user in users if user.get("age") == age]
    print_users(filtered_users)


def filter_users_by_email(email):
    users = load_users()
    filtered_users = [
        user for user in users
        if user.get("email", "").lower() == email.lower()
    ]
    print_users(filtered_users)


if __name__ == "__main__":
    filter_option = input(
        "What would you like to filter by? (name, email, age): "
    ).strip().lower()

    if filter_option == "name":
        name_to_search = input("Enter a name to filter users: ").strip()
        filter_users_by_name(name_to_search)
    elif filter_option == "email":
        email_to_search = input("Enter an email to filter users: ").strip()
        filter_users_by_email(email_to_search)
    elif filter_option == "age":
        age_input = input("Enter an age to filter users: ").strip()
        try:
            age_to_search = int(age_input)
            filter_users_by_age(age_to_search)
        except ValueError:
            print(f"'{age_input}' is not a valid age. Please enter a number.")
    else:
        print("Filtering by that option is not yet supported.")