import csv
filename = "hoopifyapp.csv"
def load_data():
    data = {}
    try:
        with open(filename, "r") as f:
            reader = csv.reader(f)
            next(reader)
            for row in reader:
                data[row[0]] = {
                    "Name": row[1],
                    "Team": row[2],
                    "Points": int(row[3]),
                    "Assists": int(row[4]),
                    "Rebounds": int(row[5])
                }
    except FileNotFoundError:
        pass
    return data

def save_data(data):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["PlayerID", "Name", "Team", "Points", "Assists", "Rebounds"])
        for pid, stats in data.items():
            writer.writerow([pid, stats["Name"], stats["Team"], stats["Points"], stats["Assists"], stats["Rebounds"]])

def add_player(data):
    pid = input("Enter Player ID: ")
    if pid in data:
        print("Player already exists.")
    else:
        name = input("Enter Player Name: ")
        team = input("Enter Team Name: ")
        points = int(input("Enter Points Scored: "))
        assists = int(input("Enter Assists: "))
        rebounds = int(input("Enter Rebounds: "))
        data[pid] = {"Name": name, "Team": team, "Points": points, "Assists": assists, "Rebounds": rebounds}
        save_data(data)
        print("Player record added.")

def delete_player(data):
    pid = input("Enter Player ID to delete: ")
    if pid in data:
        data.pop(pid)
        save_data(data)
        print("Player record deleted.")
    else:
        print("Player not found.")

def search_player(data):
    pid = input("Enter Player ID to search: ")
    if pid in data:
        p = data[pid]
        print("Found:", pid, p["Name"], "| Team:", p["Team"], "| Points:", p["Points"], "| Assists:", p["Assists"], "| Rebounds:", p["Rebounds"])
    else:
        print("Player not found.")

def display_players(data):
    if data:
        print("\nBasketball Player Stats:")
        for pid, p in data.items():
            print(pid, p["Name"], "| Team:", p["Team"], "| Points:", p["Points"], "| Assists:", p["Assists"], "| Rebounds:", p["Rebounds"])
    else:
        print("No player records.")

def update_stats(data):
    pid = input("Enter Player ID to update stats: ")
    if pid in data:
        points = int(input("Enter New Points: "))
        assists = int(input("Enter New Assists: "))
        rebounds = int(input("Enter New Rebounds: "))
        data[pid]["Points"] = points
        data[pid]["Assists"] = assists
        data[pid]["Rebounds"] = rebounds
        save_data(data)
        print("Stats updated.")
    else:
        print("Player not found.")
def main_menu():
    data = load_data()
    while True:
        print("Hoopify Main Menu")
        print("1. Add Player")
        print("2. Delete Player")
        print("3. Search Player")
        print("4. Display All Players")
        print("5. Update Player Stats")
        print("6. Exit")

        choice = input("Enter choice: ")
        if choice == "1":
            add_player(data)
        elif choice == "2":
            delete_player(data)
        elif choice == "3":
            search_player(data)
        elif choice == "4":
            display_players(data)
        elif choice == "5":
            update_stats(data)
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("Invalid choice.")
#Opening
print("Welcome to Hoopify-A Fitness Tracker Made Just for Basketball")
print("An App Made by Gokul Sanjeev Shenoy")
print("I'm Cody, your robot-coach capable enough for tracking your stats to be a great in the game of basketball")
print("Trying to be the next Jaylen Brown or the next Kobe Bryant-well, this app is made for you")
print("Are you ready to score a 3-pointer now or track your stats?")
check = input("Yes/No? ").strip().lower()
if check == "yes":
    print("Alright then..time to begin your journey..")
    main_menu() 
else:
    print("Alright then, keep playing and keep showing up at the court")
    print("Goodbye!")
