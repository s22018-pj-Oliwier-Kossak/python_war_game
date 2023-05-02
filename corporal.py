from colorama import Fore


class Corporal():
    """Class to create corporals soldiers"""

    def __init__(self, money=0, dict=None):
        self.money = money
        self.dict = {
            "corporals_level_1": 0,
            "corporals_level_2": 0,
            "corporals_level_3": 0,
            "corporals_level_4": 0,
            "corporals_level_5": 0
        }

    def display_all_corporals(self):
        """The function which display all corporals"""
        i = 1
        for x, y in self.dict.items():
            print(f"corporals level {i}:", y)
            i += 1

    def display_strength_all_corporals(self):
        """The function which display strength of all corporals"""
        strength_all_corporals = self.dict["corporals_level_1"] * 2 * 1 + self.dict["corporals_level_2"] * 2 * 2 + \
                                 self.dict[
                                     "corporals_level_3"] * 2 * 3 + self.dict["corporals_level_4"] * 2 * 4 + self.dict[
                                     "corporals_level_5"] * 2 * 5
        return strength_all_corporals

    def buy_corporals_level_1(self):
        """The function allow to buy corporals level 1"""
        while True:
            max_buy = self.money // 20
            print("Your money:", self.money)
            print("Max corporals to buy:", max_buy)
            print("If want end buy corporals enter 0")
            value_of_corporals = int(input(("Enter amount of corporals to buy: ")))
            print("value_of_corporals", value_of_corporals)
            if not isinstance(value_of_corporals, int):
                print("incorrect type, money must be int type")
                print()
                continue

            if not 0 <= value_of_corporals * 20 <= self.money:
                print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                print()
                continue

            if value_of_corporals == 0:
                break
            else:
                self.money -= value_of_corporals * 20
                self.dict["corporals_level_1"] += value_of_corporals
                break
            print()

    def training_level_1_corporals(self):
        """The function allow to train corporals level one"""
        print()

        if self.dict["corporals_level_1"] == 0:
            print("You do not have corporals to train")

        else:
            while True:
                max_corporals_training = self.money//2
                print("Your money:", self.money)
                print("Max amount of corporals to training: %s , Cost of training all corporals: %s" % (
                    max_corporals_training*2, max_corporals_training*2))
                print("If want end to training of corporals enter 0")
                value_of_corporals = int(input(("Enter amount of corporals to training: ")))
                if not isinstance(value_of_corporals, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_corporals <= self.money//2:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                if value_of_corporals == 0:
                    break
                else:
                    self.money -= value_of_corporals
                    self.dict["corporals_level_1"] -= value_of_corporals
                    self.dict["corporals_level_2"] += value_of_corporals
                break
                print()

    def training_level_2_corporals(self):
        """The function allow to train corporals level two"""
        print()
        if self.dict["corporals_level_2"] == 0:
            print("You do not have corporals to train")
        else:
            while True:
                max_corporals_training = self.money // 2
                print("Your money:", self.money)
                print("Max amount of corporals to training: %s , Cost of training all corporals: %s" % (
                    max_corporals_training * 2, max_corporals_training * 2))
                print("If want end to training of corporals enter 0")
                value_of_corporals = int(input(("Enter amount of corporals to training: ")))
                if not isinstance(value_of_corporals, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_corporals <= self.money // 2:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                if value_of_corporals == 0:
                    break
                else:
                    self.money -= value_of_corporals
                    self.dict["corporals_level_2"] -= value_of_corporals
                    self.dict["corporals_level_3"] += value_of_corporals
                break
                print()

    def training_level_3_corporals(self):
        """The function allow to train corporals level three"""
        print()
        if self.dict["corporals_level_3"] == 0:
            print("You do not have corporals to train")
        else:
            while True:
                max_corporals_training = self.money // 2
                print("Your money:", self.money)
                print("Max amount of corporals to training: %s , Cost of training all corporals: %s" % (
                    max_corporals_training * 2, max_corporals_training * 2))
                print("If want end to training of corporals enter 0")
                value_of_corporals = int(input(("Enter amount of corporals to training: ")))
                if not isinstance(value_of_corporals, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_corporals <= self.money // 2:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                if value_of_corporals == 0:
                    break
                else:
                    self.money -= value_of_corporals
                    self.dict["corporals_level_3"] -= value_of_corporals
                    self.dict["corporals_level_4"] += value_of_corporals
                break
                print()

    def training_level_4_corporals(self):
        """The function allow to train corporals level four"""

        print()
        if self.dict["corporals_level_4"] == 0:
            print("You do not have corporals to train")
        else:
            while True:
                max_corporals_training = self.money // 2
                print("Your money:", self.money)
                print("Max amount of corporals to training: %s , Cost of training all corporals: %s" % (
                    max_corporals_training * 2, max_corporals_training * 2))
                print("If want end to training of corporals enter 0")
                value_of_corporals = int(input(("Enter amount of corporals to training: ")))
                if not isinstance(value_of_corporals, int):
                    print("incorrect type, money must be int type")
                    print()
                    continue
                if not 0 <= value_of_corporals <= self.money // 2:
                    print(f"{Fore.RED}not enough money or negative value {Fore.BLUE}")
                    print()
                    continue
                if value_of_corporals == 0:
                    break
                else:
                    self.money -= value_of_corporals
                    self.dict["corporals_level_4"] -= value_of_corporals
                    self.dict["corporals_level_5"] += value_of_corporals
                break
                print()
