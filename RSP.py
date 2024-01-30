from random import randint

# Define error if the Player enters something else than 0,1 or 2
class InvalidInputError(Exception):
    "The input is not 0, 1 or 2"
    pass

# Play Rock, Paper, Scissors
def rsp(n: int) -> None:
    games = [0, 0, 0]   # index 0 is wins, 1 is losses, 2 is draws
    for game in range(n):
        try:
            P = int(input('0. Scissor\n1. Rock\n2. Paper\n'))

            # Raise exception if input is not 0, 1 or 2
            if str(P) not in '012':
                raise InvalidInputError

            # Print player input
            print(f'Player: ({P})', 'Scissor' if P == 0 else 'Rock' if P == 1 else 'Paper')
            
            C = genRSP()    # Produce a throw

            # Print the computer's throw
            print(f'Computer: ({C})', 'Scissor' if C == 0 else 'Rock' if C == 1 else 'Paper')
            
            J = judgeP1(P,C) # Generate verdict for the current turn

            games[0] += 1 if J == 1 else 0      # increment wins if won
            games[1] += 1 if J == -1 else 0     # increment losses if lost
            games[2] += 1 if J == 0 else 0      # increment draws if drawn

            # Print verdict for the last game
            if J==1:
                print('you win!')
            elif J==0:
                print("It's a draw!")
            else:
                print('You lose!')

            print() # Print a newline after each turn
            
        # Catch the exception that is invoked when the input is not 0, 1 or 2
        except InvalidInputError:
            print("Input should be either Rock, Paper or Scissor.")
            
    print(f'Wins: {games[0]}\nLosses: {games[1]}\nDraws: {games[2]}\n' if n>1 else '')



# Check if Player1 won against Player2
def judgeP1(P1, P2) -> int:
    if P1 == P2:    # A draw
        return 0
    if (P1+1)%3 == P2:  #A loss; Modulo because the precedence is cyclic
        return -1
    return 1   # A win


# Generate a throw pseudo-randomly
def genRSP() -> int:
    throw = randint(0,2)
    return throw
