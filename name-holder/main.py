# load invitee names
with open("Input/Names/invited_names.txt") as names_file:
    names = names_file.readlines()

PLACEHOLDER = '[name]'
with open('Input/Letters/letter_template.txt') as letter_file:
    content = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        print(stripped_name)
        new_letter = content.replace(PLACEHOLDER, stripped_name)
        with open(f"./Output/ReadyToSend/letter_for_{stripped_name}.txt", mode='w') as completed_letter:
            completed_letter.write(new_letter)

