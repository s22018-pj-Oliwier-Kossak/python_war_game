from private import Private
from colorama import Fore

player1_money = 1000
player1_army = [Private(player1_money)]
game = True


def choice_main():
    """The function allow to player choice first action"""
    print()
    print(f"{Fore.BLUE}Player 1")
    print("Player 1 money", player1_money)
    print("1 Check army")
    print("2 Buy soldiers")
    print("3 Training privates")
    print("4 Attack enemy")
    print("5 End turn")
    choice_player_1 = int(input("Your choice: "))
    return choice_player_1


def choice_units_to_buy():
    """The function allow to player buy units"""
    print()
    print(f"{Fore.BLUE}Player 1")
    print("Player 1 money", player1_money)
    print("1 Buy Privates")
    print("2 Buy Corporals")
    print("3 Captains")
    print("4 Majors")
    print("5 End turn")
    choice_player_1 = int(input("Your choice: "))
    return choice_player_1


while game:

    while True:

        choice_player_1 = choice_main()

        if not 0 < choice_player_1 <= 5:
            print(f"{Fore.RED}Incorrect choice {Fore.BLUE}")
            print()

        elif choice_player_1 == 1:
            player1_army[0].display_all_privates()
            print()

        elif choice_player_1 == 2:
            while True:
                choice_player_1_units_to_buy = choice_units_to_buy()
                if not 0 < choice_player_1_units_to_buy <= 5:
                    print(f"{Fore.RED}Incorrect choice {Fore.BLUE}")
                    print()
                elif choice_player_1_units_to_buy == 1:
                    player1_army[0].buy_privates_level_1()

                    print()
                elif choice_player_1_units_to_buy == 2:
                    print()
                elif choice_player_1_units_to_buy == 3:
                    print()
                elif choice_player_1_units_to_buy == 4:
                    print()
                elif choice_player_1_units_to_buy == 5:
                    print()
                    break
                print()
            break

        elif choice_player_1 == 3:
            while True:
                choice_player_1

                if not 0 < choice_player_1 <= 5:
                    print(f"{Fore.RED}Incorrect choice {Fore.BLUE}")
                    print()

                elif choice_player_1 == 1:
                    choice_player_1

                    if not 0 < choice_player_1 <= 5:
                        print(f"{Fore.RED}Incorrect choice {Fore.BLUE}")
                        print()
                    elif choice_player_1 == 1:
                        print()
                    elif choice_player_1 == 2:
                        print()
                    elif choice_player_1 == 3:
                        print()
                    elif choice_player_1 == 4:
                        print()
                    elif choice_player_1 == 5:
                        print()

                elif choice_player_1 == 2:
                    print()
                elif choice_player_1 == 3:
                    print()
                elif choice_player_1 == 4:
                    print()
                elif choice_player_1 == 5:
                    print()
                    break
                print()

            break
            print()

        elif choice_player_1 == 4:
            show_army(player1_army)
            print()

        elif choice_player_1 == 5:
            print()
            break

    print("break")
