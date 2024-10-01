voters = {}
parties = {
    "ADMK": 0,
    "DMK": 0,
    "BJP": 0,
    "CONGRESS": 0
}

def add_voter():
    voter_id = input("Enter voter ID: ")
    if voter_id in voters:
        print("Voter already exists!")
    else:
        name = input("Enter voter name: ")
        voters[voter_id] = {"name": name, "has_voted": False}
        print("Voter" , name ,"added successfully!")

def list_parties():
    print("Available parties to vote for:")
    for party in parties:
        print(party)

def cast_vote():
    voter_id = input("Enter voter ID: ")
    if voter_id not in voters:
        print("Voter ID not found!")
        return
    if voters[voter_id]["has_voted"]:
        print("You have already voted!")
        return
    
    list_parties()
    selected_party = input("Enter the party name you want to vote for: ")
    if selected_party not in parties:
        print("Invalid party name!")
    else:
        parties[selected_party] += 1
        voters[voter_id]["has_voted"] = True
        print(f"Vote successfully cast by {voters[voter_id]['name']} for {selected_party} Party")

def calculate_winner():
    max_votes = max(parties.values())
    winners = [party for party, votes in parties.items() if votes == max_votes]
    
    print("\nElection Results:")
    for party, votes in parties.items():
        print(f"{party}: {votes} votes")
    
    print(f"\nCongrats {', '.join(winners)} won with {max_votes} votes leading")

while True:
    print("Voting System Menu:")
    print("1. Add Voter")
    print("2. Cast Vote")
    print("3. Calculate Winner")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == "1":
        add_voter()
    elif choice == "2":
        cast_vote()
    elif choice == "3":
        calculate_winner()
    elif choice == "4":
        print("Exiting the voting system. Thank you!")
        break
    else:
        print("Invalid choice! Please try again.")


