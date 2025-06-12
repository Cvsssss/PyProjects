#Tresure island game

def dibujar_cofre_del_tesoro():
    cofre = r"""
           ______________________
          /|                    |\
         /_|____________________|_\
        |/////////////////////////|
        |////   ___    ___   /////|
        |////  /___\  /___\  /////|
        |////  \_$_/  \_$_/  /////|
        |////   $$$    $$$   /////|
        |////  $$$$$  $$$$$  /////|
        |/////////////////////////|
        |_________________________|
        |_________________________|
        |_________________________|
        |                         |
        |                         |
        |_________________________|
    """
    print(cofre)

dibujar_cofre_del_tesoro()

print("Welcome to the Island Game")
print("Are you ready for the adventure?")

colour = input("Select a colour (red or blue): ").lower()
if (colour == "blue"):
    print ("You can continue")
    print ("Now, select a path, right or left?")
    path = input("Select a path: ").lower()
    if (path == "left"):
        print ("You can continue")
        print ("Now, select a number, one or two")
        number = input("Select a number: ").lower()
        if (number == "one"):
            print ("You won")
        else:
            print ("You lost")
    else:
        print("YOu lost")
else:
    print("You lost") 

        