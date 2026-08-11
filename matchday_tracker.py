import csv
import os

FILE_NAME = "matches.csv"
HEADERS = [
    "player",
    "date",
    "opponent",
    "minutes",
    "goals",
    "assists",
    "result",
]


def create_file_if_missing():
    """Create the CSV file and add headers if it does not exist or is empty."""
    if not os.path.exists(FILE_NAME) or os.path.getsize(FILE_NAME) == 0:
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(HEADERS)


def get_positive_int(prompt):
    """Keep asking until the user enters a non-negative whole number."""
    while True:
        value = input(prompt).strip()

        if value.isdigit():
            return int(value)

        print("Please enter a valid non-negative whole number.")


def get_match_result():
    """Keep asking until the user enters Win, Loss, or Draw."""
    while True:
        result = input("Result (Win/Loss/Draw): ").strip().capitalize()

        if result in ["Win", "Loss", "Draw"]:
            return result

        print("Please enter Win, Loss, or Draw.")


def add_match():
    """Collect match information and save it to the CSV file."""
    player = input("Player name: ").strip()

    if player == "":
        player = "Unknown"

    date = input("Match date (YYYY-MM-DD): ").strip()

    if date == "":
        date = "Unknown"

    opponent = input("Opponent: ").strip()

    if opponent == "":
        opponent = "Unknown"

    minutes = get_positive_int("Minutes played: ")
    goals = get_positive_int("Goals: ")
    assists = get_positive_int("Assists: ")
    result = get_match_result()

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [player, date, opponent, minutes, goals, assists, result]
        )

    print("Match added successfully!\n")


def view_matches():
    """Display every match stored in the CSV file."""
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        print("\nMatch History")
        print("-" * 110)

        has_matches = False

        for row in reader:
            if len(row) < 7:
                continue

            has_matches = True

            print(
                f"Player: {row[0]} | "
                f"Date: {row[1]} | "
                f"Opponent: {row[2]} | "
                f"Minutes: {row[3]} | "
                f"Goals: {row[4]} | "
                f"Assists: {row[5]} | "
                f"Result: {row[6]}"
            )

        if not has_matches:
            print("No matches recorded yet.")

        print()


def show_summary():
    """Calculate and display total and average performance statistics."""
    total_goals = 0
    total_assists = 0
    total_matches = 0
    total_minutes = 0

    wins = 0
    losses = 0
    draws = 0

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        for row in reader:
            if len(row) < 7:
                continue

            try:
                minutes = int(row[3])
                goals = int(row[4])
                assists = int(row[5])
            except ValueError:
                continue

            total_minutes += minutes
            total_goals += goals
            total_assists += assists
            total_matches += 1

            if row[6] == "Win":
                wins += 1
            elif row[6] == "Loss":
                losses += 1
            elif row[6] == "Draw":
                draws += 1

    print("\nPerformance Summary")
    print("-" * 50)

    print(f"Total Matches: {total_matches}")
    print(f"Total Minutes: {total_minutes}")
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
    """Run the main menu until the user chooses to exit."""
    create_file_if_missing()

    while True:
        print("===== Matchday Tracker =====")
        print("1. Add match")
        print("2. View matches")
        print("3. Show summary")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

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