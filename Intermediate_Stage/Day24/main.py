PLACEHOLDER = "[name]"

with open("./Input/Names/invited_names.txt") as name_file:
    names = name_file.readlines()


with open("./Input/Letters/starting_letter.txt") as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        clean_name = name.replace("\n", "")
        new_letter = letter_contents.replace(PLACEHOLDER, clean_name)
        print(new_letter)
        with open(f"./Output/ReadyToSend/letter_to_{clean_name}.txt", mode="w") as saved_letter:
            saved_letter.write(new_letter)
