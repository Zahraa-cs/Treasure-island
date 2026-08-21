print("""
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝
""")

print("Welcome to my island")

door = input("There are two doors in front of you, red and blue.\nWhich door do you want to open? ").lower()

if door == "red":
    print("Now you entered a room.\nYou found three boxes: white, black, and green.")

    second_door = input("Which one do you choose? ").lower()

    if second_door == "white":
        print("Box full of snakes")
    elif second_door == "black":
        print("Box full of spiders")
    elif second_door == "green":
        print("Congratulations, you win!")
    else:
        print("Invalid choice")

elif door == "blue":
    print("You entered a room full of crocodiles")

else:
    print("Invalid choice")