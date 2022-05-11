print("Welcome to the Python Voting program")
results = {}
votes = 0
voters = int(input("how many people are voting?: "))
selections = input("what are you voting on? separate selections with comma: ").split(",")

count_list = []

while votes < voters:
    name = input("whats your name?: ")
    selection = input(f"select one of the following {selections}: ")
    if selection in selections:
        results[name] = selection
        votes += 1
        count_list.append(selection)
    else:
        print("please start over and enter a proper value ")

winner_dict = {}
for i in range(len(selections)):
    winner_dict[count_list[i]] = count_list.count(count_list[i])
    print(count_list.count(count_list[i]), f"votes for {count_list[i]}")


max_key = max(winner_dict, key=winner_dict.get)
print(f"{max_key} is the winner!")
