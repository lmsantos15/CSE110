# 09 Prepare: Checkpoint

friends= []
new_friends = ""
print()

while new_friends.lower() != "end":
    new_friends = input("Type the name of a friend: ")

    if new_friends != "end":
        friends.append(new_friends)

print()

for client in friends:
    print(f"Your friends are: {client}")

print()