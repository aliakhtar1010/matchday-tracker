import csv
import os

FILE_NAME = "matches.csv"
HEADERS = [
    "player",
    "date",
    "opponent",
    "team_score",
    "opponent_score",
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

    team_score = get_positive_int("Your team's score: ")
    opponent_score = get_positive_int("Opponent's score: ")
    minutes = get_positive_int("Minutes played: ")
    goals = get_positive_int("Goals: ")
    assists = get_positive_int("Assists: ")

    if team_score < opponent_score:
        result = "Loss"
    elif team_score > opponent_score:
        result = "Win"
    else:
        result = "Draw"

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(
            [
                player,
                date,
                opponent,
                team_score,
                opponent_score,
                minutes,
                goals,
                assists,
                result,
            ]
        )

    print(f"Match added successfully! Result: {result}\n")


def view_matches():
    """Display every match stored in the CSV file."""
    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.reader(file)
        next(reader, None)

        print("\nMatch History")
        print("-" * 130)

        has_matches = False

        for row in reader:
            if len(row) < 9:
                continue

            has_matches = True

            print(
                f"Player: {row[0]} | "
                f"Date: {row[1]} | "
                f"Opponent: {row[2]} | "
                f"Score: {row[3]}-{row[4]} | "
                f"Minutes: {row[5]} | "
                f"Goals: {row[6]} | "
                f"Assists: {row[7]} | "
                f"Result: {row[8]}"
            )

        if not has_matches:
            print("No matches recorded yet.")

        print()


def show_summary():
    """Calculate and display performance statistics."""
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
            if len(row) < 9:
                continue

            try:
                minutes = int(row[5])
                goals = int(row[6])
                assists = int(row[7])
            except ValueError:
                continue

            total_minutes += minutes
            total_goals += goals
            total_assists += assists
            total_matches += 1

            if row[8] == "Win":
                wins += 1
            elif row[8] == "Loss":
                losses += 1
            elif row[8] == "Draw":
                draws += 1

    total_goal_contributions = total_goals + total_assists

    print("\nPerformance Summary")
    print("-" * 50)

    print(f"Total Matches: {total_matches}")
    print(f"Total Minutes: {total_minutes}")
    print(f"Total Goals: {total_goals}")
    print(f"Total Assists: {total_assists}")
    print(f"Goal Contributions: {total_goal_contributions}")
    print(f"Record: {wins}W - {losses}L - {draws}D")

    if total_matches > 0:
        win_percentage = (wins / total_matches) * 100
        avg_goals = total_goals / total_matches
        avg_assists = total_assists / total_matches

        print(f"Win Rate: {win_percentage:.1f}%")
        print(f"Average Goals per Match: {avg_goals:.2f}")
        print(f"Average Assists per Match: {avg_assists:.2f}")
    else:
        print("Win Rate: 0.0%")
        print("No matches recorded yet.")

    if total_minutes > 0:
        goals_per_90 = (total_goals / total_minutes) * 90
        assists_per_90 = (total_assists / total_minutes) * 90
        goal_contributions_per_90 = (
            total_goal_contributions / total_minutes
        ) * 90

        print(f"Goals / 90: {goals_per_90:.2f}")
        print(f"Assists / 90: {assists_per_90:.2f}")
        print(f"G+A / 90: {goal_contributions_per_90:.2f}")
    else:
        print("Goals / 90: 0.00")
        print("Assists / 90: 0.00")
        print("G+A / 90: 0.00")

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