print("You are off on your space mission! You've just taken off and left the Earth's atmosphere. Your team is ready for an adventure of a lifetime! The goal of this mission is to try to find life in the universe. As the captain - you now have an important choice. Where do you go?")
userInput = input("Enter A, B or C. A) Fly into a black hole B) Head into empty space or C) Head towards Mars")

if userInput == 'A':
# Student 1 finishes this code

elif userInput == 'B':
# Student 2 finishes this code 

elif userInput == 'C':
# Student 3 finishes this code
C_story = print("Once you arrive on Mars, there are footprints in the terrain that lead to a dark and foreboding cave.")
C_userChoice = input("Do you A) follow the tracks? Or do you B) keep wandering around on Mars?")

    if C_userChoice == 'A':
    #Cave Scene
        C2A_story = print("You arrive at the mouth of the ominous cave. The smell of mold and dampness seems to grow stronger the more you progress into the cave's uncertainty. After walking for what felt like hours, you start to make out a dim glow in the distance. As you run towards the light, you stop in the middle of a cavern within the cave but are blinded by the sheer amount of light all around you.")
        C2A_userChoice = input("Do you A) Turn back from the blinding room? Or do you B) Wait for your eyes to adjust so you can see the room?")
    
    if C2A_userChoice == 'A':
        C2A_answer = print("You turn back from the blinding room but end up getting lost in the many tuneels of the cave. There is no way out and you eventually perish due to a lack of oxygen.")
    elif C2A_userChoice == 'B':
        C2B_answer = print("Once your eyes adjust to the brightness of the cavern. you see thousands of twinkling diamonds. You take a handful back with you through the cave and bring them back to Earth with you where you become famous for your discovery.")

    elif C_userChoice == 'B':
        C2B_story = print("You ignore the tracks and keep wandering the lifeless surface of Mars. Now stranded after hours of aimlessly walking, you ultimately perish due to a lack of oxygen.")


else: 
    print("You entered something wrong - refresh and try again!")
