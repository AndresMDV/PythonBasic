import random


def choose_options():
    options = ('piedra', 'papel', 'tijera')
    user_option = input("piedra, papel o tijera =>").lower()
    computer_option = random.choice(options)

    if not user_option in options:
        print("esa opcion no es valida")
        return None, None
        # continue

    print('User option =>', user_option)
    print('Computer option =>', computer_option)
    return user_option, computer_option


def check_rules(user_option, computer_option, user_wins, computer_wins):
    if user_option == computer_option:
        print("Empate!")
    elif user_option == "piedra":
        if computer_option == 'tijera':
            print("piedra gana a tijera")
            print("Usuario Gano")
            user_wins += 1
        else:
            print("papel gana a piedra")
            print("Computador Gano")
            computer_wins += 1
    elif user_option == 'papel':
        if computer_option == "piedra":
            print("papel gana a tijera")
            print("Usuario Gana")
            user_wins += 1
        else:
            print("tijera gana a papel")
            print("Computador Gana")
            computer_wins += 1
    elif user_option == "tijera":
        if computer_option == "papel":
            print("tijera gana a papel")
            print("Usuario Gana")
            user_wins += 1
        else:
            print("piedra gana a tijera")
            print("Computador Gana")
            computer_wins += 1
    return user_wins, computer_wins


def check_winner(user_wins, computer_wins):
    if computer_wins == 2:
        print('EL GRAN GANADOR ES LA COMPUTADORA')
    if user_wins == 2:
        print('EL GRAN GANADOR ES EL USUARIO')


def run_game():
    rounds = 1
    computer_wins = 0
    user_wins = 0
    while True:
        print('*' * 10)
        print('ROUND', rounds)
        print('*' * 10)
        print('PARTIDAS GANADAS COMPUTADOR', computer_wins)
        print('PARTIDAS GANADAS USUARIO', user_wins)

        user_option, computer_option = choose_options()
        if user_option != None:
            user_wins, computer_wins = check_rules(user_option,
                                                   computer_option,
                                                   user_wins,
                                                   computer_wins)
            check_winner(user_wins, computer_wins)
            rounds += 1


run_game()