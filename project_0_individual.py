print("Welcome to the Space Travel Calculator!")

distance = int(input("How many light years away is the celestial object?"))

speed = int(input("How fast is the spacecraft in fraction of the speed of light?"))

time = distance/speed

print("It will take ", time, "lightyears per fraction of the speed of light.")