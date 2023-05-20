import random
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style
from private import Private
from corporal import Corporal
from captain import Captain
from major import Major

start_money = random.randint(10000, 15000)
start_money2 = random.randint(10000, 15000)
player_1_money = start_money
player_2_money = start_money2
game = True

player1_army = [Private(), Corporal(), Captain(), Major()]
player2_army = [Private(), Corporal(), Captain(), Major()]

while game:

    while True:
        print()
        print()
        try:
            print()
            print()
            print(f"{Fore.BLUE}Player 1")
            print("Amount of money:", player_1_money)
            print("1 Buy soldiers")
            print("2 Level up units")
            print("3 Attack enemy")
            print("4 Army status")
            choice = int(input("Choose action: "))
            if choice == 1:
                while True:
                    try:
                        print()
                        print()
                        print("Amount of money:", player_1_money)
                        print("1 Buy privates")
                        print("2 Buy corporals")
                        print("3 Buy captains")
                        print("4 Buy major")
                        print("5 End turn")
                        choice_buy = int(input("Choose action: "))

                        if choice_buy == 1:
                            while True:
                                print()
                                print()
                                max_buy_cost = player_1_money // 10
                                print("Amount of money:", player_1_money)
                                print("max amount of privates to buy: ", max_buy_cost)
                                buy_privates = int(input("enter amount of privates to buy: "))

                                if buy_privates < 0 or buy_privates * 10 > player_1_money:
                                    print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                else:
                                    player1_army[0].buy_privates(buy_privates)
                                    player_1_money -= buy_privates * 10
                                    print("Bought privates", buy_privates)
                                    break

                        elif choice_buy == 2:
                            while True:
                                print()
                                print()
                                max_buy_cost = player_1_money // 20
                                print("Amount of money:", player_1_money)
                                print("max amount of corporals to buy: ", max_buy_cost)
                                buy_corporals = int(input("enter amount of corporals to buy:"))

                                if buy_corporals < 0 or buy_corporals * 20 > player_1_money:
                                    print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                else:
                                    player1_army[1].buy_corporals(buy_corporals)
                                    player_1_money -= buy_corporals * 20
                                    print("Bought corporals:", buy_corporals)
                                    break

                        elif choice_buy == 3:
                            while True:
                                print()
                                print()
                                max_buy_cost = player_1_money // 30
                                print("Amount of money:", player_1_money)
                                print("max amount of captains to buy:", max_buy_cost)
                                buy_captains = int(input("enter amount of captains to buy:"))

                                if buy_captains < 0 or buy_captains * 30 > player_1_money:
                                    print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                else:
                                    player1_army[2].buy_captains(buy_captains)
                                    player_1_money -= buy_captains * 30
                                    print("Bought captains:", buy_captains)
                                    break

                        elif choice_buy == 4:
                            while True:
                                print()
                                print()
                                max_buy_cost = player_1_money // 40
                                print("Amount of money:", player_1_money)
                                print("max amount of majors to buy:", max_buy_cost)
                                buy_majors = int(input("enter amount of majors to buy:"))

                                if buy_majors < 0 or buy_majors * 40 > player_1_money:
                                    print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                else:
                                    player1_army[3].buy_majors(buy_majors)
                                    player_1_money -= buy_majors * 40
                                    print("Bought majors:", buy_majors)
                                    break

                        elif choice_buy == 5:
                            break

                    except Exception as e:
                        print(f"{Fore.RED}incorrect choice {e} {Fore.BLUE}")
                        continue
                break
            elif choice == 2:
                while True:
                    try:
                        print()
                        print("Amount of money:", player_1_money)
                        print("1 Training privates")
                        print("2 Training corporals")
                        print("3 Training captains")
                        print("4 Training major")
                        print("5 End turn")
                        choice_training = int(input("Choose unit to train: "))
                        if choice_training == 1:
                            while True:
                                print()
                                print("Amount of money:", player_1_money)
                                index = 1
                                for _, j in player1_army[0].dict.items():
                                    print(f"{index} Training privates level {index}, amount: {j}")
                                    index += 1
                                print("6 End training privates")
                                choice_level_privates_to_training = int(input("Enter level of privates to training: "))
                                if choice_level_privates_to_training == 1:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of privates to training:",
                                          player1_army[0].dict["privates_level_1"])
                                    print("Privates level 1 amount:", player1_army[0].dict["privates_level_1"])
                                    amount_of_privates_to_training = int(input("Enter amount of privates to training:"))
                                    if amount_of_privates_to_training < 0 or amount_of_privates_to_training > \
                                            player1_army[0].dict[
                                                "privates_level_1"] or amount_of_privates_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[0].privates_promotion_level_1(amount_of_privates_to_training)
                                        player_1_money -= amount_of_privates_to_training
                                elif choice_level_privates_to_training == 2:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of privates to training:",
                                          player1_army[0].dict["privates_level_2"])
                                    print("Privates level 2 amount:", player1_army[0].dict["privates_level_2"])
                                    amount_of_privates_to_training = int(input("Enter amount of privates to training:"))
                                    if amount_of_privates_to_training < 0 or amount_of_privates_to_training > \
                                            player1_army[0].dict[
                                                "privates_level_2"] or amount_of_privates_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[0].privates_promotion_level_2(amount_of_privates_to_training)
                                        player_1_money -= amount_of_privates_to_training
                                elif choice_level_privates_to_training == 3:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of privates to training:",
                                          player1_army[0].dict["privates_level_3"])
                                    print("Privates level 3 amount:", player1_army[0].dict["privates_level_3"])
                                    amount_of_privates_to_training = int(input("Enter amount of privates to training:"))
                                    if amount_of_privates_to_training < 0 or amount_of_privates_to_training > \
                                            player1_army[0].dict[
                                                "privates_level_3"] or amount_of_privates_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[0].privates_promotion_level_3(amount_of_privates_to_training)
                                        player_1_money -= amount_of_privates_to_training
                                elif choice_level_privates_to_training == 4:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of privates to training:",
                                          player1_army[0].dict["privates_level_4"])
                                    print("Privates level 4 amount:", player1_army[0].dict["privates_level_4"])
                                    amount_of_privates_to_training = int(input("Enter amount of privates to training:"))
                                    if amount_of_privates_to_training < 0 or amount_of_privates_to_training > \
                                            player1_army[0].dict[
                                                "privates_level_4"] or amount_of_privates_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[0].privates_promotion_level_4(amount_of_privates_to_training)
                                        player_1_money -= amount_of_privates_to_training
                                elif choice_level_privates_to_training == 5:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of privates to training:",
                                          player1_army[0].dict["privates_level_5"])
                                    print("Privates level 5 amount:", player1_army[0].dict["privates_level_5"])
                                    amount_of_privates_to_training = int(input("Enter amount of privates to training:"))
                                    if amount_of_privates_to_training < 0 or amount_of_privates_to_training > \
                                            player1_army[0].dict[
                                                "privates_level_5"] or amount_of_privates_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[0].privates_promotion_level_5(amount_of_privates_to_training)
                                        player1_army[1].corporals_promotion_from_privates(
                                            amount_of_privates_to_training)
                                        player_1_money -= amount_of_privates_to_training
                                elif choice_level_privates_to_training == 6:
                                    break
                                else:
                                    print("Incorret value")

                        elif choice_training == 2:
                            while True:
                                print()
                                print("Amount of money:", player_1_money)
                                index = 1
                                for _, j in player1_army[1].dict.items():
                                    print(f"{index} Training corporals level {index}, amount: {j}")
                                    index += 1
                                print("6 End training corporals")
                                choice_level_corporals_to_training = int(
                                    input("Enter level of corporals to training: "))
                                if choice_level_corporals_to_training == 1:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of corporals to training:",
                                          player1_army[1].dict["corporals_level_1"])
                                    print("corporals level 1 amount:", player1_army[1].dict["corporals_level_1"])
                                    amount_of_corporals_to_training = int(
                                        input("Enter amount of corporals to training:"))
                                    if amount_of_corporals_to_training < 1 or amount_of_corporals_to_training > \
                                            player1_army[1].dict[
                                                "corporals_level_1"] or amount_of_corporals_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[1].corporals_promotion_level_1(amount_of_corporals_to_training)
                                        player_1_money -= amount_of_corporals_to_training
                                elif choice_level_corporals_to_training == 2:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of corporals to training:",
                                          player1_army[1].dict["corporals_level_2"])
                                    print("corporals level 2 amount:", player1_army[1].dict["corporals_level_2"])
                                    amount_of_corporals_to_training = int(
                                        input("Enter amount of corporals to training:"))
                                    if amount_of_corporals_to_training < 1 or amount_of_corporals_to_training > \
                                            player1_army[1].dict[
                                                "corporals_level_2"] or amount_of_corporals_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[1].corporals_promotion_level_2(amount_of_corporals_to_training)
                                        player_1_money -= amount_of_corporals_to_training
                                elif choice_level_corporals_to_training == 3:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of corporals to training:",
                                          player1_army[1].dict["corporals_level_3"])
                                    print("corporals level 3 amount:", player1_army[1].dict["corporals_level_3"])
                                    amount_of_corporals_to_training = int(
                                        input("Enter amount of corporals to training:"))
                                    if amount_of_corporals_to_training < 1 or amount_of_corporals_to_training > \
                                            player1_army[1].dict[
                                                "corporals_level_3"] or amount_of_corporals_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[1].corporals_promotion_level_3(amount_of_corporals_to_training)
                                        player_1_money -= amount_of_corporals_to_training
                                elif choice_level_corporals_to_training == 4:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of corporals to training:",
                                          player1_army[1].dict["corporals_level_4"])
                                    print("corporals level 4 amount:", player1_army[1].dict["corporals_level_4"])
                                    amount_of_corporals_to_training = int(
                                        input("Enter amount of corporals to training:"))
                                    if amount_of_corporals_to_training < 1 or amount_of_corporals_to_training > \
                                            player1_army[1].dict[
                                                "corporals_level_4"] or amount_of_corporals_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[1].corporals_promotion_level_4(amount_of_corporals_to_training)
                                        player_1_money -= amount_of_corporals_to_training
                                elif choice_level_corporals_to_training == 5:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of corporals to training:",
                                          player1_army[1].dict["corporals_level_5"])
                                    print("corporals level 5 amount:", player1_army[1].dict["corporals_level_5"])
                                    amount_of_corporals_to_training = int(
                                        input("Enter amount of corporals to training:"))
                                    if amount_of_corporals_to_training < 1 or amount_of_corporals_to_training > \
                                            player1_army[1].dict[
                                                "corporals_level_5"] or amount_of_corporals_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[1].corporals_promotion_level_5(amount_of_corporals_to_training)
                                        player1_army[2].captains_promotion_from_corporals(
                                            amount_of_corporals_to_training)
                                        player_1_money -= amount_of_corporals_to_training
                                elif choice_level_corporals_to_training == 6:
                                    break
                                else:
                                    print("Incorret value")

                        elif choice_training == 3:
                            while True:
                                print()
                                print("Amount of money:", player_1_money)
                                index = 1
                                for _, j in player1_army[2].dict.items():
                                    print(f"{index} Training captains level {index}, amount: {j}")
                                    index += 1
                                print("6 End training captains")
                                choice_level_captains_to_training = int(input("Enter level of captains to training: "))
                                if choice_level_captains_to_training == 1:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of captains to training:",
                                          player1_army[2].dict["captains_level_1"])
                                    print("captains level 1 amount:", player1_army[2].dict["captains_level_1"])
                                    amount_of_captains_to_training = int(input("Enter amount of captains to training:"))
                                    if amount_of_captains_to_training < 1 or amount_of_captains_to_training > \
                                            player1_army[2].dict[
                                                "captains_level_1"] or amount_of_captains_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[2].captains_promotion_level_1(amount_of_captains_to_training)
                                        player_1_money -= amount_of_captains_to_training
                                elif choice_level_captains_to_training == 2:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of captains to training:",
                                          player1_army[2].dict["captains_level_2"])
                                    print("captains level 2 amount:", player1_army[2].dict["captains_level_2"])
                                    amount_of_captains_to_training = int(input("Enter amount of captains to training:"))
                                    if amount_of_captains_to_training < 1 or amount_of_captains_to_training > \
                                            player1_army[2].dict[
                                                "captains_level_2"] or amount_of_captains_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[2].captains_promotion_level_2(amount_of_captains_to_training)
                                        player_1_money -= amount_of_captains_to_training
                                elif choice_level_captains_to_training == 3:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of captains to training:",
                                          player1_army[2].dict["captains_level_3"])
                                    print("captains level 3 amount:", player1_army[2].dict["captains_level_3"])
                                    amount_of_captains_to_training = int(input("Enter amount of captains to training:"))
                                    if amount_of_captains_to_training < 1 or amount_of_captains_to_training > \
                                            player1_army[2].dict[
                                                "captains_level_3"] or amount_of_captains_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[2].captains_promotion_level_3(amount_of_captains_to_training)
                                        player_1_money -= amount_of_captains_to_training
                                elif choice_level_captains_to_training == 4:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of captains to training:",
                                          player1_army[2].dict["captains_level_4"])
                                    print("captains level 4 amount:", player1_army[2].dict["captains_level_4"])
                                    amount_of_captains_to_training = int(input("Enter amount of captains to training:"))
                                    if amount_of_captains_to_training < 1 or amount_of_captains_to_training > \
                                            player1_army[2].dict[
                                                "captains_level_4"] or amount_of_captains_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[2].captains_promotion_level_4(amount_of_captains_to_training)
                                        player_1_money -= amount_of_captains_to_training
                                elif choice_level_captains_to_training == 5:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of captains to training:",
                                          player1_army[2].dict["captains_level_5"])
                                    print("captains level 5 amount:", player1_army[2].dict["captains_level_5"])
                                    amount_of_captains_to_training = int(input("Enter amount of captains to training:"))
                                    if amount_of_captains_to_training < 1 or amount_of_captains_to_training > \
                                            player1_army[2].dict[
                                                "captains_level_5"] or amount_of_captains_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[2].captains_promotion_level_5(amount_of_captains_to_training)
                                        player1_army[3].majors_promotion_from_captains(amount_of_captains_to_training)
                                        player_1_money -= amount_of_captains_to_training
                                elif choice_level_captains_to_training == 6:
                                    break
                                else:
                                    print("Incorret value")


                        elif choice_training == 4:
                            while True:
                                print()
                                print("Amount of money:", player_1_money)
                                index = 1
                                print(f"""1 Training privates level 1, amount: {player2_army[3].dict["majors_level_1"]}
                                       2 Training privates level 2, amount: {player2_army[3].dict["majors_level_2"]}
                                       3 Training privates level 3, amount: {player2_army[3].dict["majors_level_3"]}
                                       4 Training privates level 4, amount: {player2_army[3].dict["majors_level_4"]}""")
                                print("6 End training majors")
                                choice_level_majors_to_training = int(input("Enter level of majors to training: "))
                                if choice_level_majors_to_training == 1:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of majors to training:", player1_army[3].dict["majors_level_1"])
                                    print("majors level 1 amount:", player1_army[3].dict["majors_level_1"])
                                    amount_of_majors_to_training = int(input("Enter amount of majors to training:"))
                                    if amount_of_majors_to_training < 1 or amount_of_majors_to_training > \
                                            player1_army[3].dict[
                                                "majors_level_1"] or amount_of_majors_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[3].majors_promotion_level_1(amount_of_majors_to_training)
                                        player_1_money -= amount_of_majors_to_training
                                elif choice_level_majors_to_training == 2:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of majors to training:", player1_army[3].dict["majors_level_2"])
                                    print("majors level 2 amount:", player1_army[3].dict["majors_level_2"])
                                    amount_of_majors_to_training = int(input("Enter amount of majors to training:"))
                                    if amount_of_majors_to_training < 1 or amount_of_majors_to_training > \
                                            player1_army[3].dict[
                                                "majors_level_2"] or amount_of_majors_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[3].majors_promotion_level_2(amount_of_majors_to_training)
                                        player_1_money -= amount_of_majors_to_training
                                elif choice_level_majors_to_training == 3:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of majors to training:", player1_army[3].dict["majors_level_3"])
                                    print("majors level 3 amount:", player1_army[3].dict["majors_level_3"])
                                    amount_of_majors_to_training = int(input("Enter amount of majors to training:"))
                                    if amount_of_majors_to_training < 1 or amount_of_majors_to_training > \
                                            player1_army[3].dict[
                                                "majors_level_3"] or amount_of_majors_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[3].majors_promotion_level_3(amount_of_majors_to_training)
                                        player_1_money -= amount_of_majors_to_training
                                elif choice_level_majors_to_training == 4:
                                    print()
                                    print("Amount of money:", player_1_money)
                                    print("Max amount of majors to training:", player1_army[3].dict["majors_level_4"])
                                    print("majors level 4 amount:", player1_army[3].dict["majors_level_4"])
                                    amount_of_majors_to_training = int(input("Enter amount of majors to training:"))
                                    if amount_of_majors_to_training < 1 or amount_of_majors_to_training > \
                                            player1_army[3].dict[
                                                "majors_level_4"] or amount_of_majors_to_training > player_1_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.BLUE}")
                                    else:
                                        player1_army[3].majors_promotion_level_4(amount_of_majors_to_training)
                                        player_1_money -= amount_of_majors_to_training

                                elif choice_level_majors_to_training == 5:
                                    break
                                else:
                                    print("Incorret value")

                        elif choice_training == 5:
                            break

                    except Exception as e:
                        print(f"{Fore.RED}incorrect choice {e} {Fore.BLUE}")
                        continue
                break


            elif choice == 3:
                print("attack enemy")

            elif choice == 4:
                print()
                print("Army:")
                index = 1
                for _, j in player1_army[0].dict.items():
                    print(f"Privates level {index}, amount: {j}")
                    index += 1
                print()
                index = 1
                for _, j in player1_army[1].dict.items():
                    print(f"Corporal level {index}, amount: {j}")
                    index += 1
                print()
                index = 1
                for _, j in player1_army[2].dict.items():
                    print(f"Captains level {index}, amount: {j}")
                    index += 1
                print()
                index = 1
                for _, j in player1_army[3].dict.items():
                    print(f"Majors level {index}, amount: {j}")
                    index += 1
                army_strenght = player1_army[0].all_privates_strength() + player1_army[1].all_corporals_strength() + \
                                player1_army[2].all_captains_strength() + player1_army[3].all_majors_strength()
                print("Army strength:", army_strenght)
                continue
        except Exception as e:
            print(f"{Fore.RED}incorrect choice {e} {Fore.BLUE}")
            continue

    # PLAYER 2
    while True:
        print()
        print()
        try:
            print()
            print()
            print(f"{Fore.MAGENTA}Player 1")
            print("Amount of money:", player_2_money)
            print("1 Buy soldiers")
            print("2 Level up units")
            print("3 Attack enemy")
            print("4 Army status")
            choice = int(input("Choose action: "))
            if choice == 1:
                while True:
                    try:
                        print()
                        print()
                        print("Amount of money:", player_2_money)
                        print("1 Buy privates")
                        print("2 Buy corporals")
                        print("3 Buy captains")
                        print("4 Buy major")
                        print("5 End turn")
                        choice_buy = int(input("Choose action: "))

                        if choice_buy == 1:
                            while True:
                                print()
                                print()
                                max_buy_cost = player_2_money // 10
                                print("Amount of money:", player_2_money)
                                print("max amount of privates to buy: ", max_buy_cost)
                                buy_privates = int(input("enter amount of privates to buy: "))

                                if buy_privates < 0 or buy_privates * 10 > player_2_money:
                                    print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                else:
                                    player2_army[0].buy_privates(buy_privates)
                                    player_2_money -= buy_privates * 10
                                    print("Bought privates", buy_privates)
                                    break

                        elif choice_buy == 2:
                            while True:
                                print()
                                print()
                                max_buy_cost = player_2_money // 20
                                print("Amount of money:", player_2_money)
                                print("max amount of corporals to buy: ", max_buy_cost)
                                buy_corporals = int(input("enter amount of corporals to buy:"))

                                if buy_corporals < 0 or buy_corporals * 20 > player_2_money:
                                    print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                else:
                                    player2_army[1].buy_corporals(buy_corporals)
                                    player_2_money -= buy_corporals * 20
                                    print("Bought corporals:", buy_corporals)
                                    break

                        elif choice_buy == 3:
                            while True:
                                print()
                                print()
                                max_buy_cost = player_2_money // 30
                                print("Amount of money:", player_2_money)
                                print("max amount of captains to buy:", max_buy_cost)
                                buy_captains = int(input("enter amount of captains to buy:"))

                                if buy_captains < 0 or buy_captains * 30 > player_2_money:
                                    print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                else:
                                    player2_army[2].buy_captains(buy_captains)
                                    player_2_money -= buy_captains * 30
                                    print("Bought captains:", buy_captains)
                                    break

                        elif choice_buy == 4:
                            while True:
                                print()
                                print()
                                max_buy_cost = player_2_money // 40
                                print("Amount of money:", player_2_money)
                                print("max amount of majors to buy:", max_buy_cost)
                                buy_majors = int(input("enter amount of majors to buy:"))

                                if buy_majors < 0 or buy_majors * 40 > player_2_money:
                                    print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                else:
                                    player2_army[3].buy_majors(buy_majors)
                                    player_2_money -= buy_majors * 40
                                    print("Bought majors:", buy_majors)
                                    break

                        elif choice_buy == 5:
                            break

                    except Exception as e:
                        print(f"{Fore.RED}incorrect choice {e} {Fore.MAGENTA}")
                        continue
                break
            elif choice == 2:
                while True:
                    try:
                        print()
                        print("Amount of money:", player_2_money)
                        print("1 Training privates")
                        print("2 Training corporals")
                        print("3 Training captains")
                        print("4 Training major")
                        print("5 End turn")
                        choice_training = int(input("Choose unit to train: "))
                        if choice_training == 1:
                            while True:
                                print()
                                print("Amount of money:", player_2_money)
                                index = 1
                                for _, j in player2_army[0].dict.items():
                                    print(f"{index} Training privates level {index}, amount: {j}")
                                    index += 1
                                print("6 End training privates")
                                choice_level_privates_to_training = int(input("Enter level of privates to training: "))
                                if choice_level_privates_to_training == 1:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of privates to training:",
                                          player2_army[0].dict["privates_level_1"])
                                    print("Privates level 1 amount:", player2_army[0].dict["privates_level_1"])
                                    amount_of_privates_to_training = int(input("Enter amount of privates to training:"))
                                    if amount_of_privates_to_training < 0 or amount_of_privates_to_training > \
                                            player2_army[0].dict[
                                                "privates_level_1"] or amount_of_privates_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[0].privates_promotion_level_1(amount_of_privates_to_training)
                                        player_2_money -= amount_of_privates_to_training
                                elif choice_level_privates_to_training == 2:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of privates to training:",
                                          player2_army[0].dict["privates_level_2"])
                                    print("Privates level 2 amount:", player2_army[0].dict["privates_level_2"])
                                    amount_of_privates_to_training = int(input("Enter amount of privates to training:"))
                                    if amount_of_privates_to_training < 0 or amount_of_privates_to_training > \
                                            player2_army[0].dict[
                                                "privates_level_2"] or amount_of_privates_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[0].privates_promotion_level_2(amount_of_privates_to_training)
                                        player_2_money -= amount_of_privates_to_training
                                elif choice_level_privates_to_training == 3:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of privates to training:",
                                          player2_army[0].dict["privates_level_3"])
                                    print("Privates level 3 amount:", player2_army[0].dict["privates_level_3"])
                                    amount_of_privates_to_training = int(input("Enter amount of privates to training:"))
                                    if amount_of_privates_to_training < 0 or amount_of_privates_to_training > \
                                            player2_army[0].dict[
                                                "privates_level_3"] or amount_of_privates_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[0].privates_promotion_level_3(amount_of_privates_to_training)
                                        player_2_money -= amount_of_privates_to_training
                                elif choice_level_privates_to_training == 4:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of privates to training:",
                                          player2_army[0].dict["privates_level_4"])
                                    print("Privates level 4 amount:", player2_army[0].dict["privates_level_4"])
                                    amount_of_privates_to_training = int(input("Enter amount of privates to training:"))
                                    if amount_of_privates_to_training < 0 or amount_of_privates_to_training > \
                                            player2_army[0].dict[
                                                "privates_level_4"] or amount_of_privates_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[0].privates_promotion_level_4(amount_of_privates_to_training)
                                        player_2_money -= amount_of_privates_to_training
                                elif choice_level_privates_to_training == 5:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of privates to training:",
                                          player2_army[0].dict["privates_level_5"])
                                    print("Privates level 5 amount:", player2_army[0].dict["privates_level_5"])
                                    amount_of_privates_to_training = int(input("Enter amount of privates to training:"))
                                    if amount_of_privates_to_training < 0 or amount_of_privates_to_training > \
                                            player2_army[0].dict[
                                                "privates_level_5"] or amount_of_privates_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[0].privates_promotion_level_5(amount_of_privates_to_training)
                                        player2_army[1].corporals_promotion_from_privates(
                                            amount_of_privates_to_training)
                                        player_2_money -= amount_of_privates_to_training
                                elif choice_level_privates_to_training == 6:
                                    break
                                else:
                                    print("Incorret value")

                        elif choice_training == 2:
                            while True:
                                print()
                                print("Amount of money:", player_2_money)
                                index = 1
                                for _, j in player2_army[1].dict.items():
                                    print(f"{index} Training corporals level {index}, amount: {j}")
                                    index += 1
                                print("6 End training corporals")
                                choice_level_corporals_to_training = int(
                                    input("Enter level of corporals to training: "))
                                if choice_level_corporals_to_training == 1:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of corporals to training:",
                                          player2_army[1].dict["corporals_level_1"])
                                    print("corporals level 1 amount:", player2_army[1].dict["corporals_level_1"])
                                    amount_of_corporals_to_training = int(
                                        input("Enter amount of corporals to training:"))
                                    if amount_of_corporals_to_training < 1 or amount_of_corporals_to_training > \
                                            player2_army[1].dict[
                                                "corporals_level_1"] or amount_of_corporals_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[1].corporals_promotion_level_1(amount_of_corporals_to_training)
                                        player_2_money -= amount_of_corporals_to_training
                                elif choice_level_corporals_to_training == 2:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of corporals to training:",
                                          player2_army[1].dict["corporals_level_2"])
                                    print("corporals level 2 amount:", player2_army[1].dict["corporals_level_2"])
                                    amount_of_corporals_to_training = int(
                                        input("Enter amount of corporals to training:"))
                                    if amount_of_corporals_to_training < 1 or amount_of_corporals_to_training > \
                                            player2_army[1].dict[
                                                "corporals_level_2"] or amount_of_corporals_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[1].corporals_promotion_level_2(amount_of_corporals_to_training)
                                        player_2_money -= amount_of_corporals_to_training
                                elif choice_level_corporals_to_training == 3:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of corporals to training:",
                                          player2_army[1].dict["corporals_level_3"])
                                    print("corporals level 3 amount:", player2_army[1].dict["corporals_level_3"])
                                    amount_of_corporals_to_training = int(
                                        input("Enter amount of corporals to training:"))
                                    if amount_of_corporals_to_training < 1 or amount_of_corporals_to_training > \
                                            player2_army[1].dict[
                                                "corporals_level_3"] or amount_of_corporals_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[1].corporals_promotion_level_3(amount_of_corporals_to_training)
                                        player_2_money -= amount_of_corporals_to_training
                                elif choice_level_corporals_to_training == 4:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of corporals to training:",
                                          player2_army[1].dict["corporals_level_4"])
                                    print("corporals level 4 amount:", player2_army[1].dict["corporals_level_4"])
                                    amount_of_corporals_to_training = int(
                                        input("Enter amount of corporals to training:"))
                                    if amount_of_corporals_to_training < 1 or amount_of_corporals_to_training > \
                                            player2_army[1].dict[
                                                "corporals_level_4"] or amount_of_corporals_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[1].corporals_promotion_level_4(amount_of_corporals_to_training)
                                        player_2_money -= amount_of_corporals_to_training
                                elif choice_level_corporals_to_training == 5:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of corporals to training:",
                                          player2_army[1].dict["corporals_level_5"])
                                    print("corporals level 5 amount:", player2_army[1].dict["corporals_level_5"])
                                    amount_of_corporals_to_training = int(
                                        input("Enter amount of corporals to training:"))
                                    if amount_of_corporals_to_training < 1 or amount_of_corporals_to_training > \
                                            player2_army[1].dict[
                                                "corporals_level_5"] or amount_of_corporals_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[1].corporals_promotion_level_5(amount_of_corporals_to_training)
                                        player2_army[2].captains_promotion_from_corporals(
                                            amount_of_corporals_to_training)
                                        player_2_money -= amount_of_corporals_to_training
                                elif choice_level_corporals_to_training == 6:
                                    break
                                else:
                                    print("Incorret value")
                            break
                        elif choice_training == 3:
                            while True:
                                print()
                                print("Amount of money:", player_2_money)
                                index = 1
                                for _, j in player2_army[2].dict.items():
                                    print(f"{index} Training captains level {index}, amount: {j}")
                                    index += 1
                                print("6 End training captains")
                                choice_level_captains_to_training = int(input("Enter level of captains to training: "))
                                if choice_level_captains_to_training == 1:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of captains to training:",
                                          player2_army[2].dict["captains_level_1"])
                                    print("captains level 1 amount:", player2_army[2].dict["captains_level_1"])
                                    amount_of_captains_to_training = int(input("Enter amount of captains to training:"))
                                    if amount_of_captains_to_training < 1 or amount_of_captains_to_training > \
                                            player2_army[2].dict[
                                                "captains_level_1"] or amount_of_captains_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[2].captains_promotion_level_1(amount_of_captains_to_training)
                                        player_2_money -= amount_of_captains_to_training
                                elif choice_level_captains_to_training == 2:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of captains to training:",
                                          player2_army[2].dict["captains_level_2"])
                                    print("captains level 2 amount:", player2_army[2].dict["captains_level_2"])
                                    amount_of_captains_to_training = int(input("Enter amount of captains to training:"))
                                    if amount_of_captains_to_training < 1 or amount_of_captains_to_training > \
                                            player2_army[2].dict[
                                                "captains_level_2"] or amount_of_captains_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[2].captains_promotion_level_2(amount_of_captains_to_training)
                                        player_2_money -= amount_of_captains_to_training
                                elif choice_level_captains_to_training == 3:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of captains to training:",
                                          player2_army[2].dict["captains_level_3"])
                                    print("captains level 3 amount:", player2_army[2].dict["captains_level_3"])
                                    amount_of_captains_to_training = int(input("Enter amount of captains to training:"))
                                    if amount_of_captains_to_training < 1 or amount_of_captains_to_training > \
                                            player2_army[2].dict[
                                                "captains_level_3"] or amount_of_captains_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[2].captains_promotion_level_3(amount_of_captains_to_training)
                                        player_2_money -= amount_of_captains_to_training
                                elif choice_level_captains_to_training == 4:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of captains to training:",
                                          player2_army[2].dict["captains_level_4"])
                                    print("captains level 4 amount:", player2_army[2].dict["captains_level_4"])
                                    amount_of_captains_to_training = int(input("Enter amount of captains to training:"))
                                    if amount_of_captains_to_training < 1 or amount_of_captains_to_training > \
                                            player2_army[2].dict[
                                                "captains_level_4"] or amount_of_captains_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[2].captains_promotion_level_4(amount_of_captains_to_training)
                                        player_2_money -= amount_of_captains_to_training
                                elif choice_level_captains_to_training == 5:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of captains to training:",
                                          player2_army[2].dict["captains_level_5"])
                                    print("captains level 5 amount:", player2_army[2].dict["captains_level_5"])
                                    amount_of_captains_to_training = int(input("Enter amount of captains to training:"))
                                    if amount_of_captains_to_training < 1 or amount_of_captains_to_training > \
                                            player2_army[2].dict[
                                                "captains_level_5"] or amount_of_captains_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[2].captains_promotion_level_5(amount_of_captains_to_training)
                                        player2_army[3].majors_promotion_from_captains(amount_of_captains_to_training)
                                        player_2_money -= amount_of_captains_to_training
                                elif choice_level_captains_to_training == 6:
                                    break
                                else:
                                    print("Incorret value")


                        elif choice_training == 4:
                            while True:
                                print()
                                print("Amount of money:", player_2_money)
                                index = 1
                                print(f"""1 Training privates level 1, amount: {player2_army[3].dict["majors_level_1"]}
           2 Training privates level 2, amount: {player2_army[3].dict["majors_level_2"]}
           3 Training privates level 3, amount: {player2_army[3].dict["majors_level_3"]}
           4 Training privates level 4, amount: {player2_army[3].dict["majors_level_4"]}""")
                                print("5 End training majors")
                                choice_level_majors_to_training = int(input("Enter level of majors to training: "))
                                if choice_level_majors_to_training == 1:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of majors to training:", player2_army[3].dict["majors_level_1"])
                                    print("majors level 1 amount:", player2_army[3].dict["majors_level_1"])
                                    amount_of_majors_to_training = int(input("Enter amount of majors to training:"))
                                    if amount_of_majors_to_training < 1 or amount_of_majors_to_training > \
                                            player2_army[3].dict[
                                                "majors_level_1"] or amount_of_majors_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[3].majors_promotion_level_1(amount_of_majors_to_training)
                                        player_2_money -= amount_of_majors_to_training
                                elif choice_level_majors_to_training == 2:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of majors to training:", player2_army[3].dict["majors_level_2"])
                                    print("majors level 2 amount:", player2_army[3].dict["majors_level_2"])
                                    amount_of_majors_to_training = int(input("Enter amount of majors to training:"))
                                    if amount_of_majors_to_training < 1 or amount_of_majors_to_training > \
                                            player2_army[3].dict[
                                                "majors_level_2"] or amount_of_majors_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[3].majors_promotion_level_2(amount_of_majors_to_training)
                                        player_2_money -= amount_of_majors_to_training
                                elif choice_level_majors_to_training == 3:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of majors to training:", player2_army[3].dict["majors_level_3"])
                                    print("majors level 3 amount:", player2_army[3].dict["majors_level_3"])
                                    amount_of_majors_to_training = int(input("Enter amount of majors to training:"))
                                    if amount_of_majors_to_training < 1 or amount_of_majors_to_training > \
                                            player2_army[3].dict[
                                                "majors_level_3"] or amount_of_majors_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[3].majors_promotion_level_3(amount_of_majors_to_training)
                                        player_2_money -= amount_of_majors_to_training
                                elif choice_level_majors_to_training == 4:
                                    print()
                                    print("Amount of money:", player_2_money)
                                    print("Max amount of majors to training:", player2_army[3].dict["majors_level_4"])
                                    print("majors level 4 amount:", player2_army[3].dict["majors_level_4"])
                                    amount_of_majors_to_training = int(input("Enter amount of majors to training:"))
                                    if amount_of_majors_to_training < 1 or amount_of_majors_to_training > \
                                            player2_army[3].dict[
                                                "majors_level_4"] or amount_of_majors_to_training > player_2_money:
                                        print(f"{Fore.RED}incorrect value or not enough money to buy{Fore.MAGENTA}")
                                    else:
                                        player2_army[3].majors_promotion_level_4(amount_of_majors_to_training)
                                        player_2_money -= amount_of_majors_to_training

                                elif choice_level_majors_to_training == 5:
                                    break
                                else:
                                    print("Incorret value")


                        elif choice_training == 5:
                            break
                    except Exception as e:
                        print(f"{Fore.RED}incorrect choice {e} {Fore.MAGENTA}")
                        continue


            elif choice == 3:
                print("attack enemy")

            elif choice == 4:
                print()
                print("Army:")
                index = 1
                for _, j in player2_army[0].dict.items():
                    print(f"Privates level {index}, amount: {j}")
                    index += 1
                print()
                index = 1
                for _, j in player2_army[1].dict.items():
                    print(f"Corporal level {index}, amount: {j}")
                    index += 1
                print()
                index = 1
                for _, j in player2_army[2].dict.items():
                    print(f"Captains level {index}, amount: {j}")
                    index += 1
                print()
                index = 1
                for _, j in player2_army[3].dict.items():
                    print(f"Majors level {index}, amount: {j}")
                    index += 1
                army_strenght = player2_army[0].all_privates_strength() + player2_army[1].all_corporals_strength() + \
                                player2_army[2].all_captains_strength() + player2_army[3].all_majors_strength()
                print("Army strength:", army_strenght)
                continue
        except Exception as e:
            print(f"{Fore.RED}incorrect choice {e} {Fore.MAGENTA}")
            continue
        break
