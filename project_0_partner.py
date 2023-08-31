print("You are off on your space mission! You've just taken off and left the Earth's atmosphere. Your team is ready for an adventure of a lifetime! The goal of this mission is to try to find life in the universe. As the captain - you now have an important choice. Where do you go?")
userInput = input("Enter A, B or C. A) Fly into a black hole B) Head into empty space or C) Head towards Mars")

#if userInput == 'A':
# Student 1 finishes this code

if userInput == 'B':
# Student 2 finishes this code
    print("You're cruising through a starry abyss when suddenly, you see a giant, flaming sphere in the distance!")
    b_input_one = input("Uh oh... It's heading towards your vessle at an alarming rate!  What do you do?! A) Accept your fate B) Jump to light speed!")
    if b_input_one == 'A':
        print("What?!  The flame makes a sharp turn right as you are preparing for your end!")
        b_input_two = input("Out of the flames emerges a purple alien with three eyes and four arms!  It latches onto your vessel, making lots of alien noises.  Do you let it in? Y/N")
        if b_input_two == 'Y':
            print("It asks you to take it to Earth so it can see the ocean and the sky.  You head back home and become besties!")
        elif b_input_two == 'N':
            print("You head back home, and carry this guilt with you forever :(")
    elif b_input_one == 'B':
        print("The speed of light?!  What made you think you would survive that?  Everyone on the vessel evaporates into thin air!")


else: 
    print("You entered something wrong - refresh and try again!")