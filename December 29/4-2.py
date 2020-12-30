# DRAGON REALM SKELETON CODE
# Basic Computing 2020 Winter, 002, Group 4
# Tutor Wonseok Shin (CSE)

import time, random

# STEP 6, 7 : REPEATED GAMEPLAY LOOP
replay = "yes"
while replay == "yes" or replay == "y":
    # STEP 1 : PRINT INTRO MESSAGE
    # print intro message, one line per second.
    # you may use time.sleep(1)
    print("You are in a land full of dragons.")
    time.sleep(1)
    print("In front of you, you see two caves.")
    time.sleep(1)
    print("In one cave, the dragon is friendly,")
    time.sleep(1)
    print("and will share his treasure with you.")
    time.sleep(1)
    print("The other dragon is greedy and hungry,")
    time.sleep(1)
    print("and will eat you on sight.\n")

    # STEP 2 : PRINT CAVE SELECTION
    # get user input, send to cave
    cave = ""
    while not(cave == "1" or cave == "2"):
        cave = input("Which cave will you go into? (1 or 2)")
    cave = int(cave)

    # STEP 3 : DRAGON APPEARS...
    # print message
    print("\nYou approach the cave...")
    time.sleep(1)
    print("It is dark and spooky...")
    time.sleep(1)
    print("A large dragon jumps out in front of you!")
    time.sleep(1)
    print("He opens his jaws and...")
    time.sleep(1)

    # STEP 4 : CHECK RANDOM VALUE.
    # Depending on random value, print message
    dragon = random.randint(1, 2)
    if cave == dragon:
        print("Gives you his treasure!")
    else:
        # STEP 8 : IMPLEMENT FIGHT PART
        # 6 attack chance, each random attack.
        atkchance = 0
        dragonHP = 100
        while True:
            atkchance += 1
            atk = random.randint(1, 30)
            time.sleep(1)
            print(f"You hit dragon with {atk} damage!")
            dragonHP -= atk
            if dragonHP <= 0:
                print("You won the fight!")
                break
            if atkchance >= 6:
                print('Gobbles you down in one bite!')

    # STEP 6, 7 : REPEATED GAMEPLAY LOOP, ENDING GAME
    replay = input("Do you want to play again?(yes or no)\n\n")

print("Thank you!")