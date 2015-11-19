"""This is an implementation of the classic guess game "1A2B"
The program generates 4 random numbers and asks the user to guess the it. 
If a number the user guesses is in the program generated numbers, and is in the right position, 
the program returns 1A; If a number the user guesses is in the program generated numbers, 
and but is not in the right position, the program returns 1B. 
After each guess, the program will let the user know how many A and B's the user get for that guess. 
The user wins if he/she guesses the number correctly in 10 turns. 
"""

from random import randint
from random import sample

gen_num = sample(range(0,9),4)
gen_num_str = map(str, gen_num)


print "Hi, Welcome to the 1A2B game!"
print "Try to guess what number the computer generated!"
print "Please enter 4 different numbers."  


for tries in range(1,11):
    print "Try: ", tries
    guess = str(raw_input("Enter your guess: "))
    guess_list = []

    def guess_to_list(guess):
        for num in guess:
            guess_list.append(num)

    guess_to_list(guess)

    ##Calculate total of As and Bs
    
    def Count_B():
        total_B = 0
        for i in range(4):
            if guess_list[i] != gen_num_str[i]:
                if guess_list[i] in gen_num_str:
                    total_B += 1
        print total_B, "B"

    total_A = 0

    for each in range(4):
        if guess_list[each] == gen_num_str[each]:
            total_A = total_A + 1

    if total_A == 4:
        print "You win! Congrats!"
        break

    else:    
        if tries == 10:
            print "Sorry, you lose!"
            print "The correct answer is ", " ".join(gen_num_str)
        else:
            print total_A, "A"
            Count_B()

Thanks = raw_input("Thanks for playing!")


 









