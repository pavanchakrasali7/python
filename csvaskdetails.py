import csv

# Step 2: Load the CSV Data
def load_csv_data(file_path):
    data = []
    with open("C:\\Users\\pavan\\OneDrive\\Desktop\\projects\\ipl auction prediction\\Ipl Data\\2023.csv", mode='r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

# Step 3: Function to Answer Questions
def answer_question(data, question):
    question = question.lower()

    if "how many" in question and "people" in question:
        return f"There are {len(data)} people in the dataset."

    elif "average age" in question:
        ages = [int(row["Age"]) for row in data]
        average_age = sum(ages) / len(ages)
        return f"The average age is {average_age:.2f} years."

    elif "oldest person" in question:
        oldest_person = max(data, key=lambda x: int(x["Age"]))
        return f"The oldest person is {oldest_person['Name']} who is {oldest_person['Age']} years old."

    elif "youngest person" in question:
        youngest_person = min(data, key=lambda x: int(x["Age"]))
        return f"The youngest person is {youngest_person['Name']} who is {youngest_person['Age']} years old."

    elif "who is" in question and "engineer" in question:
        for row in data:
            if row["Occupation"].lower() == "engineer":
                return f"{row['Name']} is an engineer."

    elif "from" in question:
        country = question.split("from")[-1].strip().capitalize()
        people_from_country = [row["Name"] for row in data if row["Country"] == country]
        if people_from_country:
            return f"People from {country}: {', '.join(people_from_country)}."
        else:
            return f"No one is from {country} in the dataset."

    else:
        return "I don't understand the question."
    if "how many players" in question:
        return f"There are {len(data)} players in the dataset."

    elif "highest raa" in question:
        highest_raa_player = max(data, key=lambda x: int(x["RAA"]))
        return f"The player with the highest RAA is {highest_raa_player['Player']} with an RAA of {highest_raa_player['RAA']}."

    elif "lowest salary" in question:
        lowest_salary_player = min(data, key=lambda x: int(x["Salary"]))
        return f"The player with the lowest salary is {lowest_salary_player['Player']} earning ${int(lowest_salary_player['Salary']):,}."

    elif "best efscore" in question:
        best_efscore_player = max(data, key=lambda x: float(x["EFScore"]))
        return f"The player with the best EFScore is {best_efscore_player['Player']} with an EFScore of {best_efscore_player['EFScore']}."

    elif "most valuable" in question:
        most_valuable_player = max(data, key=lambda x: int(x["Value"]))
        return f"The most valuable player is {most_valuable_player['Player']} with a value of ${int(most_valuable_player['Value']):,}."

    elif "team" in question:
        team = question.split("team")[-1].strip().capitalize()
        players_in_team = [row["Player"] for row in data if row["Team"].lower() == team.lower()]
        if players_in_team:
            return f"Players in {team}: {', '.join(players_in_team)}."
        else:
            return f"No players found from the team {team}."

    elif "wins" in question:
        highest_wins_player = max(data, key=lambda x: int(x["Wins"]))
        return f"The player with the most wins is {highest_wins_player['Player']} with {highest_wins_player['Wins']} wins."

    else:
        return "I don't understand the question."

# Step 4: Main Function to Handle User Input
def main():
    file_path = "C:\\Users\\pavan\\OneDrive\\Desktop\\projects\\ipl auction prediction\\Ipl Data\\2023.csv"  # Replace with the path to your CSV file
    data = load_csv_data("C:\\Users\\pavan\\OneDrive\\Desktop\\projects\\ipl auction prediction\\Ipl Data\\2023.csv")
    
    print("You can ask questions about the data. Type 'exit' to quit.")
    while True:
        question = input("Ask a question: ")
        if question.lower() == "exit":
            break
        answer = answer_question(data, question)
        print(answer)

if __name__ == "__main__":
    main()

