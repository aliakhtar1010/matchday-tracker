import csv
import os

FILE_NAME = "matches.csv"
HEADERS = ["player", "opponent", "goals", "assists", "result"]


def create_file_if_missing():
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


def get_positive_int(prompt):
    while True:
        value = input(prompt)

        if value.isdigit():
            return int(value)

        print("Please enter a valid number.")


def get_match_result():
    while True:
        result = input("Result (Win/Loss/Draw): ").strip().capitalize()

        if result in ["Win", "Loss", "Draw"]:
            return result

        print("Please enter Win, Loss, or Draw.")


def add_match():
    player = input("Player name: ").strip()

    if player == "":
        player = "Unknown"

    opponent = input("Opponent: ").strip()

    if opponent == "":
        opponent = "Unknown"

    goals = get_positive_int("Goals: ")
    assists = get_positive_int("Assists: ")
    result = get_match_result()

    with open(FILE_NAME, "a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([player, opponent, goals, assists, result])

    print("Match added successfully!\n")


def view_matches():
    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        print("\nMatch History")
        print("-" * 50)

        has_matches = False

        for row in reader:
            has_matches = True
            print(
                f"Player: {row[0]} | Goals: {row[1]} | "
                f"Assists: {row[2]} | Result: {row[3]}"
            )

        if not has_matches:
            print("No matches recorded yet.")

        print()


def show_summary():
    total_goals = 0
    total_assists = 0
    total_matches = 0
    wins = 0
    losses = 0
    draws = 0

    with open(FILE_NAME, "r") as file:
        reader = csv.reader(file)
        next(reader)

        for row in reader:
            total_goals += int(row[1])
            total_assists += int(row[2])
            total_matches += 1

            if row[3] == "Win":
                wins += 1
            elif row[3] == "Loss":
                losses += 1
            elif row[3] == "Draw":
                draws += 1

    print("\nPerformance Summary")
    print("-" * 50)
    print(f"Total Matches: {total_matches}")
    print(f"Total Goals: {total_goals}")
    print(f"Total Assists: {total_assists}")
    print(f"Record: {wins}W - {losses}L - {draws}D")

    if total_matches > 0:
        avg_goals = total_goals / total_matches
        avg_assists = total_assists / total_matches

        print(f"Average Goals per Match: {avg_goals:.2f}")
        print(f"Average Assists per Match: {avg_assists:.2f}")
    else:
        print("No matches recorded yet.")

    print()


def main():
    create_file_if_missing()

    while True:
        print("===== Matchday Tracker =====")
        print("1. Add match")
        print("2. View matches")
        print("3. Show summary")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            add_match()
        elif choice == "2":
            view_matches()
        elif choice == "3":
            show_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.\n")


if __name__ == "__main__":
    main()