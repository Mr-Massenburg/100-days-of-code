# Day 24 | Auto addressing letters - working with files and directories. 

with open("./Input/Names/invited_names.txt") as file:
    names = file.read().splitlines()

with open("./Input/Letters/starting_letter.txt") as letter:
    template = letter.read()
    for name in names:
        new_email = template.replace("[name]", name)
        with open(f"./Output/ReadyToSend/{name}_ready.txt", mode='w') as new_letter:
            new_letter.write(new_email)