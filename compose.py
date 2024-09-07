import os

poems_dir = "poems"
poem_files = sorted(os.listdir(poems_dir))

from mapping import georgian_to_russian

learned = {}

for (georgian_letter, russian_letters), poem_file in zip(georgian_to_russian.items(), poem_files):

    russian_letters_str = ", ".join(russian_letters)
    print(f"({georgian_letter}={russian_letters_str})")
    print()

    for russian_letter in russian_letters:
        learned[russian_letter] = georgian_letter
        learned[russian_letter.upper()] = georgian_letter
        
    
    poem_file = os.path.join(poems_dir, poem_file)
    with open(poem_file, "r") as file:
        poem_text = file.read()

    for russian_letter, georgian_letter in learned.items():
        poem_text = poem_text.replace(russian_letter, georgian_letter)

    print(poem_text)
    print()