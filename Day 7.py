def draw_hangman(lives):
    stages = [
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / \\
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |   / 
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |   /|\\
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |   /|
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |    |
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    O
         |    
         |    
         |
        --------
        """,
        """
         ------
         |    |
         |    
         |    
         |    
         |
        --------
        """
    ]
    print(stages[6 - lives])

def word_to_guess():
    word = input("Dame la palabra a adivinar: ").lower()
    print("\n" * 50)
    word_array = list(word)
    puzzle = ["_" for _ in word_array]
    lives = 6
    guessed_letters = []

    while lives > 0 and puzzle != word_array:
        draw_hangman(lives)
        print("Palabra:", ' '.join(puzzle))
        print("Letras usadas:", ', '.join(guessed_letters))
        guess = input("Adivina una letra: ").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Ingresa solo UNA letra válida.")
            continue

        if guess in guessed_letters:
            print("Ya usaste esa letra.")
            continue

        guessed_letters.append(guess)

        if guess in word_array:
            for i in range(len(word_array)):
                if word_array[i] == guess:
                    puzzle[i] = guess
            print("¡Correcto!")
        else:
            lives -= 1
            print("Incorrecto, pierdes una vida.")

    if puzzle == word_array:
        print("\n¡Felicidades! Adivinaste la palabra:", ''.join(word_array))
    else:
        draw_hangman(lives)
        print("\n¡Perdiste! La palabra era:", ''.join(word_array))

# Iniciar juego
word_to_guess()
