import re

#pregame setup

answer = "What's up, doc?"

answer = answer.upper()

answer_flags = []

for current_answer_character in answer:
    if re.search("^[A-Z]$", current_answer_character):
        answer_flags.append(False)
    else: 
        answer_flags.append(True)

# game logic
MAX_INCORRECT_GUESSES = 5

num_of_incorrect_guesses = 0

guessed_letters = []

while num_of_incorrect_guesses < MAX_INCORRECT_GUESSES and False in answer_flags:
    print(f"Number of Incorrect guesses remaining: {MAX_INCORRECT_GUESSES - num_of_incorrect_guesses}")                                                                                                                               

    print()

    print("Gussed letters: ", end = "")

    for current_gussed_letter in guessed_letters:
        print(current_gussed_letter, end = " ")
    
    print()
    print()

    for current_answer_index in range(len(answer)):
        if answer_flags[current_answer_index]:
            print(answer[current_answer_index], end = "")
        else:
            print("_", end = "")
    
    print()
    print()

    letter = input("Enter a letter : ")


    letter = letter.upper()

    if re.search("^[A-Z]$", letter) and len(letter) == 1 and letter not in guessed_letters:
        # add letters to guessed letters through insertion sort.
        current_insertion_index = 0

        for current_guessed_letter in guessed_letters:
            if letter < current_guessed_letter:
                break
            current_insertion_index += 1

        guessed_letters.insert(current_insertion_index, letter)

        #check if letter is in the puzzle
        if letter in answer:
            for current_answer_index in range(len(answer)):
                if answer[current_answer_index] == letter:
                    answer_flags[current_answer_index] = True
        else:
            num_of_incorrect_guesses += 1

# post game smmary.
if num_of_incorrect_guesses < MAX_INCORRECT_GUESSES:
    print("You win!!!!!!!!!!!")
else:
    print(" You Lose!!!!!!!!!!!!")
print()

print(f"The answer was {answer}")
            



