voters = {}
parties = {
    1: {"name": "ADMK", "votes": 0},
    2: {"name": "DMK", "votes": 0},
    3: {"name": "BJP", "votes": 0},
    4: {"name": "CONGRESS", "votes": 0}
}
def add_voter():
    voter_id = input("Enter voter ID: ")
    if voter_id in voters:
        print("Voter already exists!")
    else:
        name = input("Enter voter name: ")
        voters[voter_id] = {"name": name, "has_voted": False}
        print(f"Voter {name} added successfully!")

def list_parties():
    print("Available parties to vote for:")
    for party_id, party_info in parties.items():
        print(f"{party_id}: {party_info['name']}")

def cast_vote():
    voter_id = input("Enter voter ID: ")
    if voter_id not in voters:
        print("Voter ID not found!")
        return
    if voters[voter_id]["has_voted"]:
        print("You have already voted!")
        return
    
    list_parties()
    party_id = int(input("Enter the party ID you want to vote for: "))
    if party_id not in parties:
        print("Invalid party ID!")
    else:
        parties[party_id]["votes"] += 1
        voters[voter_id]["has_voted"] = True
        print(f"Vote successfully cast for {parties[party_id]['name']} Party")

def calculate_winner():
    sorted_parties = sorted(parties.items(), key=lambda x: x[1]["votes"], reverse=True)

    max_votes = sorted_parties[0][1]["votes"]
    winners = [party_info["name"] for party_id, party_info in sorted_parties if party_info["votes"] == max_votes]
    
    print("Election Results:")
    for party_id, party_info in sorted_parties:
        print(f"{party_info['name']}: {party_info['votes']} votes")
    
    if len(winners) > 1:
        print(f"\nIt's a tie! The following parties have {max_votes} votes: {', '.join(winners)}")
    else:
        print(f"\nCongrats {winners[0]} won with {max_votes} votes!")

    if len(sorted_parties) > 1 and sorted_parties[1][1]["votes"] < max_votes:
        second_leader = sorted_parties[1]
        print(f"\nSecond leading party is {second_leader[1]['name']} with {second_leader[1]['votes']} votes.")
    
    print("\nVote Differences with Winner:")
    for party_id, party_info in sorted_parties:
        vote_diff = max_votes - party_info["votes"]
        if vote_diff > 0:
            print(f"{party_info['name']} is behind by {vote_diff} votes.")

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
