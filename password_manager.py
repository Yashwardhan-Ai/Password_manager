# Simple Password Manager (without encryption)

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, password):
        self.passwords[website] = password
        print(f"Password for {website} added successfully!")

    def retrieve_password(self, website):
        if website in self.passwords:
            print(f"Password for {website}: {self.passwords[website]}")
        else:
            print(f"No password found for {website}.")

    def view_saved_websites(self):
        print("Saved websites:")
        for site in self.passwords:
            print(site)

def main():
    manager = PasswordManager()

    while True:
        print("\nPassword Manager Menu:")
        print("1. Add Password")
        print("2. Retrieve Password")
        print("3. View Saved Websites")
        print("4. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            website = input("Enter website name: ")
            password = input("Enter password: ")
            manager.add_password(website, password)

        elif choice == '2':
            website = input("Enter website name: ")
            manager.retrieve_password(website)

        elif choice == '3':
            manager.view_saved_websites()

        elif choice == '4':
            print("Exiting Password Manager. Goodbye!")
            break

if __name__ == "__main__":
    main()


