import time
import os

FILE_NAME = "time_capsule.txt"

def save_message():
    message = input("Enter your secret message: ")
    unlock_time = int(input("Enter unlock time in seconds: "))  

    with open(FILE_NAME, "w") as file:
        file.write(f"{time.time() + unlock_time}\n{message}")

    print(f"Your message is locked! Come back in {unlock_time} seconds.")

def read_message():
    if not os.path.exists(FILE_NAME):
        print("No time capsule found!")
        return
    
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
        unlock_time = float(lines[0].strip())
        message = lines[1]

    if time.time() >= unlock_time:
        print(f"Your message: {message}")
        os.remove(FILE_NAME)  # Delete after reading
    else:
        print("The message is still locked! Wait a little longer.")

def main():
    while True:
        print("\n1. Write a new message\n2. Read message\n3. Exit")
        choice = input("Choose an option: ")
        
        if choice == "1":
            save_message()
        elif choice == "2":
            read_message()
        elif choice == "3":
            break
        else:
            print("Invalid choice! Try again.")

if __name__ == "__main__":
    main()
