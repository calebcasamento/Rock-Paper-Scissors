import random


def get_ai_choice():
    return random.choice(['r', 'p', 's'])
    
def get_choice():
    choice = ''
    while choice == '':
        choice = input("[r]ock, [p]aper, or [s]cissors? ")
        choice = validate_choice(choice)
    return choice

def validate_choice(choice):
    if choice.lower() in ['r', 'p', 's', 'rock', 'paper', 'scissors']:
        return choice.lower()[0]
    else:
        return ''

def play():
    player = get_choice()
    ai = get_ai_choice()
    check_winner(player, ai)

def check_winner(player, ai):
    print(f'Player chose {player}. AI chose {ai}')
    if player == 'r':
        if ai == 'r':
            print("It's a draw!")
        elif ai == 'p':
            print("AI wins!")
        else:
            print("You win!")
    elif player == 'p':
        if ai == 'r':
            print("You win!")
        elif ai == 'p':
            print("It's a draw!")
        else:
            print("AI wins!")
    else:
        if ai == 'r':
            print("AI wins!")
        elif ai == 'p':
            print("You win!")
        else:
            print("It's a draw!")

        
    
def main():
    print('Rock, Paper, Scissors!')
    play()

if __name__ == '__main__':
    main()
    
