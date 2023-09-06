print("You are off on your space mission! You've just taken off and left the Earth's atmosphere. Your team is ready for an adventure of a lifetime! The goal of this mission is to try to find life in the universe. As the captain - you now have an important choice. Where do you go?")
userInput = input("Enter A, B or C. A) Fly into a black hole B) Head into empty space or C) Head towards Mars")

if userInput == 'A':
    print("So, you wanna fly into a black hole. You think that's a smart idea?")
    a_input1 = input("Last chance to back out. Choose wisely. A) I'm getting out of here! B) Nah screw it, I'm going in!")
    if a_input1 == "A":
        print("Ah you're no fun. Directing ship back to home.")
    elif a_input1 == "B":
        print("Alright, that's the right idea! Directing course to the black hole, which we won't actually be able to see, but we'll know it when we get there.")
        a_input2B = input("\nSooooo it seems like the ship is being pulled by something and that pull is getting stronger and stronger. We must be approaching the black hole. Have any last words before we die a hopefully painless death? Y/N")
        if a_input2B == "Y":
            a_input2BY = input("Say them now my friend: ")
            print("I feel the same way. Goodbye friend. It was honor to fly with you.")
        elif a_input2B == "N":
            print("Well it was nice knowin' yah. Just before we die, know that this was all your idea.")
            

elif userInput == 'B':
# Student 2 finishes this code 

else: 
    print("You entered something wrong - refresh and try again!")
