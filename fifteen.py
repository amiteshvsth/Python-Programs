import datetime

# Function to reserve a ticket
def reserve_ticket():
    train_no = input("Enter train number: ")
    passenger_name = input("Enter passenger name: ")
    age = input("Enter passenger age: ")
    gender = input("Enter passenger gender (M/F): ")
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Write reservation details to file
    with open("reservations.txt", "a") as file:
        file.write(f"{train_no},{passenger_name},{age},{gender},{timestamp}\n")
        print("Ticket reserved successfully!")

# Function to list all reservations for today's trains
def list_reservations():
    today = datetime.date.today().strftime("%Y-%m-%d")
    with open("reservations.txt", "r") as file:
        for line in file:
            fields = line.strip().split(",")
            if fields[-1].startswith(today):
                print(f"Train No: {fields[0]}")
                print(f"Passenger Name: {fields[1]}")
                print(f"Age: {fields[2]}")
                print(f"Gender: {fields[3]}")
                print(f"Timestamp: {fields[4]}")
                print("--------------")

# Main function
def main():
    while True:
        print("\nMenu:")
        print("1. Reserve a ticket")
        print("2. List all reservations for today's trains")
        print("3. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            reserve_ticket()
        elif choice == "2":
            list_reservations()
        elif choice == "3":
            break
        else:
            print("Invalid choice. Try again.")

# Run the main function
if __name__ == "__main__":
    main()
